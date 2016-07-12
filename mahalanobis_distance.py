# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MahalanobisDistance
                                 A QGIS plugin
 Calculates Mahalanobis distance
                              -------------------
        begin                : 2016-07-10
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Damian Michal Harasymczuk
        email                : d.harasymczuk@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, QFileInfo, Qt
from PyQt4.QtGui import QAction, QIcon, QDoubleSpinBox, QFileDialog, QMessageBox, QTableWidgetItem
from qgis.gui import QgsMapLayerComboBox, QgsMapLayerProxyModel
from qgis.core import QgsRasterLayer, QgsMapLayerRegistry
import resources_rc
from mahalanobis_distance_dialog import MahalanobisDistanceDialog
import os.path, gdal, numpy
from scipy.spatial.distance import cdist


class MahalanobisDistance:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'MahalanobisDistance_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = MahalanobisDistanceDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Mahalanobis Distance')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'Mahalanobis Distance')
        self.toolbar.setObjectName(u'Mahalanobis Distance')

        # signals and slots
        self.dlg.addBtn.clicked.connect(self.add_layer)
        self.dlg.removeBtn.clicked.connect(self.remove_layer)
        self.dlg.outputBtn.clicked.connect(self.output)
        self.dlg.buttonBox.accepted.connect(self.calculate)
        self.dlg.buttonBox.rejected.connect(self.dlg.close)

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('Mahalanobis Distance', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToRasterMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        icon_path = ':/plugins/MahalanobisDistance/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Calculate Mahalanobis distance'),
            callback=self.run,
            parent=self.iface.mainWindow())


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginRasterMenu(
                self.tr(u'&Mahalanobis Distance'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    def add_layer(self):
        i = self.dlg.table.rowCount()
        self.dlg.table.insertRow(i)

        layer = QgsMapLayerComboBox()
        layer.setFilters(QgsMapLayerProxyModel.RasterLayer)
        band = QTableWidgetItem('1')
        band.setFlags(Qt.ItemIsEnabled)
        mean = QDoubleSpinBox()
        mean.setRange(-10000.00,10000.00)

        self.dlg.table.setCellWidget(i, 0, layer)
        self.dlg.table.setItem(i, 1, band)
        self.dlg.table.setCellWidget(i, 2, mean)

    def remove_layer(self):
        self.dlg.table.removeRow(self.dlg.table.currentRow())

    def output(self):
        self.dlg.outputPath.setText(QFileDialog.getSaveFileName())

    def calculate(self):
        self.dlg.progressBar.setValue(0)
        rows = self.dlg.table.rowCount()
        if rows == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("Choose minimum one input layer!")
            msg.exec_()
            return
        paths = []
        means = []
        for row in range(rows):
            path = self.dlg.table.cellWidget(row, 0).currentLayer().source()
            mean = self.dlg.table.cellWidget(row, 2).value()
            paths.append(path)
            means.append(mean)
        rasters = []
        # parameters of the first raster
        f1 = gdal.Open(paths[0])
        size_x = f1.RasterXSize
        size_y = f1.RasterYSize
        proj = f1.GetProjection ()
        georef = f1.GetGeoTransform()
        del f1
        for path in paths:
            f = gdal.Open(path)
            raster = f.ReadAsArray()
            rasters.append(raster)
        # covariance matrix and inverted covariance matrix
        covariance = numpy.cov([i.ravel() for i in rasters])
        inv_covariance = numpy.linalg.inv(covariance)
        means = numpy.array(means)
        # calculate mahalanobis distances for each pixel
        rasters = numpy.dstack(rasters).reshape(-1, len(rasters))
        result = cdist(rasters, means[None, :], metric='mahalanobis', VI=inv_covariance)
        result = result.reshape(size_y, size_x)
        # new raster
        driver = gdal.GetDriverByName('GTiff')
        fileName = self.dlg.outputPath.text()
        output = driver.Create(fileName, size_x, size_y, 1, gdal.GDT_Float32)
        output.GetRasterBand(1).WriteArray(result)
        output.SetProjection( proj )
        output.SetGeoTransform( georef )
        output.FlushCache()
        output = None
        self.dlg.progressBar.setValue(100)
        # add result to canvas
        if self.dlg.checkBox.isChecked():
            fileInfo = QFileInfo(fileName)
            baseName = fileInfo.baseName()
            new_layer = QgsRasterLayer(fileName, baseName)
            QgsMapLayerRegistry.instance().addMapLayer(new_layer)

    def run(self):
        self.dlg.show()
        result = self.dlg.exec_()
        if result:
            pass

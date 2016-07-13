# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mahalanobis_distance_dialog_base.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MahalanobisDistanceDialogBase(object):
    def setupUi(self, MahalanobisDistanceDialogBase):
        MahalanobisDistanceDialogBase.setObjectName(_fromUtf8("MahalanobisDistanceDialogBase"))
        MahalanobisDistanceDialogBase.resize(475, 378)
        self.table = QtGui.QTableWidget(MahalanobisDistanceDialogBase)
        self.table.setGeometry(QtCore.QRect(10, 40, 455, 171))
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setColumnCount(3)
        self.table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setDefaultSectionSize(150)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setStretchLastSection(False)
        self.addBtn = QtGui.QPushButton(MahalanobisDistanceDialogBase)
        self.addBtn.setGeometry(QtCore.QRect(390, 220, 31, 31))
        self.addBtn.setObjectName(_fromUtf8("addBtn"))
        self.removeBtn = QtGui.QPushButton(MahalanobisDistanceDialogBase)
        self.removeBtn.setGeometry(QtCore.QRect(430, 220, 31, 31))
        self.removeBtn.setObjectName(_fromUtf8("removeBtn"))
        self.outputPath = QtGui.QLineEdit(MahalanobisDistanceDialogBase)
        self.outputPath.setGeometry(QtCore.QRect(10, 270, 371, 26))
        self.outputPath.setObjectName(_fromUtf8("outputPath"))
        self.outputBtn = QtGui.QPushButton(MahalanobisDistanceDialogBase)
        self.outputBtn.setGeometry(QtCore.QRect(390, 270, 71, 26))
        self.outputBtn.setObjectName(_fromUtf8("outputBtn"))
        self.checkBox = QtGui.QCheckBox(MahalanobisDistanceDialogBase)
        self.checkBox.setGeometry(QtCore.QRect(10, 310, 221, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.buttonBox = QtGui.QDialogButtonBox(MahalanobisDistanceDialogBase)
        self.buttonBox.setGeometry(QtCore.QRect(300, 340, 160, 26))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.progressBar = QtGui.QProgressBar(MahalanobisDistanceDialogBase)
        self.progressBar.setGeometry(QtCore.QRect(10, 340, 271, 26))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label = QtGui.QLabel(MahalanobisDistanceDialogBase)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(MahalanobisDistanceDialogBase)
        self.label_2.setGeometry(QtCore.QRect(10, 250, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(MahalanobisDistanceDialogBase)
        QtCore.QMetaObject.connectSlotsByName(MahalanobisDistanceDialogBase)

    def retranslateUi(self, MahalanobisDistanceDialogBase):
        MahalanobisDistanceDialogBase.setWindowTitle(_translate("MahalanobisDistanceDialogBase", "MahalanobisDistance", None))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MahalanobisDistanceDialogBase", "Layer", None))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MahalanobisDistanceDialogBase", "Band", None))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MahalanobisDistanceDialogBase", "Mean", None))
        self.addBtn.setToolTip(_translate("MahalanobisDistanceDialogBase", "Add", None))
        self.addBtn.setText(_translate("MahalanobisDistanceDialogBase", "+", None))
        self.removeBtn.setToolTip(_translate("MahalanobisDistanceDialogBase", "Remove", None))
        self.removeBtn.setText(_translate("MahalanobisDistanceDialogBase", "-", None))
        self.outputBtn.setText(_translate("MahalanobisDistanceDialogBase", "Browse", None))
        self.checkBox.setText(_translate("MahalanobisDistanceDialogBase", "Add result to canvas", None))
        self.label.setText(_translate("MahalanobisDistanceDialogBase", "Input rasters:", None))
        self.label_2.setText(_translate("MahalanobisDistanceDialogBase", "Output raster:", None))


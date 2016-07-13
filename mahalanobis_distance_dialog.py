# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MahalanobisDistanceDialog
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

import os

from PyQt4 import QtGui, uic
<<<<<<< HEAD
from mahalanobis_distance_dialog_base import Ui_MahalanobisDistanceDialogBase
#FORM_CLASS, _ = uic.loadUiType(os.path.join(
#    os.path.dirname(__file__), 'mahalanobis_distance_dialog_base.ui'))


class MahalanobisDistanceDialog(QtGui.QDialog, Ui_MahalanobisDistanceDialogBase):
=======

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'mahalanobis_distance_dialog_base.ui'))


class MahalanobisDistanceDialog(QtGui.QDialog, FORM_CLASS):
>>>>>>> a121f8a9e46fb5f9963d92e10881bb92270438fb
    def __init__(self, parent=None):
        """Constructor."""
        super(MahalanobisDistanceDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

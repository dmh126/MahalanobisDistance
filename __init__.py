# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MahalanobisDistance
                                 A QGIS plugin
 Calculates Mahalanobis distance
                             -------------------
        begin                : 2016-07-10
        copyright            : (C) 2016 by Damian Michal Harasymczuk
        email                : d.harasymczuk@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load MahalanobisDistance class from file MahalanobisDistance.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .mahalanobis_distance import MahalanobisDistance
    return MahalanobisDistance(iface)

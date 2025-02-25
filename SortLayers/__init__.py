# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SortLayers
                                 A QGIS plugin
 Description
                             -------------------
        copyright            : (C) 2024 by mminin
        email                : mminin2010@gmail.com
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
    """Load SortLayers class from file SortLayers.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .sort_layers import SortLayers
    return SortLayers(iface)

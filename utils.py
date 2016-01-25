#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Cristian García
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# You should have received a copy of the GNU General Public License
# along with this library; if not, write to the Free Software
# Foundation, 51 Franklin Street, Suite 500 Boston, MA 02110-1335 USA

import os

from constants import Hardware

from gi.repository import Gtk


def _get_dmi(node):
    ''' The desktop management interface should be a reliable source
    for product and version information. '''

    path = os.path.join('/sys/class/dmi/id', node)

    try:
        return open(path).readline().strip()

    except:
        return None


def get_screen_dpi():
    ''' Return screen DPI '''
    xft_dpi = Gtk.Settings.get_default().get_property('gtk-xft-dpi')
    dpi = float(xft_dpi / 1024)
    return dpi


def get_hardware():
    ''' Determine whether we are using XO 1.0, 1.5, ... or 'unknown'
    hardware '''

    version = _get_dmi('product_version')
    # product = _get_dmi('product_name')

    if version is None:
        hwinfo_path = '/bin/olpc-hwinfo'
        if os.path.exists(hwinfo_path) and os.access(hwinfo_path, os.X_OK):
            model = check_output([hwinfo_path, 'model'], 'unknown hardware')
            version = model.strip()

    if version == '1':
        return Hardware.XO1

    elif version == '1.5':
        return Hardware.XO15

    elif version == '1.75':
        return Hardware.XO4

    else:
        # Some systems (e.g. ARM) don't have dmi info
        if os.path.exists('/sys/devices/platform/lis3lv02d/position'):
            return Hardware.XO175

        elif os.path.exists('/etc/olpc-release'):
            return Hardware.XO1

        else:
            return Hardware.UNKNOWN


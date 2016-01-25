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

import toolbarbox

from gi.repository import Gtk

from sugar3.activity.activity import Activity


class MusicBlocks(Activity):

    def __init__(self, handle):
        Activity.__init__(self, handle)

        toolbarbox = toolbarbox.MBToolbarBox()
        self.set_toolbar_box(toolbarbox)

        self.show_all()


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

"""
from toolbarbox import MBToolbarBox
from area import MBArea

from gi.repository import Gtk

from sugar3.activity.activity import Activity

class MusicBlocks(Activity):

    def __init__(self, handle):
        Activity.__init__(self, handle)

        toolbarbox = MBToolbarBox(self)
        self.set_toolbar_box(toolbarbox)

        self.area = MBArea()
        self.set_canvas(self.area)

        self.show_all()
"""

import gi
gi.require_version("Gtk", "3.0")
gi.require_version('PangoCairo', '1.0')

from gi.repository import Gtk

from area import MBArea


class MusicBlocks(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)

        self.set_title("Music Blocks")
        self.maximize()

        self.vbox = Gtk.VBox()
        self.add(self.vbox)

        self._setup_canvas()

        self.connect("destroy", Gtk.main_quit)

        self.show_all()

    def _setup_canvas(self):
        scroll = Gtk.ScrolledWindow()
        self.vbox.pack_start(scroll, True, True, 0)

        self.area = MBArea()
        scroll.add(self.area)


if __name__ == "__main__":
    MusicBlocks()
    Gtk.main()


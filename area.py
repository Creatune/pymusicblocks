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

from constants import (PaletteOrienation as POrientation, AREA_BG_COLOR,
                       Hardware)

from utils import get_hardware, get_screen_dpi

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import PangoCairo


class MBArea(Gtk.DrawingArea):

    def __init__(self):
        Gtk.DrawingArea.__init__(self)

        self.set_size_request(Gdk.Screen.width() * 2, Gdk.Screen.height() * 2)
        self.set_can_focus(True)

        self.mouse_x = 0
        self.mouse_y = 0
        self.update_counter = 0
        self.running_blocks = False
        self.saving_blocks = False
        self.copying_blocks = False
        self.sharing_blocks = False
        self.deleting_blocks = False
        self.decimal_point = "."  # TODO: Try load the system decimal_point
                                  #       like Turtle Blocks

        self.orientation = POrientation.HORIZONTAL
        self.hw = get_hardware()
        self.lead = 1.0

        if self.hw in [Hardware.XO1, Hardware.XO15,
                       Hardware.XO175, Hardware.XO4]:
            self.scale = 1.0
            self.entry_scale = 0.67
            if self.hw == Hardware.XO1:
                self.color_mode = '565'

            else:
                self.color_mode = '888'

        else:
            self.scale = 1.0
            self.entry_scale = 1.0
            self.color_mode = '888'  # TODO: Read visual mode from gtk image

        self._set_screen_dpi()

        self.connect("draw", self._draw_cb)

    def _set_screen_dpi(self):
        dpi = get_screen_dpi()
        if self.hw in [Hardware.XO1, Hardware.XO15, Hardware.XO175]:
            dpi = 133  # Tweak for XO display color mode

        font_map_default = PangoCairo.font_map_get_default()
        font_map_default.set_resolution(dpi)

    def _draw_cb(self, area, context):
        self._draw_background(context)

    def _draw_background(self, ctx):
        alloc = self.get_allocation()

        ctx.set_source_rgb(*AREA_BG_COLOR)
        ctx.rectangle(0, 0, alloc.width, alloc.height)
        ctx.fill()


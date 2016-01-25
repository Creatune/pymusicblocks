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

from gi.repository import Gtk

from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.graphics.toolbarbox import ToolButton
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ActivityToolbarButton


def make_separator(expand=False):
    sep = Gtk.SeparatorToolItem()
    sep.set_expand(expand)
    sep.props.draw = not expand
    return sep


class MBToolbarBox(ToolbarBox):

    def __init__(self, activity):
        ToolbarBox.__init__(self)

        self.toolbar.insert(ActivityToolbarButton(activity), -1)
        self.toolbar.insert(make_separator(expand=False), -1)

        self.button_fast = ToolButton("fast-button")
        self.toolbar.insert(self.button_fast, -1)

        self.button_slow = ToolButton("slow-button")
        self.toolbar.insert(self.button_slow, -1)

        self.button_step = ToolButton("step-button")
        self.toolbar.insert(self.button_step, -1)

        self.button_slow_music = ToolButton("slow-music-button")
        self.toolbar.insert(self.button_slow_music, -1)

        self.button_step_music = ToolButton("step-music-button")
        self.toolbar.insert(self.button_step_music, -1)

        self.button_stop = ToolButton("stop-turtle-button")
        self.toolbar.insert(self.button_stop, -1)

        self.button_clear = ToolButton("clear-button")
        self.toolbar.insert(self.button_clear, -1)

        self.button_palette = ToolButton("palette-button")
        self.toolbar.insert(self.button_palette, -1)

        self.button_hide_blocks = ToolButton("hide-blocks-button")
        self.toolbar.insert(self.button_hide_blocks, -1)

        self.button_collapse_blocks = ToolButton("collapse-blocks-button")
        self.toolbar.insert(self.button_collapse_blocks, -1)

        self.button_help = ToolButton("help-button")
        self.toolbar.insert(self.button_help, -1)

        self.toolbar.insert(make_separator(expand=True), -1)

        self.button_menu = ToolButton("menu-button")
        self.toolbar.insert(self.button_menu, -1)

        self.toolbar.insert(make_separator(expand=False), -1)
        self.toolbar.insert(StopButton(activity), -1)

        self.show_all()
        self.toolbar.show_all()


# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2012 Sean Davis <smd.seandavis@gmail.com>
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License version 3, as published 
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along 
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

class MenulibreInitException(Exception):
    def __init__(self, section, details):
        self.section = section
        self.details = details
        
    def __str__(self):
        details_string = ""
        if len(self.details) > 1:
            for detail in self.details[1:]:
                details_string += detail + "\n"
        msg = """
MenuLibre failed to initialize...  Please report a bug with the following 
details at https://bugs.launchpad.net/menulibre

Section: %s
Exception: %s

Additional Details: %s""" % (self.section, self.details[0], details_string)
        return repr(msg)

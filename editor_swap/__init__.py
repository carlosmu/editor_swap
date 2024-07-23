# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from . import ui_keymap
from . import user_prefs
from . import ot_editor_swap
from . import draw_button

bl_info = {
    "name": "Editor Swap",
    "author": "carlosmu <carlos.damian.munoz@gmail.com>",
    "blender": (2, 83, 0),
    "version": (1, 3, 0), 
    "category": "User",
    "location": "Editors headers",
    "description": "Swap Editors by pressing shortcut or button.",
    "warning": "",
    "doc_url": "https://blendermarket.com/products/editor-swap/",
    "tracker_url": "https://blendermarket.com/creators/carlosmu",
}

### Changelog 1.3.0
# Fix error when area == None 
# Add support for 4.2 Extensions System
# Add custom icons

####################################
# REGISTER/UNREGISTER
####################################

def register():
    draw_button.register()
    ot_editor_swap.register()
    user_prefs.register()
    ui_keymap.register()


def unregister():
    draw_button.unregister()
    ot_editor_swap.unregister()
    user_prefs.unregister()
    ui_keymap.unregister()
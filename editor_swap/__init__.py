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

bl_info = {
    "name" : "Editor Swap",
    "author" : "carlosmu <carlos.damian.munoz@gmail.com>",    
    "blender" : (2, 83, 0),
    "version" : (0, 7, 0),
    "category" : "User",
    "location" : "Editors headers",
    "description" : "Swapping between paired editors.",
    "warning" : "",
    "doc_url" : "https://github.com/carlosmu/editor_swap",
    "tracker_url" : "https://github.com/carlosmu/editor_swap/issues",
}

import bpy

from . import draw_button
from . import ot_editor_swap
from . import user_prefs
# from . import keymap


addon_keymaps = []

####################################
# REGISTER/UNREGISTER
####################################
def register():
    draw_button.register()
    ot_editor_swap.register() 
    user_prefs.register() 
    # keymap.register() 

    # Keymap
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Window', space_type='EMPTY')
        kmi = km.keymap_items.new("area.editor_swap", type = 'E', value = 'PRESS', ctrl = True, alt = True)
        addon_keymaps.append((km, kmi))

    
        
def unregister():
    draw_button.unregister()
    ot_editor_swap.unregister() 
    user_prefs.unregister() 
    # keymap.unregister() 

    # Keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


"""
TO-DO
- Editors based on preferences properties = OK
- Custom icons based on properties = OK
- Resolve image editor 291
- Resolve geometry nodes 292 = OK
- Resolve asset browser 293 = OK

- Keymap cunfigurable by preferences (default CTRL ALT E)
- Restore Defaults button (or deactivate, activate)
- Add "None" option to editors selector


"""


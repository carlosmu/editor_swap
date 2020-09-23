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
    "name" : "fast_switcher",
    "author" : "carlosmu <carlos.damian.munoz@gmail.com>",    
    "blender" : (2, 83, 0),
    "version" : (0, 2, 1),
    "category" : "User",
    "location" : "Some editors headers",
    "description" : "Fast switching between some editors.",
    "warning" : "",
    "doc_url" : "https://github.com/carlosmu/fast_switcher",
    "tracker_url" : "",
}

import bpy

# Operator class
class FS_OT_fast_switcher(bpy.types.Operator):
    """Fast switch between outliner and properties editors"""
    bl_idname = "area.fast_switcher"
    bl_label = "Fast Switcher"
    
    # It prevents the operator from appearing in other editors.
    @classmethod
    def poll(cls, context):
        if context.area.ui_type == 'OUTLINER':
            return True
        elif context.area.ui_type == 'DOPESHEET':
            return True
        elif context.area.ui_type == 'FCURVES':
            return True
        elif context.area.ui_type == 'PROPERTIES':
            return True
        else:
            return False
    
    # If the current editor is "X" assign "Y"...
    def execute(self, context):
        if (bpy.context.area.ui_type == 'OUTLINER'):
            bpy.context.area.ui_type = 'PROPERTIES'
        elif (bpy.context.area.ui_type == 'PROPERTIES'):
            bpy.context.area.ui_type = 'OUTLINER'
        elif (bpy.context.area.ui_type == 'DOPESHEET'):
            bpy.context.area.ui_type = 'FCURVES'
        else: 
            bpy.context.area.ui_type = 'DOPESHEET'
        return{'FINISHED'}

# Draw buttons
def draw_fast_switcher(self, context):
    # If not (context editor "Drivers" or "Timeline") draw buttons. 
    # Because this are children of DopeSheet and FCurves
    if not (bpy.context.area.ui_type == 'DRIVERS' or bpy.context.area.ui_type == 'TIMELINE'): 
        self.layout.operator("area.fast_switcher",text="", icon='WINDOW')

# Register/unregister the operator class and draw function
def register():
    bpy.utils.register_class(FS_OT_fast_switcher)
    bpy.types.OUTLINER_HT_header.prepend(draw_fast_switcher)
    bpy.types.PROPERTIES_HT_header.prepend(draw_fast_switcher)
    bpy.types.DOPESHEET_HT_header.prepend(draw_fast_switcher)
    bpy.types.GRAPH_HT_header.prepend(draw_fast_switcher)    
        
def unregister():
    bpy.utils.unregister_class(FS_OT_fast_switcher)
    bpy.types.OUTLINER_HT_header.remove(draw_fast_switcher)
    bpy.types.PROPERTIES_HT_header.remove(draw_fast_switcher)
    bpy.types.DOPESHEET_HT_header.remove(draw_fast_switcher)
    bpy.types.GRAPH_HT_header.remove(draw_fast_switcher)
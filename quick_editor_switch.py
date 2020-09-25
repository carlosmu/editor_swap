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

import bpy

bl_info = {
    "name" : "Quick Editor Switch",
    "author" : "carlosmu <carlos.damian.munoz@gmail.com>",    
    "blender" : (2, 83, 0),
    "version" : (0, 4, 3),
    "category" : "User",
    "location" : "Editors headers",
    "description" : "Quick switch between editors.",
    "warning" : "",
    "doc_url" : "https://github.com/carlosmu/quick_editor_switch",
    "tracker_url" : "",
}

# Operator class
class QES_OT_quick_editor_switch(bpy.types.Operator):
    """Quick switch between editors"""
    bl_idname = "area.quick_editor_switch"
    bl_label = "Quick Editor Switch"  
    
    # It prevents the operator from appearing in unsupported editors.
    @classmethod
    def poll(cls, context):
        if ((context.area.ui_type == 'VIEW_3D') 
        or (context.area.ui_type == 'PREFERENCES')
        or (context.area.ui_type == 'TextureNodeTree')
        or (context.area.ui_type == 'FILE_BROWSER')):
            return False
        else:
            return True
    
    # If the current editor is "X" assign "Y"...
    def execute(self, context):
        if (context.area.ui_type == 'OUTLINER'):
            context.area.ui_type = 'PROPERTIES'
        elif (context.area.ui_type == 'PROPERTIES'):
            context.area.ui_type = 'OUTLINER'
        elif (context.area.ui_type == 'DOPESHEET'):
            context.area.ui_type = 'FCURVES'
        elif (context.area.ui_type == 'TIMELINE'):
            context.area.ui_type = 'INFO'
        elif (context.area.ui_type == 'INFO'):
            context.area.ui_type = 'TIMELINE'
        # Fixing inconsistent Image_Editor names between versions
        elif (context.area.ui_type == 'UV'):
            if bpy.app.version >= (2, 91, 0):
                context.area.ui_type = 'IMAGE_EDITOR'
            else: 
                context.area.ui_type = 'VIEW'
                # End of fix
        elif (context.area.ui_type == 'VIEW'): 
            context.area.ui_type = 'UV'
        elif (context.area.ui_type == 'IMAGE_EDITOR'): 
            context.area.ui_type = 'UV'
        elif (context.area.ui_type == 'TEXT_EDITOR'):
            context.area.ui_type = 'CONSOLE'
        elif (context.area.ui_type == 'CONSOLE'):
            context.area.ui_type = 'TEXT_EDITOR'
        elif (context.area.ui_type == 'CompositorNodeTree'):
            context.area.ui_type = 'ShaderNodeTree'
        elif (context.area.ui_type == 'ShaderNodeTree'):
            context.area.ui_type = 'CompositorNodeTree'
        elif (context.area.ui_type == 'DRIVERS'):
            context.area.ui_type = 'NLA_EDITOR'
        elif (context.area.ui_type == 'NLA_EDITOR'):
            context.area.ui_type = 'DRIVERS'
        elif (context.area.ui_type == 'SEQUENCE_EDITOR'):
            context.area.ui_type = 'CLIP_EDITOR'
        elif (context.area.ui_type == 'CLIP_EDITOR'):
            context.area.ui_type = 'SEQUENCE_EDITOR'
        else: 
            context.area.ui_type = 'DOPESHEET'
        return{'FINISHED'}

# Draw buttons
def draw_quick_editor_switch(self, context):
    # If not context editor "Drivers" draw buttons (because this is children of FCurves). 
    if not (context.area.ui_type == 'TextureNodeTree'): 
        self.layout.operator("area.quick_editor_switch",text="", icon='WINDOW')

# Register/unregister the operator class and draw function
# To-Do: Give more elegance to this code.
def register():
    bpy.utils.register_class(QES_OT_quick_editor_switch)
    bpy.types.OUTLINER_HT_header.prepend(draw_quick_editor_switch)
    bpy.types.PROPERTIES_HT_header.prepend(draw_quick_editor_switch)
    bpy.types.DOPESHEET_HT_header.prepend(draw_quick_editor_switch)
    bpy.types.GRAPH_HT_header.prepend(draw_quick_editor_switch)    
    bpy.types.INFO_HT_header.prepend(draw_quick_editor_switch)    
    bpy.types.IMAGE_HT_header.prepend(draw_quick_editor_switch)    
    bpy.types.TEXT_HT_header.prepend(draw_quick_editor_switch)    
    bpy.types.CONSOLE_HT_header.prepend(draw_quick_editor_switch)    
    bpy.types.NODE_HT_header.prepend(draw_quick_editor_switch)    
    bpy.types.NLA_HT_header.prepend(draw_quick_editor_switch)    
    bpy.types.SEQUENCER_HT_header.prepend(draw_quick_editor_switch)    
    bpy.types.CLIP_HT_header.prepend(draw_quick_editor_switch)    
        
def unregister():
    bpy.utils.unregister_class(QES_OT_quick_editor_switch)
    bpy.types.OUTLINER_HT_header.remove(draw_quick_editor_switch)
    bpy.types.PROPERTIES_HT_header.remove(draw_quick_editor_switch)
    bpy.types.DOPESHEET_HT_header.remove(draw_quick_editor_switch)
    bpy.types.GRAPH_HT_header.remove(draw_quick_editor_switch)
    bpy.types.INFO_HT_header.remove(draw_quick_editor_switch)
    bpy.types.IMAGE_HT_header.remove(draw_quick_editor_switch)
    bpy.types.TEXT_HT_header.remove(draw_quick_editor_switch)
    bpy.types.CONSOLE_HT_header.remove(draw_quick_editor_switch)
    bpy.types.NODE_HT_header.remove(draw_quick_editor_switch)
    bpy.types.NLA_HT_header.remove(draw_quick_editor_switch)
    bpy.types.SEQUENCER_HT_header.remove(draw_quick_editor_switch)
    bpy.types.CLIP_HT_header.remove(draw_quick_editor_switch)
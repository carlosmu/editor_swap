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
    "name" : "Editor Swap",
    "author" : "carlosmu <carlos.damian.munoz@gmail.com>",    
    "blender" : (2, 83, 0),
    "version" : (0, 6, 0),
    "category" : "User",
    "location" : "Editors headers",
    "description" : "Swapping between paired editors.",
    "warning" : "",
    "doc_url" : "https://github.com/carlosmu/editor_swap",
    "tracker_url" : "https://github.com/carlosmu/editor_swap/issues",
}

####################################
# USER PREFS
####################################

####################################
# MAIN OPERATOR
####################################
class ES_OT_editor_swap(bpy.types.Operator):
    """Quick switch between editors"""
    bl_idname = "area.editor_swap"
    bl_label = "Editor Swap"  
    
    # It prevents the operator from appearing in unsupported editors.
    @classmethod
    def poll(cls, context):
        if not (context.area.ui_type == 'TextureNodeTree'
        or context.area.ui_type == 'FILE_BROWSER'):
            return True
    
    # If the current editor is "X" assign "Y"...
    def execute(self, context):
        if context.area.ui_type == 'OUTLINER':
            context.area.ui_type = 'PROPERTIES'
        elif context.area.ui_type == 'PROPERTIES':
            context.area.ui_type = 'OUTLINER'
        elif context.area.ui_type == 'DOPESHEET':
            context.area.ui_type = 'FCURVES'
        elif context.area.ui_type == 'TIMELINE':
            context.area.ui_type = 'INFO'
        elif context.area.ui_type == 'INFO':
            context.area.ui_type = 'TIMELINE'
        # Fixing inconsistent Image_Editor names between versions
        elif context.area.ui_type == 'UV':
            if bpy.app.version >= (2, 91, 0):
                context.area.ui_type = 'IMAGE_EDITOR'
            else: 
                context.area.ui_type = 'VIEW'
                # End of fix
        elif context.area.ui_type == 'VIEW':
            context.area.ui_type = 'UV'
        elif context.area.ui_type == 'IMAGE_EDITOR':
            context.area.ui_type = 'UV'
        elif context.area.ui_type == 'TEXT_EDITOR':
            context.area.ui_type = 'CONSOLE'
        elif context.area.ui_type == 'CONSOLE':
            context.area.ui_type = 'TEXT_EDITOR'
        elif context.area.ui_type == 'CompositorNodeTree':
            context.area.ui_type = 'ShaderNodeTree'
        elif context.area.ui_type == 'ShaderNodeTree':
            context.area.ui_type = 'CompositorNodeTree'
        elif context.area.ui_type == 'DRIVERS':
            context.area.ui_type = 'NLA_EDITOR'
        elif context.area.ui_type == 'NLA_EDITOR':
            context.area.ui_type = 'DRIVERS'
        elif context.area.ui_type == 'SEQUENCE_EDITOR':
            context.area.ui_type = 'CLIP_EDITOR'
        elif context.area.ui_type == 'CLIP_EDITOR':
            context.area.ui_type = 'SEQUENCE_EDITOR'
        elif context.area.ui_type == 'PREFERENCES':
            context.area.ui_type = 'VIEW_3D'
        elif context.area.ui_type == 'VIEW_3D':
            context.area.ui_type = 'PREFERENCES'
        else: 
            context.area.ui_type = 'DOPESHEET'
        return{'FINISHED'}

####################################
# DRAW BUTTONS
####################################
def draw_editor_swap(self, context):
    # If not "TextureNodeTree" draw buttons (because shares space with shaders and compositor). 
    if not context.area.ui_type == 'TextureNodeTree': 
        self.layout.operator("area.editor_swap",text="", icon='WINDOW')


####################################
# REGISTER/UNREGISTER
####################################
def register():
    bpy.utils.register_class(ES_OT_editor_swap)
    bpy.types.OUTLINER_HT_header.prepend(draw_editor_swap)
    bpy.types.PROPERTIES_HT_header.prepend(draw_editor_swap)
    bpy.types.DOPESHEET_HT_header.prepend(draw_editor_swap)
    bpy.types.GRAPH_HT_header.prepend(draw_editor_swap)    
    bpy.types.INFO_HT_header.prepend(draw_editor_swap)    
    bpy.types.IMAGE_HT_header.prepend(draw_editor_swap)    
    bpy.types.TEXT_HT_header.prepend(draw_editor_swap)    
    bpy.types.CONSOLE_HT_header.prepend(draw_editor_swap)    
    bpy.types.NODE_HT_header.prepend(draw_editor_swap)    
    bpy.types.NLA_HT_header.prepend(draw_editor_swap)    
    bpy.types.SEQUENCER_HT_header.prepend(draw_editor_swap)    
    bpy.types.CLIP_HT_header.prepend(draw_editor_swap)    
    bpy.types.VIEW3D_HT_header.prepend(draw_editor_swap)    
    bpy.types.USERPREF_HT_header.prepend(draw_editor_swap)    
        
def unregister():
    bpy.utils.unregister_class(ES_OT_editor_swap)
    bpy.types.OUTLINER_HT_header.remove(draw_editor_swap)
    bpy.types.PROPERTIES_HT_header.remove(draw_editor_swap)
    bpy.types.DOPESHEET_HT_header.remove(draw_editor_swap)
    bpy.types.GRAPH_HT_header.remove(draw_editor_swap)
    bpy.types.INFO_HT_header.remove(draw_editor_swap)
    bpy.types.IMAGE_HT_header.remove(draw_editor_swap)
    bpy.types.TEXT_HT_header.remove(draw_editor_swap)
    bpy.types.CONSOLE_HT_header.remove(draw_editor_swap)
    bpy.types.NODE_HT_header.remove(draw_editor_swap)
    bpy.types.NLA_HT_header.remove(draw_editor_swap)
    bpy.types.SEQUENCER_HT_header.remove(draw_editor_swap)
    bpy.types.CLIP_HT_header.remove(draw_editor_swap)
    bpy.types.VIEW3D_HT_header.remove(draw_editor_swap)
    bpy.types.USERPREF_HT_header.remove(draw_editor_swap)
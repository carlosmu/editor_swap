####################################
# MAIN OPERATOR
####################################

import bpy
# from bpy.types import Panel, PropertyGroup, WindowManager
# from bpy.utils import register_class, unregister_class

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
            context.area.ui_type = bpy.context.preferences.addons[__package__].preferences.view_3d,
        else: 
            context.area.ui_type = 'DOPESHEET'
        return{'FINISHED'}

####################################
# REGISTER/UNREGISTER
####################################
def register():
    bpy.utils.register_class(ES_OT_editor_swap) 
        
def unregister():
    bpy.utils.unregister_class(ES_OT_editor_swap)
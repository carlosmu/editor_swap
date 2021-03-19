####################################
# MAIN OPERATOR
####################################

import bpy

class ES_OT_editor_swap(bpy.types.Operator):
    """Quick switch between editors"""
    bl_idname = "area.editor_swap"
    bl_label = "Editor Swap"  

    # If the current editor is "X" assign "Y"...
    def execute(self, context):
        # Cast properties from user_prefs
        es_view_3d = context.preferences.addons[__package__].preferences.es_view_3d
        
        if bpy.app.version >= (2, 91, 0):
            es_image_editor = context.preferences.addons[__package__].preferences.es_image_editor
        else:
            es_view = context.preferences.addons[__package__].preferences.es_view
        
        es_uv = context.preferences.addons[__package__].preferences.es_uv
        es_compositor = context.preferences.addons[__package__].preferences.es_compositor
        es_texture_node = context.preferences.addons[__package__].preferences.es_texture_node
        
        if bpy.app.version >= (2, 92, 0):
            es_geometry_node = context.preferences.addons[__package__].preferences.es_geometry_node
        
        es_shader_editor = context.preferences.addons[__package__].preferences.es_shader_editor
        es_sequence_editor = context.preferences.addons[__package__].preferences.es_sequence_editor
        es_clip_editor = context.preferences.addons[__package__].preferences.es_clip_editor
        es_dopesheet = context.preferences.addons[__package__].preferences.es_dopesheet
        es_timeline = context.preferences.addons[__package__].preferences.es_timeline
        es_fcurves = context.preferences.addons[__package__].preferences.es_fcurves
        es_drivers = context.preferences.addons[__package__].preferences.es_drivers
        es_nla_editor = context.preferences.addons[__package__].preferences.es_nla_editor
        es_text_editor = context.preferences.addons[__package__].preferences.es_text_editor
        es_console = context.preferences.addons[__package__].preferences.es_console
        es_info = context.preferences.addons[__package__].preferences.es_info
        es_outliner = context.preferences.addons[__package__].preferences.es_outliner
        es_properties = context.preferences.addons[__package__].preferences.es_properties
        es_files = context.preferences.addons[__package__].preferences.es_files
        
        if bpy.app.version >= (2, 93, 0):
            es_assets = context.preferences.addons[__package__].preferences.es_assets
        es_preferences = context.preferences.addons[__package__].preferences.es_preferences
        
        # Cast the editors
        if context.area.ui_type == 'VIEW_3D':
            context.area.ui_type = es_view_3d
        elif context.area.ui_type == 'IMAGE_EDITOR':
            context.area.ui_type = es_image_editor
        elif context.area.ui_type == 'VIEW':
            context.area.ui_type = es_view
        elif context.area.ui_type == 'UV':
            context.area.ui_type = es_uv
        elif context.area.ui_type == 'CompositorNodeTree': 
            context.area.ui_type = es_compositor
        elif context.area.ui_type == 'TextureNodeTree':
            context.area.ui_type = es_texture_node
        elif context.area.ui_type == 'GeometryNodeTree':
            context.area.ui_type = es_geometry_node
        elif context.area.ui_type == 'ShaderNodeTree':
            context.area.ui_type = es_shader_editor
        elif context.area.ui_type == 'SEQUENCE_EDITOR':
            context.area.ui_type = es_sequence_editor
        elif context.area.ui_type == 'CLIP_EDITOR':
            context.area.ui_type = es_clip_editor
        elif context.area.ui_type == 'DOPESHEET':
            context.area.ui_type = es_dopesheet
        elif context.area.ui_type == 'TIMELINE':
            context.area.ui_type = es_timeline
        elif context.area.ui_type == 'FCURVES':
            context.area.ui_type = es_fcurves
        elif context.area.ui_type == 'DRIVERS':
            context.area.ui_type = es_drivers
        elif context.area.ui_type == 'NLA_EDITOR':
            context.area.ui_type = es_nla_editor
        elif context.area.ui_type == 'TEXT_EDITOR':
            context.area.ui_type = es_text_editor
        elif context.area.ui_type == 'CONSOLE':
            context.area.ui_type = es_console
        elif context.area.ui_type == 'INFO':
            context.area.ui_type = es_info
        elif context.area.ui_type == 'OUTLINER':
            context.area.ui_type = es_outliner
        elif context.area.ui_type == 'PROPERTIES':
            context.area.ui_type = es_properties
        elif context.area.ui_type == 'FILES':
            context.area.ui_type =  es_files
        elif context.area.ui_type == 'ASSETS':
            context.area.ui_type = es_assets
        elif context.area.ui_type == 'PREFERENCES':
            context.area.ui_type = es_preferences
        else: 
            pass
        return{'FINISHED'}

####################################
# REGISTER/UNREGISTER
####################################
def register():
    bpy.utils.register_class(ES_OT_editor_swap) 
        
def unregister():
    bpy.utils.unregister_class(ES_OT_editor_swap)
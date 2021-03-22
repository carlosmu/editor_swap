####################################
# DRAW BUTTONS
####################################

import bpy


def draw_editor_swap(self, context):
    es_enable_buttons = context.preferences.addons[__package__].preferences.es_enable_buttons 
    es_custom_icon = context.preferences.addons[__package__].preferences.es_custom_icon 
   
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

    if es_enable_buttons:
        if context.area.ui_type == 'VIEW_3D' and context.area.ui_type == es_view_3d:
            return
        if context.area.ui_type == 'IMAGE_EDITOR' and context.area.ui_type == es_image_editor:
            return
        if context.area.ui_type == 'VIEW' and context.area.ui_type == es_view:
            return
        if context.area.ui_type == 'UV' and context.area.ui_type == es_uv:
            return
        if context.area.ui_type == 'CompositorNodeTree' and context.area.ui_type == es_compositor:
            return
        if context.area.ui_type == 'TextureNodeTree' and context.area.ui_type == es_texture_node:
            return
        if context.area.ui_type == 'TextureChannelMixing' and context.area.ui_type == es_texture_node:
            return
        if context.area.ui_type == 'GeometryNodeTree' and context.area.ui_type == es_geometry_node:
            return
        if context.area.ui_type == 'ShaderNodeTree' and context.area.ui_type == es_shader_editor:
            return
        if context.area.ui_type == 'SEQUENCE_EDITOR' and context.area.ui_type == es_sequence_editor:
            return
        if context.area.ui_type == 'CLIP_EDITOR' and context.area.ui_type == es_clip_editor:
            return
        if context.area.ui_type == 'DOPESHEET' and context.area.ui_type == es_dopesheet:
            return
        if context.area.ui_type == 'TIMELINE' and context.area.ui_type == es_timeline:
            return
        if context.area.ui_type == 'FCURVES' and context.area.ui_type == es_fcurves:
            return
        if context.area.ui_type == 'DRIVERS' and context.area.ui_type == es_drivers:
            return
        if context.area.ui_type == 'NLA_EDITOR' and context.area.ui_type == es_nla_editor:
            return
        if context.area.ui_type == 'TEXT_EDITOR' and context.area.ui_type == es_text_editor:
            return
        if context.area.ui_type == 'CONSOLE' and context.area.ui_type == es_console:
            return
        if context.area.ui_type == 'INFO' and context.area.ui_type == es_info:
            return
        if context.area.ui_type == 'OUTLINER' and context.area.ui_type == es_outliner:
            return
        if context.area.ui_type == 'PROPERTIES' and context.area.ui_type == es_properties:
            return
        if context.area.ui_type == 'FILES' and context.area.ui_type == es_files:
            return
        if context.area.ui_type == 'FILE_BROWSER' and context.area.ui_type == es_files:
            return
        if context.area.ui_type == 'ASSETS' and context.area.ui_type == es_assets:
            return
        if context.area.ui_type == 'PREFERENCES' and context.area.ui_type == es_preferences:
            return        
        else:
            self.layout.operator("area.editor_swap",text="", icon=es_custom_icon)
            

####################################
# REGISTER/UNREGISTER
####################################
def register():
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
    bpy.types.FILEBROWSER_HT_header.prepend(draw_editor_swap)    
        
def unregister():
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
    bpy.types.FILEBROWSER_HT_header.remove(draw_editor_swap)
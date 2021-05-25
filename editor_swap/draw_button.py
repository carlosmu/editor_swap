####################################
# DRAW BUTTONS
####################################

import bpy

def draw_editor_swap(self, context):
    
    # Variable for cast properties from preferences
    es_props = context.preferences.addons[__package__].preferences

    # Cast options from user_prefs
    es_enable_buttons = es_props.es_enable_buttons 
    es_custom_icon = es_props.es_custom_icon 
   
    # Cast editors props from user_prefs
    es_view_3d = es_props.es_view_3d
    es_uv = es_props.es_uv
    es_compositor = es_props.es_compositor
    es_texture_node = es_props.es_texture_node
    es_shader_editor = es_props.es_shader_editor
    es_sequence_editor = es_props.es_sequence_editor
    es_clip_editor = es_props.es_clip_editor
    es_dopesheet = es_props.es_dopesheet
    es_timeline = es_props.es_timeline
    es_fcurves = es_props.es_fcurves
    es_drivers = es_props.es_drivers
    es_nla_editor = es_props.es_nla_editor
    es_text_editor = es_props.es_text_editor
    es_console = es_props.es_console
    es_info = es_props.es_info
    es_outliner = es_props.es_outliner
    es_properties = es_props.es_properties
    es_files = es_props.es_files
    es_preferences = es_props.es_preferences
    es_image_editor = es_props.es_image_editor
    
    # Add Geometry Nodes for 2.92 and above
    if bpy.app.version >= (2, 92, 0):
        es_geometry_node = es_props.es_geometry_node  

    # Add Spreadsheet for 2.93 and above
    if bpy.app.version >= (2, 93, 0):
        es_spreadsheet = es_props.es_spreadsheet 
    
    # Uncomment this snippet to enable the asset browser 
    # if bpy.app.version >= (3, 0, 0):
    #     es_assets = es_props.es_assets


    ####################################
    # SHOW AND HIDE BUTTONS 
    ####################################
    ui_type = context.area.ui_type

    if es_enable_buttons:
        if ui_type == 'VIEW_3D' and ui_type == es_view_3d:
            return
        if ui_type == 'IMAGE_EDITOR' and ui_type == es_image_editor:
            return
        if ui_type == 'VIEW' and ui_type == es_image_editor:
            return
        if ui_type == 'UV' and ui_type == es_uv:
            return
        if ui_type == 'CompositorNodeTree' and ui_type == es_compositor:
            return
        if ui_type == 'TextureNodeTree' and ui_type == es_texture_node:
            return
        if ui_type == 'TextureChannelMixing' and ui_type == es_texture_node:
            return
        if ui_type == 'GeometryNodeTree' and ui_type == es_geometry_node:
            return
        if ui_type == 'ShaderNodeTree' and ui_type == es_shader_editor:
            return
        if ui_type == 'SEQUENCE_EDITOR' and ui_type == es_sequence_editor:
            return
        if ui_type == 'CLIP_EDITOR' and ui_type == es_clip_editor:
            return
        if ui_type == 'DOPESHEET' and ui_type == es_dopesheet:
            return
        if ui_type == 'TIMELINE' and ui_type == es_timeline:
            return
        if ui_type == 'FCURVES' and ui_type == es_fcurves:
            return
        if ui_type == 'DRIVERS' and ui_type == es_drivers:
            return
        if ui_type == 'NLA_EDITOR' and ui_type == es_nla_editor:
            return
        if ui_type == 'TEXT_EDITOR' and ui_type == es_text_editor:
            return
        if ui_type == 'CONSOLE' and ui_type == es_console:
            return
        if ui_type == 'INFO' and ui_type == es_info:
            return
        if ui_type == 'OUTLINER' and ui_type == es_outliner:
            return
        if ui_type == 'PROPERTIES' and ui_type == es_properties:
            return
        if ui_type == 'FILES' and ui_type == es_files:
            return
        if ui_type == 'FILE_BROWSER' and ui_type == es_files:
            return
        if ui_type == 'ASSETS' and ui_type == es_assets:
            return
        if ui_type == 'SPREADSHEET' and ui_type == es_spreadsheet:
            return
        if ui_type == 'PREFERENCES' and ui_type == es_preferences:
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
    if bpy.app.version >= (2, 93, 0):
        bpy.types.SPREADSHEET_HT_header.prepend(draw_editor_swap)    
        
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
    if bpy.app.version >= (2, 93, 0):
        bpy.types.SPREADSHEET_HT_header.remove(draw_editor_swap)
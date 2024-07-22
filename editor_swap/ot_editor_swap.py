####################################
# MAIN OPERATOR
####################################

import bpy

class ES_OT_editor_swap(bpy.types.Operator):
    """Quick swap between editors"""
    bl_idname = "area.editor_swap"
    bl_label = "Editor Swap"  
    bl_options = {'REGISTER'}

    # If the current editor is "X" assign "Y"...
    def execute(self, context):

        if context.area is None:
            self.report({'ERROR'}, "No active area found. Please put the cursor inside an area/editor")
            return {'CANCELLED'}
        
        global addon_icons
        
        # Cast Properties from preferences
        es_props = context.preferences.addons[__package__].preferences
    
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
        
        # Add Spreadsheet for 2.92 and above
        if bpy.app.version >= (2, 93, 0):
            es_spreadsheet = es_props.es_spreadsheet

        # Add Asset Browser for 3.0 and above  
        if bpy.app.version >= (3, 0, 0):
            es_assets = es_props.es_assets
        
        # Cast the editors
        ui_type = context.area.ui_type

        if ui_type == 'VIEW_3D':
            context.area.ui_type = es_view_3d
        elif ui_type == 'IMAGE_EDITOR' or ui_type == 'VIEW':
            context.area.ui_type = es_image_editor
        elif ui_type == 'UV':
            context.area.ui_type = es_uv
        elif ui_type == 'CompositorNodeTree': 
            context.area.ui_type = es_compositor
        elif ui_type == 'TextureNodeTree' or ui_type == 'TextureChannelMixing':
            context.area.ui_type = es_texture_node
        elif ui_type == 'GeometryNodeTree':
            context.area.ui_type = es_geometry_node
        elif ui_type == 'ShaderNodeTree':
            context.area.ui_type = es_shader_editor
        elif ui_type == 'SEQUENCE_EDITOR':
            context.area.ui_type = es_sequence_editor
        elif ui_type == 'CLIP_EDITOR':
            context.area.ui_type = es_clip_editor
        elif ui_type == 'DOPESHEET':
            context.area.ui_type = es_dopesheet
        elif ui_type == 'TIMELINE':
            context.area.ui_type = es_timeline
        elif ui_type == 'FCURVES':
            context.area.ui_type = es_fcurves
        elif ui_type == 'DRIVERS':
            context.area.ui_type = es_drivers
        elif ui_type == 'NLA_EDITOR':
            context.area.ui_type = es_nla_editor
        elif ui_type == 'TEXT_EDITOR':
            context.area.ui_type = es_text_editor
        elif ui_type == 'CONSOLE':
            context.area.ui_type = es_console
        elif ui_type == 'INFO':
            context.area.ui_type = es_info
        elif ui_type == 'OUTLINER':
            context.area.ui_type = es_outliner
        elif ui_type == 'PROPERTIES':
            context.area.ui_type = es_properties
        elif ui_type == 'FILES':
            context.area.ui_type =  es_files
        elif ui_type == 'FILE_BROWSER':
            context.area.ui_type =  es_files
        elif ui_type == 'ASSETS':
            context.area.ui_type = es_assets
        elif ui_type == 'SPREADSHEET':
            context.area.ui_type = es_spreadsheet
        elif ui_type == 'PREFERENCES':
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
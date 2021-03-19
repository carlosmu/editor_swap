##############################################
#    USER PREFERENCES 
##############################################

import bpy 

class ES_UserPrefs(bpy.types.AddonPreferences):
    bl_idname = __package__

    enable_keymap : bpy.props.BoolProperty(
        name="Enable Keymap",
        description="Enable or Disable Addon Keymap", 
        default=True
        )
    enable_buttons : bpy.props.BoolProperty(
        name="Enable Buttons on Headers",
        description="Enable or Disable Buttons on Headers", 
        default=True
        )

    my_icons = (
            ('WINDOW', 'Window', ''),
            ('ARROW_LEFTRIGHT', 'Arrows Left-Right', ''),
            ('UV_SYNC_SELECT', 'Arrows Diagonal', ''),
            ('FILE_REFRESH', 'Refresh', ''),
            ('FORCE_VORTEX', 'Force Vortex', ''),
            ('SHADERFX', 'FX', ''),
    )

    es_custom_icon : bpy.props.EnumProperty(
        name = "Custom Icon",
        description= "Choose an custom icon",
        items = my_icons,
        default= 'WINDOW'
    )

    editors = (
            ('VIEW_3D', '3D Viewport', ''),
            ('IMAGE_EDITOR', 'Image Editor', '')
            if bpy.app.version >= (2, 91, 0) else
            ('VIEW', 'Old Image Editor', ''),
            ('UV', 'UV Editor', ''),
            ('CompositorNodeTree', 'Compositor', ''),
            ('TextureNodeTree', 'Texture Node Editor', ''),
            ('GeometryNodeTree', 'Geometry Node Editor', ''),
            ('ShaderNodeTree', 'Shader Editor', ''),
            ('SEQUENCE_EDITOR', 'Video Sequencer', ''),
            ('CLIP_EDITOR', 'Movie Clip Editor', ''),
            ('DOPESHEET', 'Dope Sheet', ''),
            ('TIMELINE', 'Timeline', ''),
            ('FCURVES', 'Graph Editor', ''),
            ('DRIVERS', 'Drivers', ''),
            ('NLA_EDITOR', 'Nonlinear Animation', ''),
            ('TEXT_EDITOR', 'Text Editor', ''),
            ('CONSOLE', 'Python Console', ''),
            ('INFO', 'Info', ''),
            ('OUTLINER', 'Outliner', ''),
            ('PROPERTIES', 'Properties', ''),
            ('FILES', 'File Browser', ''),
            ('ASSETS', 'Asset Browser', ''),
            ('PREFERENCES', 'Preferences', '')
    )

    es_view_3d : bpy.props.EnumProperty(
        name = "3D Viewport",
        description= "",
        items = editors,
        default='ShaderNodeTree',
    )
    es_image_editor : bpy.props.EnumProperty(
        name = "Image Editor",
        description= "",
        items = editors,
        default='UV',
    )
    es_uv : bpy.props.EnumProperty(
        name = "UV Editor",
        description= "",
        items = editors,
        default='IMAGE_EDITOR',
    )
    es_compositor : bpy.props.EnumProperty(
        name = "Compositor",
        description= "",
        items = editors,
        default='CompositorNodeTree',
    )
    es_texture_node : bpy.props.EnumProperty(
        name = "Texture Node Editor",
        description= "",
        items = editors,
        default='TextureNodeTree',
    )
    es_geometry_node : bpy.props.EnumProperty(
        name = "Geometry Node Editor",
        description= "",
        items = editors,
        default='GeometryNodeTree',
    )
    es_shader_editor : bpy.props.EnumProperty(
        name = "Shader Editor",
        description= "",
        items = editors,
        default='VIEW_3D',
    )
    es_sequence_editor : bpy.props.EnumProperty(
        name = "Video Sequencer",
        description= "",
        items = editors,
        default='CLIP_EDITOR',
    )
    es_clip_editor : bpy.props.EnumProperty(
        name = "Movie Clip Editor",
        description= "",
        items = editors,
        default='SEQUENCE_EDITOR',
    )
    es_dopesheet : bpy.props.EnumProperty(
        name = "Dope Sheet",
        description= "",
        items = editors,
        default='FCURVES',
    )
    es_timeline : bpy.props.EnumProperty(
        name = "Timeline",
        description= "",
        items = editors,
        default='INFO',
    )
    es_fcurves : bpy.props.EnumProperty(
        name = "Graph Editor",
        description= "",
        items = editors,
        default='DOPESHEET',
    )
    es_drivers : bpy.props.EnumProperty(
        name = "Drivers",
        description= "",
        items = editors,
        default='DRIVERS',
    )
    es_nla_editor : bpy.props.EnumProperty(
        name = "Nonlinear Animation",
        description= "",
        items = editors,
        default='NLA_EDITOR',
    )
    es_text_editor : bpy.props.EnumProperty(
        name = "Text Editor",
        description= "",
        items = editors,
        default='CONSOLE',
    )
    es_console : bpy.props.EnumProperty(
        name = "Python Console",
        description= "",
        items = editors,
        default='TEXT_EDITOR',
    )
    es_info : bpy.props.EnumProperty(
        name = "Info",
        description= "",
        items = editors,
        default='TIMELINE',
    )
    es_outliner : bpy.props.EnumProperty(
        name = "Outliner",
        description= "",
        items = editors,
        default='PROPERTIES',
    )
    es_properties : bpy.props.EnumProperty(
        name = "Properties",
        description= "",
        items = editors,
        default='OUTLINER',
    )
    es_files : bpy.props.EnumProperty(
        name = "File Browser",
        description= "",
        items = editors,
        default='ASSETS',
    )
    es_assets : bpy.props.EnumProperty(
        name = "Asset Browser",
        description= "",
        items = editors,
        default='FILES',
    )
    es_preferences : bpy.props.EnumProperty(
        name = "Preferences",
        description= "",
        items = editors,
        default='PREFERENCES',
    )
    
    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = True
        layout.prop(self, "enable_keymap")
        # https://github.com/pitiwazou/Scripts-Blender/blob/Older-Scripts/addon_keymap_template
        layout.prop(self, "enable_buttons")
        if context.preferences.addons[__package__].preferences.enable_buttons:
            layout.prop(self, "es_custom_icon", icon = context.preferences.addons[__package__].preferences.es_custom_icon)
        box = layout.box()
        box.separator()
        box.label(text="   Choose the pairing editors")
        box.separator()
        box.prop(self, "es_view_3d", text="3D Viewport")
        box.prop(self, "es_image_editor", text="Image Editor")
        box.prop(self, "es_uv", text="UV Editor")
        box.prop(self, "es_compositor", text="Compositor")
        box.prop(self, "es_texture_node", text="Texture Node Editor")
        box.prop(self, "es_geometry_node", text="Geometry Node Editor")
        box.prop(self, "es_shader_editor", text="Shader Editor")
        box.prop(self, "es_sequence_editor", text="Video Sequencer")
        box.prop(self, "es_clip_editor", text="Movie Clip Editor")
        box.prop(self, "es_dopesheet", text="Dope Sheet")
        box.prop(self, "es_timeline", text="Timeline")
        box.prop(self, "es_fcurves", text="Graph Editor")
        box.prop(self, "es_drivers", text="Drivers")
        box.prop(self, "es_nla_editor", text="Nonlinear Animation")
        box.prop(self, "es_text_editor", text="Text Editor")
        box.prop(self, "es_console", text="Python Console")
        box.prop(self, "es_info", text="Info")
        box.prop(self, "es_outliner", text="Outliner")
        box.prop(self, "es_properties", text="Properties")
        box.prop(self, "es_files", text="File Browser")
        box.prop(self, "es_assets", text="Asset Browser")
        box.prop(self, "es_preferences", text="Preferences")
        box.separator()

####################################
# REGISTER/UNREGISTER
####################################
def register():
    bpy.utils.register_class(ES_UserPrefs) 
        
def unregister():
    bpy.utils.unregister_class(ES_UserPrefs)
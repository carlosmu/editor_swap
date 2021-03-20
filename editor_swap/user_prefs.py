##############################################
#    USER PREFERENCES 
##############################################

import bpy 

class ES_UserPrefs(bpy.types.AddonPreferences):
    bl_idname = __package__

    enable_buttons : bpy.props.BoolProperty(
        name="Enable Buttons on Headers",
        description="Enable or Disable Buttons on Headers", 
        default=True
        )

    my_icons = (
            ('WINDOW', 'Window', ''),
            ('ARROW_LEFTRIGHT', 'Arrows Left-Right', ''),
            ('FILE_REFRESH', 'Refresh', ''),
            ('FORCE_VORTEX', 'Force Vortex', ''),
            ('SHADERFX', 'FX', ''),
    )

    es_custom_icon : bpy.props.EnumProperty(
        name = "Custom Icon for Swap Buttons",
        description= "Choose an custom icon",
        items = my_icons,
        default= 'WINDOW'
    )

    image_editor = ('IMAGE_EDITOR', 'Image Editor', '') if bpy.app.version >= (2, 91, 0) else ('VIEW', 'Image Editor', '')
    texture_editor = ('TextureNodeTree', 'Texture Node Editor', '') if bpy.app.version >= (2, 90, 0) else ('TextureChannelMixing', 'Texture Node Editor', '')
    file_browser = ('FILES', 'File Browser', '') if bpy.app.version >= (2, 92, 0) else ('FILE_BROWSER', 'File Browser', '')

    editors = [
            ('VIEW_3D', '3D Viewport', ''),
            image_editor,
            ('UV', 'UV Editor', ''),
            ('CompositorNodeTree', 'Compositor', ''),
            texture_editor,            
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
            file_browser,
            ('PREFERENCES', 'Preferences', '')
    ]
    
    if bpy.app.version >= (2, 92, 0):
        editors.append(('GeometryNodeTree', 'Geometry Node Editor', ''),)

    if bpy.app.version >= (2, 93, 0):
        editors.append(('ASSETS', 'Asset Browser', ''))

    es_view_3d : bpy.props.EnumProperty(
        name = "3D Viewport",
        description= "",
        items = editors,
        default='ShaderNodeTree',
    )
    
    # If >= 291 image_editor else view
    if bpy.app.version >= (2, 91, 0):
        es_image_editor : bpy.props.EnumProperty(
            name = "Image Editor",
            description= "",
            items = editors,
            default='UV',
        )
    else:
        es_view : bpy.props.EnumProperty(
            name = "Image Editor",
            description= "",
            items = editors,
            default='UV',
        )
    es_uv : bpy.props.EnumProperty(
        name = "UV Editor",
        description= "",
        items = editors,
        default='IMAGE_EDITOR' if bpy.app.version >= (2, 91, 0) else 'VIEW',
    )
    es_compositor : bpy.props.EnumProperty(
        name = "Compositor",
        description= "",
        items = editors,
        default='CompositorNodeTree',
    )
    # Podría usar esto en lugar de lo que hice con el image editor y view
    es_texture_node : bpy.props.EnumProperty(
        name = "Texture Node Editor",
        description= "",
        items = editors,
        default='TextureNodeTree' if bpy.app.version >= (2, 90, 0) else 'TextureChannelMixing',
    )
    if bpy.app.version >= (2, 92, 0):
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

    if bpy.app.version >= (2, 93, 0):
        es_files_default = 'ASSETS'
    elif bpy.app.version == (2, 92, 0):
        es_files_default = 'FILES'
    else:
        es_files_default = 'FILE_BROWSER'

    es_files : bpy.props.EnumProperty(
        name = "File Browser",
        description= "",
        items = editors,
        default = es_files_default,
        # default='ASSETS' if bpy.app.version >= (2, 93, 0) else 'FILE_BROWSER',
    )    
    if bpy.app.version >= (2, 93, 0):
        es_assets : bpy.props.EnumProperty(
            name = "Asset Browser",
            description= "",
            items = editors,
            default='FILES' if bpy.app.version >= (2, 92, 0) else 'FILE_BROWSER',
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
        
        box = layout.box()
        box.label(text="Tooltip: The shortcut for swap between editors is CTRL + ALT + E", icon='INFO')
        # https://github.com/pitiwazou/Scripts-Blender/blob/Older-Scripts/addon_keymap_template
        
        layout.prop(self, "enable_buttons")
        if context.preferences.addons[__package__].preferences.enable_buttons:
            layout.prop(self, "es_custom_icon", icon = context.preferences.addons[__package__].preferences.es_custom_icon)
        
        box = layout.box()
        box.separator()
        box.label(text="Choose the pairing editors. For none select the same editor", icon='WINDOW')
        box.separator()

        box.prop(self, "es_view_3d", text="3D Viewport")

        if bpy.app.version >= (2, 91, 0):
            box.prop(self, "es_image_editor", text="Image Editor")
        else:
            box.prop(self, "es_image_editor", text="Image Editor")

        box.prop(self, "es_uv", text="UV Editor")
        box.prop(self, "es_compositor", text="Compositor")
        box.prop(self, "es_texture_node", text="Texture Node Editor")

        if bpy.app.version >= (2, 92, 0):
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

        if bpy.app.version >= (2, 93, 0):
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
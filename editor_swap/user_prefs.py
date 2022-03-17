##############################################
#    USER PREFERENCES 
##############################################

import bpy 
class ES_UserPrefs(bpy.types.AddonPreferences):
    bl_idname = __package__

    # Options
    es_enable_buttons : bpy.props.BoolProperty(
        name="Enable Swap Buttons on Headers",
        description="Enable or Disable Buttons on Headers", 
        default=True
    )
    es_enable_maximize : bpy.props.BoolProperty(
        name="Enable Maximize Button on Topbar",
        description="Enable or Disable Maximize Button on Topbar", 
        default=True
    )
    custom_icons = (
            ('WINDOW', 'Window', '', 'WINDOW', 0),
            ('ARROW_LEFTRIGHT', 'Arrows Left-Right', '', 'ARROW_LEFTRIGHT', 1),
            ('FILE_REFRESH', 'Refresh', '', 'FILE_REFRESH', 2),
            ('FORCE_VORTEX', 'Force Vortex', '', 'FORCE_VORTEX', 3),
            ('SHADERFX', 'FX', '', 'SHADERFX', 4),
    )
    es_custom_icon : bpy.props.EnumProperty(
        name = "Custom Icon for Swap Buttons",
        description= "Choose an custom icon",
        items = custom_icons,
        default= 'WINDOW'
    )

    # List Editors (in some cases the names do not match across the versions)
    image_editor = ('IMAGE_EDITOR', 'Image Editor', '', 'IMAGE', 1) if bpy.app.version >= (2, 91, 0) else ('VIEW', 'Image Editor', '', 'IMAGE', 1)
    texture_editor = ('TextureNodeTree', 'Texture Node Editor', '', 'NODE_TEXTURE', 4) if bpy.app.version >= (2, 90, 0) else ('TextureChannelMixing', 'Texture Node Editor', '', 'NODE_TEXTURE', 4)
    file_browser = ('FILES', 'File Browser', '', 'FILEBROWSER', 18) if bpy.app.version >= (2, 92, 0) else ('FILE_BROWSER', 'File Browser', '', 'FILEBROWSER', 18)

    editors = [
            ('VIEW_3D', '3D Viewport', '', 'VIEW3D', 0),
            image_editor,
            ('UV', 'UV Editor', '', 'UV', 2),
            ('CompositorNodeTree', 'Compositor', '', 'NODE_COMPOSITING', 3),
            texture_editor,            
            ('ShaderNodeTree', 'Shader Editor', '', 'SHADING_RENDERED', 5),
            ('SEQUENCE_EDITOR', 'Video Sequencer', '', 'SEQUENCE', 6),
            ('CLIP_EDITOR', 'Movie Clip Editor', '', 'TRACKER', 7),
            ('DOPESHEET', 'Dope Sheet', '', 'ACTION', 8),
            ('TIMELINE', 'Timeline', '', 'TIME', 9),
            ('FCURVES', 'Graph Editor', '', 'GRAPH', 10),
            ('DRIVERS', 'Drivers', '', 'DRIVER', 11),
            ('NLA_EDITOR', 'Nonlinear Animation', '', 'NLA', 12),
            ('TEXT_EDITOR', 'Text Editor', '', 'TEXT', 13),
            ('CONSOLE', 'Python Console', '', 'CONSOLE', 14),
            ('INFO', 'Info', '', 'INFO', 15),
            ('OUTLINER', 'Outliner', '', 'OUTLINER', 16),
            ('PROPERTIES', 'Properties', '', 'PROPERTIES', 17),
            file_browser,
            ('PREFERENCES', 'Preferences', '', 'PREFERENCES', 19)            
    ]
    
    # Append New Editors for 2.92 and 2.93
    if bpy.app.version >= (2, 92, 0):
        editors.append(('GeometryNodeTree', 'Geometry Node Editor', '', 'NODETREE', 20),)

    if bpy.app.version >= (2, 93, 0):
        editors.append(('SPREADSHEET', 'Spreadsheet', '', 'SPREADSHEET', 21))

    # Append Asset Browser for 3.0 and above 
    if bpy.app.version >= (3, 0, 0):
        editors.append(('ASSETS', 'Asset Browser', '', 'ASSET_MANAGER', 22))

    # Set the enums properties
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
        default='IMAGE_EDITOR' if bpy.app.version >= (2, 91, 0) else 'VIEW',
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
        default='TextureNodeTree' if bpy.app.version >= (2, 90, 0) else 'TextureChannelMixing',
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
    es_preferences : bpy.props.EnumProperty(
        name = "Preferences",
        description= "",
        items = editors,
        default='PREFERENCES',
    ) 

    # Set es_files_default
    if bpy.app.version >= (2, 92, 0):
        es_files_default = 'FILES'
    else:
        es_files_default = 'FILE_BROWSER'

    es_files : bpy.props.EnumProperty(
        name = "File Browser",
        description= "",
        items = editors,
        default = es_files_default,
    ) 

    # If >= 2.92, use geometry nodes
    if bpy.app.version >= (2, 92, 0):
        es_geometry_node : bpy.props.EnumProperty(
            name = "Geometry Node Editor",
            description= "",
            items = editors,
            default='GeometryNodeTree',
    )  
    # If >= 2.93, use spreadsheet
    if bpy.app.version >= (2, 93, 0):
        es_spreadsheet : bpy.props.EnumProperty(
            name = "Spreadsheet",
            description= "",
            items = editors,
            default='SPREADSHEET',
    )
    # If >= 3.0, use asset browser
    if bpy.app.version >= (3, 0, 0):
        es_assets : bpy.props.EnumProperty(
            name = "Asset Browser",
            description= "",
            items = editors,
            default='ASSETS',
    )

    ##############################################
    #    DRAW FUNCTION 
    ##############################################
    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        
        # Enable Button and Custom Icons
        layout.prop(self, "es_enable_buttons")
        layout.prop(self, "es_enable_maximize")

        if context.preferences.addons[__package__].preferences.es_enable_buttons:
            es_custom_icon = context.preferences.addons[__package__].preferences.es_custom_icon
            layout.prop(self, "es_custom_icon", icon = es_custom_icon)
        
        # Choose the pairing editors
        box = layout.box()
        box.label(text="Choose the pairing editors. For none select the same editor", icon='WINDOW')
        box.separator()
        # row = box.row()
        # row.label(text="3D Viewport", icon='VIEW3D')
        box.prop(self, "es_view_3d", text="3D Viewport")
        box.prop(self, "es_image_editor", text="Image Editor")
        box.prop(self, "es_uv", text="UV Editor")
        box.prop(self, "es_compositor", text="Compositor")
        box.prop(self, "es_texture_node", text="Texture Node Editor")

        # GeoNodes only appears on 2.92 and above
        if bpy.app.version >= (2, 92, 0):
            box.prop(self, "es_geometry_node", text="Geometry Node Editor")

        # Spreadsheet only appears on 2.93 and above
        if bpy.app.version >= (2, 93, 0):
            box.prop(self, "es_spreadsheet", text="Spreadsheet")

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

        # Asset Browser only appears on 3.0 and above
        if bpy.app.version >= (3, 0, 0):
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
##############################################
#    USER PREFERENCES 
##############################################

import bpy 

class ES_UserPrefs(bpy.types.AddonPreferences):
    bl_idname = __package__

    # popup_dialog : bpy.props.BoolProperty(
    #     name="Enable Popup Dialog on Creation",
    #     description="Enable or Disable the Popup Dialog on creation of Quick Lattice", 
    #     default=True
    #     )

    items = [
        ('NONE', 'None', 'None', '', 0, '', ''),
        ('VIEW_3D', '3D Viewport', '3D Viewport', 'VIEW3D', 1, 'view_3d', 'VIEW3D_HT_tool_header'),
        ('VIEW', 'Image Editor', 'Image Editor', 'IMAGE', 2, 'image_editor', 'IMAGE_HT_header') if bpy.app.version < (2, 91, 0)
        else ('IMAGE_EDITOR', 'Image Editor', 'Image Editor', 'IMAGE', 2, 'image_editor', 'IMAGE_HT_header'),
        ('UV', 'UV Editor', 'UV Editor', 'UV', 3, 'uv_editor', 'IMAGE_HT_header'),
        ('ShaderNodeTree', 'Shader Editor', 'Shader Editor', 'SHADING_RENDERED', 4, 'shader_editor', 'NODE_HT_header'),
        ('CompositorNodeTree', 'Compositor', 'Compositor', 'NODE_COMPOSITING', 5, 'compositor', 'NODE_HT_header'),
        ('TextureNodeTree', 'Texture Node Editor', 'Texture Node Editor', 'NODE_TEXTURE', 6, 'texture_node_editor', 'NODE_HT_header'),
        ('SEQUENCE_EDITOR', 'Video Squiencer', 'Video Sequencer', 'SEQUENCE', 7, 'sequence_editor', 'SEQUENCER_HT_header'),
        ('CLIP_EDITOR', 'Movie Clip Editor', 'Movie Clip Editor', 'TRACKER', 8, 'clip_editor', 'CLIP_HT_header'),
        ('DOPESHEET', 'Dope Sheet', 'Dope Sheet', 'ACTION', 9, 'doppesheet', 'DOPESHEET_HT_header'),
        ('TIMELINE', 'TimeLine', 'TimeLine', 'TIME', 10, 'timeline', 'DOPESHEET_HT_header'),
        ('FCURVES', 'Graph Editor', 'Graph Editor', 'GRAPH', 11, 'fcurves', 'GRAPH_HT_header'),
        ('DRIVERS', 'Drivers', 'Drivers', 'DRIVER', 12, 'drivers', 'GRAPH_HT_header'),
        ('NLA_EDITOR', 'Nonlinear Animation', 'Nonlinear Animation', 'NLA', 13, 'nla_editor', 'NLA_HT_header'),
        ('TEXT_EDITOR', 'Text Editor', 'Text Editor', 'TEXT', 14, 'text_editor', 'TEXT_HT_header'),
        ('CONSOLE', 'Python Console', 'Python Console', 'CONSOLE', 15, 'console', 'CONSOLE_HT_header'),
        ('INFO', 'Info', 'Info', 'INFO', 16, 'info', 'INFO_HT_header'),
        ('OUTLINER', 'Outliner', 'Outliner', 'OUTLINER', 17, 'outliner', 'OUTLINER_HT_header'),
        ('PROPERTIES', 'Properties', 'Properties', 'PROPERTIES', 18, 'properties', 'PROPERTIES_HT_header'),
        ('FILE_BROWSER', 'File Browser', 'File Browser', 'FILEBROWSER', 19, 'file_browser', 'FILEBROWSER_HT_header'),
        ('PREFERENCES', 'Preferences', 'Preferences', 'PREFERENCES', 20, 'preferences', 'USERPREF_HT_header'),
        ('an_AnimationNodeTree', 'Animation Nodes', 'Animation Nodes', 'ONIONSKIN_ON', 21, 'animation_nodes', 'NODE_HT_header')
    ]

    # view_3d: EnumProperty(
    #     name='View 3D',
    #     items=[elem[:5] for elem in items],
    #     default='ShaderNodeTree',
    #     update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    # )
    # [(id, name, description, icon, id_num, variable name, area header name), ...]
    view_3d : bpy.props.EnumProperty(
        name = "View 3D",
        description = "Select an editor to pair them",
        items = [elem[:5] for elem in items],
        # items = ['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'PREFERENCES'],
        default='ShaderNodeTree',
        # update=lambda self, context: AREA_SWITCHER_ui.update(context=context)
    )
    
    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = True
        box = layout.box()
        box.separator()
        # box.prop(self, "popup_dialog")
        box.separator()
        box.prop(self, "view_3d", text="3D Viewport")
        # box.prop(self, "editor_selector", text="Image Editor")
        # box.prop(self, "editor_selector", text="UV Editor")
        # box.prop(self, "editor_selector", text="Shader Editor")
        box.separator()

####################################
# REGISTER/UNREGISTER
####################################
def register():
    bpy.utils.register_class(ES_UserPrefs) 
        
def unregister():
    bpy.utils.unregister_class(ES_UserPrefs)
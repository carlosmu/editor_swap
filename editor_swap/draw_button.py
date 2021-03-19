####################################
# DRAW BUTTONS
####################################

import bpy

def draw_editor_swap(self, context):
    # If not "TextureNodeTree" draw buttons (because shares space with shaders and compositor). 
    # if not context.area.ui_type == 'TextureNodeTree': 
        ## TO-DO use properties defined by the user
    if context.area.ui_type == 'OUTLINER':
        self.layout.operator("area.editor_swap",text="", icon='MONKEY')
    else:
        self.layout.operator("area.editor_swap",text="", icon='WINDOW')

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
# import bpy

# class Editor_Swap_Keymap:

#     addon_keymaps = []

#     # @classmethod # probar desactivar esto
#     def register(cls, context):
#         wm = bpy.context.window.manager
#         kc = wm.keyconfigs.addon
#         if kc:
#             km = kc.keymap.new(name='3D VIEW', space_type='EMPTY')
#             kmi = km.keymap_items.new("area.editor_swap", type = 'X', value = 'PRESS', ctrl = True, alt = True)
#             addon_keymaps.append((km, kmi))
    
#     def unregister(cls):
#         for km, kmi in addon_keymaps:
#             km.keymap_items.remove(kmi)
#         addon_keymaps.clear()




# def register():
#     Editor_Swap_Keymap.register()


# def unregister():
#     Editor_Swap_Keymap.unregister()
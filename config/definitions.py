import os
import ctypes.wintypes


ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
src_dir = os.path.join(ROOT_DIR, 'src')
app_dir = os.path.join(src_dir, 'app')
main_path = os.path.join(app_dir, 'ui', 'Main.py')
assets_dir = os.path.join(src_dir, 'assets')
img_dir = os.path.join(assets_dir, 'img')
txt_dir = os.path.join(assets_dir, 'txt')

CSIDL_PERSONAL = 5
SHGFP_TYPE_CURRENT = 0
doc_array = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, doc_array)
doc_dir = doc_array.value

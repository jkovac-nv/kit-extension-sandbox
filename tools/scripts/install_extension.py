import os
import shutil
import sys

def install_extension():
    src_path = Path(__file__).resolve().parent.parent.parent
    src_exts_path = os.path.join(src_path, 'exts')
    dst_exts_path = get_default_exts_path()
    subdirs = os.listdir(src_exts_path)
    if not len(subdirs):
        return
    for subdir in subdirs:
        src = os.path.join(src_exts_path, subdir)
        dst = os.path.join(dst_exts_path, subdir)

        # if folder exists lets delete from dst first
        if os.path.isdir(dst):
            print(f'{subdir} exists in destination. Removing')
            shutil.rmtree(dst)
        # os.chmod(src, 0o777)
        if len(sys.argv) > 1:
            if sys.argv[1] == "i":
                print("Installing extension(s)")
                shutil.copytree(src, dst)
            elif sys.argv[1] == "u":
                print("Uninstalling extension(s)")


def get_default_exts_path():
    docs_dir = os.path.join(os.path.expanduser("~"), "Documents")
    # additional handling for OneDrive directories, etc
    try:
        import ctypes.wintypes
        buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, 5, None, 0, buf)
        docs_dir = buf.value
    except:  # pylint: disable=bare-except
        pass
    return os.path.join(docs_dir, "kit\\shared\\exts")

if __name__ == "__main__":
    install_extension()

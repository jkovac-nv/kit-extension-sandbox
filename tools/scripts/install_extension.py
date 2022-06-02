import os
import shutil
import sys


""" May need to switch to copying per-App """
# import sys
# import json
# import urllib.request
# def find_omniverse_apps():
#     supported_apps = ["create", "code", "view"]
#     try:
#         with urllib.request.urlopen("http://127.0.0.1:33480/components") as response:
#             r = response.read()
#     except Exception as e:
#         print(f"Failed retrieving apps from an Omniverse Launcher, maybe it is not installed?\nError: {e}")
#         sys.exit(1)
#     app_paths = []
#     # @TODO clean this up some
#     for x in json.loads(r.decode("utf-8")):
#         latest = x.get("installedVersions", {}).get("latest", "")
#         if latest:
#             for s in x.get("settings", []):
#                 if s.get("version", "") == latest:
#                     if x["slug"] in supported_apps:
#                         app_paths.append(s["base"])
#     return app_paths

def install_extension():
    # os.chdir("../../")
    src_exts_path = os.path.join(os.getcwd(), 'exts')
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

from util.datutil import DataFile
from pyshortcuts import make_shortcut
from pathlib import Path
import patches.vulkan
import util.fileutil
import shutil

patcher_version = "1.0"

class PatchOption:
    def __init__(self, n, opt, rec):
        self.display_name: str = n
        self.options: list[str] = opt
        self.recommended: int = rec
        self.value: str = self.options[rec]

class PatchConfig:
    def __init__(self):
        self.renderer = PatchOption("Renderer", ["Metal", "OpenGL", "Vulkan"], 0)

def apply(roblox_path: str, config: PatchConfig):
    data_file = DataFile(roblox_path + "/roblox-silicon", 0)
    data_file.write("version", patcher_version)
    data_file.write("launch_config", "")

    if config.renderer.value == "Metal":
        data_file.write("launch_config", "--force-metal")
    if config.renderer.value == "OpenGL":
        patches.vulkan.clear_patch(roblox_path)
    if config.renderer.value == "Vulkan":
        patches.vulkan.apply_patch(roblox_path)
    
    data_file.flush()
    
    path = Path(__file__).resolve().parent / "bootstrapper.py"
    shutil.copy(str(path), roblox_path + "/bootstrapper.py")
    make_shortcut(roblox_path + "/bootstrapper.py", name="roblox-silicon", icon=roblox_path+"/Contents/Resources/AppIcon.icns", folder="/Applications", terminal=False)

def unapply(roblox_path: str):
    patches.vulkan.clear_patch(roblox_path)
    util.fileutil.destroy(roblox_path + "/roblox_silicon")

def get_patch_version(robloxPath):
    data = DataFile(robloxPath + "/roblox-silicon", 1)

    try:
        return data.filedata["version"]
    except:
        return None
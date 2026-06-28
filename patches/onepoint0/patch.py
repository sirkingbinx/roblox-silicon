import util.fileutil as fileutil
import util.datutil as datutil

from pathlib import Path
from pyshortcuts import make_shortcut

import shutil

class Patch10:
    version = "1.0"

    def apply(self, robloxPath: str):
        data = datutil.rsil_data(robloxPath + "/roblox-silicon.dat", 0)

        data.write("version", self.version)
        data.write("launch_config", "--force-metal")

        data.flush()

        path = (Path(__file__).resolve().parent / "bootstrap.py")
        shutil.copy(str(path), robloxPath + "/bootstrap.py")

        make_shortcut(robloxPath + "/bootstrap.py", name="roblox-silicon", icon=robloxPath+"/Contents/Resources/AppIcon.icns", folder="/Applications", terminal=False)

    def unapply(self, robloxPath: str):
        fileutil.destroy(robloxPath + "/roblox-silicon.dat")
        fileutil.destroy(robloxPath + "/bootstrap.py")
        fileutil.destroy("/Applications/roblox-silicon.app")
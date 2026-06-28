import util.datutil

import patches.onepoint0.patch as patch_10

patches = {
    "1.0": patch_10.Patch10()
}

def all_patch_versions():
    return list(patches)

def get_patch_version(robloxPath):
    data = util.datutil.rsil_data(robloxPath + "/roblox-silicon.dat", 1)
    try:
        return data.filedata["version"]
    except:
        return None
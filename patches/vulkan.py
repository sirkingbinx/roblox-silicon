import util.fileutil
import os

vulkan_config_file = """{
    \"DFIntTaskSchedulerTargetFps\": 240,
    \"FFlagDebugGraphicsDisableMetal\": \"true\",
    \"FFlagDebugGraphicsPreferVulkan\": \"true\"
}
"""
vulkan_config_file_path = "/Contents/MacOS/ClientSettings/ClientAppSettings.json"

def apply_patch(roblox_path: str):
    file_path = roblox_path + vulkan_config_file_path

    os.makedirs(roblox_path + "/Contents/MacOS/ClientSettings")

    with open(file_path, "w") as client_settings:
        client_settings.write(vulkan_config_file)
        client_settings.flush()

def clear_patch(roblox_path: str):
    util.fileutil.destroy(roblox_path + vulkan_config_file_path)
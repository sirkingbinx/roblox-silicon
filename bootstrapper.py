# roblox-silicon bootstrapper

# This can be ran either as a Python script, a Python module, or an application shortcut
# by opening roblox-silicon and pressing "Create Launch Shortcut"

import os
import pathlib
import subprocess

from tkinter import messagebox

class rsil_data:
    def __init__(self, fname: str):
        self.filepath = fname
        self.filedata = {}

        if not (os.path.exists(self.filepath) and os.path.isfile(self.filepath)):
            return
        
        with open(self.filepath, "r") as file:
            for line in file.readlines():
                kv = line.split("=")

                if len(kv) > 2:
                    print("Syntax error in roblox-silicon-dat: KV pair - {key}={value}")

                self.filedata[kv[0].strip()] = kv[1].strip()

def launch():
    script_path = pathlib.Path(__file__).resolve()
    roblox_app_dir = script_path.parent

    data = rsil_data(roblox_app_dir / "roblox-silicon")
    subprocess.run(["open", roblox_app_dir, "--args", data.filedata["launch_config"]])

if __name__ == "__main__":
    launch()
# roblox-silicon/app.py
# Tk interface is based from here

from tkinter import *
from tkinter import messagebox, ttk

import platform
import sys

import patcher

patch_version = patcher.get_patch_version("/Applications/Roblox.app")

root = Tk()
root.title("roblox-silicon")
root.geometry("300x375")

combo = ttk.Combobox(root, values=patcher.all_patch_versions(), state="readonly")
combo.set("Patch version")
combo.pack(pady=20)

def run():
    if not ((sys.platform == "darwin") and (platform.machine() == "arm64")):
        messagebox.showinfo("Unsupported", "apple-silicon is designed for M-series macOS computers.")
        return

    apply_patch_button = Button(root, text="Apply Patch", command=apply_patch)
    apply_patch_button.pack()

    if patch_version != None:
        rem_patch_button = Button(root, text=f"Remove Patch (Version {patch_version})", command=remove_patch)
        rem_patch_button.pack()

    root.mainloop()

def apply_patch():
    patcher.patches[combo.get()].apply("/Applications/Roblox.app")
    messagebox.showinfo("Installed", f"The game has been patched with roblox-silicon v{combo.get()}. You may run Roblox by running the roblox-silicon app (/Applications/roblox-silicon.app)")

def remove_patch():
    patcher.patches[patch_version].unapply("/Applications/Roblox.app")
    messagebox.showinfo("Uninstalled", "The patch has been removed.")

if __name__ == "__main__":
    run()
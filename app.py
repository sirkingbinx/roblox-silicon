# roblox-silicon/app.py
# Tk interface is based from here

from tkinter import *
from tkinter import messagebox, ttk

import platform
import sys

import patcher

patch_version = patcher.get_patch_version("/Applications/Roblox.app")
patch_options = patcher.PatchConfig()

root = Tk()
root.title("roblox-silicon")
root.geometry("335x375")

def run():
    if not ((sys.platform == "darwin") and (platform.machine() == "arm64")):
        messagebox.showinfo("Unsupported", "apple-silicon is designed for M-series macOS computers.")
        return

    config_fields = [
        key for key, value in vars(patch_options).items()
        if not key.startswith('__') and not callable(value)
    ]

    row = 0

    for k in config_fields:
        v: patcher.PatchOption = getattr(patch_options, k)

        label = ttk.Label(root, text=v.display_name + ":")
        label.grid(row=row, column=0, padx=5, pady=2, sticky="w")

        combo = ttk.Combobox(root, values=v.options, state="readonly")
        combo.grid(row=row, column=1, padx=5, pady=2)
        combo.current(v.recommended)

        def on_select(event):
            v.value = combo.get()

        combo.bind("<<ComboboxSelected>>", on_select)

        row += 1
    
    apply_patch_button = Button(root, text="Apply Patch", command=apply_patch)
    apply_patch_button.grid(row=row+1, column=0, padx=5, pady=2)

    remove_patch_button = Button(root, text="Remove Patch", command=remove_patch)
    remove_patch_button.grid(row=row+1, column=1, padx=5, pady=2)

    root.mainloop()

def apply_patch():
    patcher.apply("/Applications/Roblox.app", patch_options)
    messagebox.showinfo("Installed", f"The game has been patched with roblox-silicon. You may run Roblox by running the roblox-silicon app (/Applications/roblox-silicon.app)")

def remove_patch():
    patcher.unapply("/Applications/Roblox.app")
    messagebox.showinfo("Uninstalled", "The patch has been removed.")

if __name__ == "__main__":
    run()
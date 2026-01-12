"""import tkinter as tk
from tkinter import ttk
import os

# --- Your game state ---
state = {
    "producers": {
        "barista": {"name": "Hire Barista", "icon": "barista.png"},
        "machine": {"name": "Buy Coffee Machine", "icon": "machine.png"},
        "shop": {"name": "Open Coffee Shop", "icon": "shop.png"},
        "farmer": {"name": "Hire Coffee Farmer", "icon": "shop.png"},
        "factory": {"name": "Build Coffee Factory", "icon": "shop.png"},
        "franchise": {"name": "Start Global Franchise", "icon": "shop.png"},
        "Solar_system_shop": {"name": "Start Solar System Shop", "icon": "solar_system_shop.png"}
    }
}

# --- Setup window ---
root = tk.Tk()
root.title("Producer Button Test")
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

producers_tab = ttk.Frame(notebook)
notebook.add(producers_tab, text="Producers")

images = {}

# Change this to your actual image folder
img_path = os.path.join(os.getcwd(), "Images")
print("🔍 Looking for images in:", img_path)

# --- Test loop ---
for pid, producer in state["producers"].items():
    frame = tk.Frame(producers_tab)
    frame.pack(fill="x", pady=3)

    icon_file = os.path.join(img_path, producer["icon"])
    print(f"Checking {pid}: {icon_file}")

    try:
        images[pid] = tk.PhotoImage(file=icon_file)
        btn = tk.Button(frame, image=images[pid])
        btn.pack(side="left", padx=5)
        tk.Label(frame, text=producer["name"]).pack(side="left")
        print(f"✅ Loaded: {pid}")
    except Exception as e:
        print(f"❌ Could not load {pid}: {e}")
        tk.Label(frame, text=f"[Missing image] {producer['name']}").pack(side="left")

root.mainloop()"""

"""
import tkinter as tk

root = tk.Tk()

from button_sound import Play_Music
music = Play_Music()

def sound(var_1):

            music.set_volume(float(var_1) / 100)

var_1 = tk.DoubleVar(value=70)
sound_bar = tk.Scale(root, variable = var_1, from_ = 0, to = 100, resolution=1, command = sound, orient = tk.HORIZONTAL)
sound_bar.pack()
music.loop_music()
root.mainloop()"""
import tkinter as tk
from tkinter import ttk
import os
from tool_tips import ToolTip
from helpers import Helpers
from play_music import Play_Music
from ttkthemes import ThemedTk

class Gui:
    helper = Helpers()
    def setup_root(self) -> tk.Tk:
        root = ThemedTk(theme="breeze")
        root.title("🍵 Josh's Coffee Shop 🍵")
        return root

    def setup_stats_label(self, root: tk.Tk) -> tk.Label:
        stats_label = ttk.Label(root, text="", font=("Arial", 12))
        stats_label.pack(pady=5)
        return stats_label

    def setup_canvas(self, root: tk.Tk) -> tk.Canvas:
        canvas = tk.Canvas(root, width=120, height=100, bg="white")
        canvas.pack(pady=5)
        return canvas

    def setup_brew_button(self, canvas: tk.Canvas, images: dict, brew_click, stats_label: tk.Label, producer_widgets: dict, upgrade_widgets: dict, stats_widgets: dict, state: dict) -> tk.Button:
        img_path = os.getcwd()
        img_path = os.path.join(img_path, "Images")
        images["brew"] = tk.PhotoImage(file=os.path.join(img_path, "cup.png"))
        
        brew_btn = tk.Button(canvas, image=images["brew"], command=lambda: brew_click(self, canvas, stats_label, producer_widgets, upgrade_widgets, stats_widgets, state), borderwidth=0, highlightthickness=0, bg="white", activebackground="white")
        canvas.create_window(60, 50, window=brew_btn)
        ToolTip(brew_btn, "Brew Coffee")

        return brew_btn

    def setup_sound_bar(self, root) -> tk.Scale:
        
        music = Play_Music()
        music.loop_music()
        
        def sound(value):
            volume = float(value) / 100
            music.set_volume(volume)

        var_1 = tk.DoubleVar(value=67)
        
        sound_bar = tk.Scale(
        root,
        variable=var_1,
        from_=0,
        to=100,
        resolution=1,
        orient=tk.HORIZONTAL,
        command=sound
    )
        
        sound_bar.pack()
        ToolTip(sound_bar, "Music Volume")
        return sound_bar

    def setup_notebook(self, root: tk.Tk) -> ttk.Notebook:
        notebook = ttk.Notebook(root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        return notebook

   
    def setup_producers_tab(self, notebook: ttk.Notebook, images: dict, stats_label: tk.Label, producer_widgets: dict, upgrade_widgets: dict, stats_widgets: dict, state: dict, buy_producer=None) -> tk.Label:
        producers_tab = ttk.Frame(notebook)
        notebook.add(producers_tab, text="Producers")
        
        canvas = tk.Canvas(producers_tab)
        scrollbar = ttk.Scrollbar(producers_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        for pid, p in state["producers"].items():
            frame = tk.Frame(scrollable_frame)
            frame.pack(fill="x", pady=2)
            img_path = os.path.join(os.getcwd(), "Images")
            images[pid] = tk.PhotoImage(file=os.path.join(img_path, p["icon"]))

            button_border = tk.Frame(frame, highlightbackground = "black", highlightthickness = 2, bd=0)
            button_border.pack(side="left")
            btn = tk.Button(button_border, image=images[pid], fg="black", bg="white",  command=lambda pid=pid: buy_producer(pid, notebook, stats_label, producer_widgets, upgrade_widgets, stats_widgets, state))
            btn.pack()
            label = ttk.Label(frame, text=p.get("name", f"Producer {pid}"), anchor="w", justify="left")
            label.pack(side="left", padx=5)
            producer_widgets[pid] = {"button": btn, "label": label}

        return producers_tab
            

    def setup_upgrades_tab(self, notebook: ttk.Notebook, images: dict, upgrade_widgets: dict, state: dict, buy_upgrade, stats_label: tk.Label, producer_widgets: dict, stats_widgets: dict) -> tk.Frame:
        upgrades_tab = ttk.Frame(notebook)
        notebook.add(upgrades_tab, text="Producers")
        
        canvas = tk.Canvas(upgrades_tab)
        scrollbar = ttk.Scrollbar(upgrades_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        for uid, upgrade in state["upgrades"].items():
            frame = tk.Frame(scrollable_frame)
            frame.pack(fill="x", pady=2)
            img_path = os.path.join(os.getcwd(), "Images")
            images[uid] = tk.PhotoImage(file=os.path.join(img_path, upgrade["icon"]))

            button_border = tk.Frame(frame, highlightbackground = "black", highlightthickness = 2, bd=0)
            button_border.pack(side="left")
            btn = tk.Button(button_border, image=images[uid], command=lambda uid=uid: buy_upgrade(uid, state, canvas, stats_label, producer_widgets, upgrade_widgets, stats_widgets))
            btn.pack()
            
            label = ttk.Label(frame, text=upgrade.get("name", f"Upgrade: {uid}"), anchor="w", justify="left")
            label.pack(side="left", padx=5)
            upgrade_widgets[uid] = {"button": btn, "label": label}
            
            
            formatted_type = str(upgrade["unlock_at"])
            formatted_type = formatted_type.strip().replace("{", "").replace("}", "").replace("'", "")
            
            if formatted_type.count("producer:") == 1:
                if formatted_type.count("[") == 1 and formatted_type.count("]") == 1:
                    formatted_type = formatted_type.replace("[", "").replace("]", "")
                
                
                formatted_type = formatted_type.replace("producer:", "").replace("(", "").replace(")", "")
                formatted_type = formatted_type.replace(",", "s needed:")
                
            else:
                formatted_type = list(formatted_type)
                formatted_type.pop(formatted_type.index(":"))

                string_number = ""
                money_text = ""
                for i in formatted_type:
                    try:
                        string_number += str(int(i))
                    except ValueError:
                        money_text += i
                
                string_number = int(string_number)
                final = money_text + "needed: " f"${(string_number):,}"

                formatted_type = final

            ToolTip(btn, formatted_type)
            

        return upgrades_tab


    def setup_stats_tab(self, notebook: ttk.Notebook, stats_widgets: dict) -> ttk.Frame:
        stats_tab = ttk.Frame(notebook)
        notebook.add(stats_tab, text="Stats & Achievements")
        stats_widgets["clicks"] = ttk.Label(stats_tab, text="Total Clicks: 0", anchor="w")
        stats_widgets["clicks"].pack(fill="x", pady=2)
        stats_widgets["upgrades"] = ttk.Label(stats_tab, text="Total Upgrades Bought: 0", anchor="w")
        stats_widgets["upgrades"].pack(fill="x", pady=2)
        stats_widgets["achievements"] = ttk.Label(stats_tab, text="Achievements: None", anchor="w", wraplength=250, justify="left")
        stats_widgets["achievements"].pack(fill="x", pady=2)
        
        return stats_tab

    def update_ui(self, stats_label: ttk.Label, producer_widgets: dict, upgrade_widgets: dict, stats_widgets: dict, state: dict) -> None:
        stats_label.config(
            text=f"Cups: {Helpers.format_num(Helpers, state['cups'])}   |   Profit: ${Helpers.format_num(Helpers, state['money'])}\n"
                f"Production: {Helpers.get_total_production(Helpers, state):.1f} cups/sec   |   Click Power: {state['click_power']}"
        )

        # Producers
        for pid, producers in state["producers"].items():
            cost = Helpers.get_cost(Helpers, producers)

            producer_widgets[pid]["label"].config(
                text=f"{producers['name']} (x{producers['qty']})\nCost: ${Helpers.format_num(Helpers, cost)} | +{producers['baseProd']*producers['mult']}/sec"
            )

        # Upgrades
        for uid, upgrades in state["upgrades"].items():
            if not Helpers.is_unlocked(Helpers, upgrades, state):
                upgrade_widgets[uid]["label"].config(text="???")
                upgrade_widgets[uid]["button"].config(state="disabled")
                continue

            if upgrades["purchased"]:
                upgrade_widgets[uid]["label"].config(text=f"{upgrades['name']} (BOUGHT)")
                upgrade_widgets[uid]["button"].config(state="disabled")
            else:
                upgrade_widgets[uid]["label"].config(text=f"{upgrades['name']} - Cost: ${Helpers.format_num(Helpers, upgrades['cost'])}")
                upgrade_widgets[uid]["button"].config(state="normal")

        # Stats & Achievements
        stats_widgets["clicks"].config(text=f"Total Clicks: {state['total_clicks']}")
        stats_widgets["upgrades"].config(text=f"Total Upgrades Bought: {state['total_upgrades']}")
        stats_widgets["achievements"].config(
            text="Achievements:\n" + ("\n".join(state["achievements"]) if state["achievements"] else "None")
        )


    

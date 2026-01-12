import tkinter as tk
from tkinter import ttk
import json
import os
from DatabaseManager import DatabaseManager
from Gui import Gui
from helpers import Helpers
from game_state import game_state
import pygame
from Events_Handler import EventHandler
from CheatMode import enable_cheat_mode
from ttkthemes import ThemedTk

# ========================
# ONLY 2 GLOBALS IN THE GAME
# ========================

# Instantiate helpers and GUI helper classes (use instances, not class methods)
gui = Gui()
helper = Helpers()
root = gui.setup_root()
db = DatabaseManager()


# ========================
# GAME LOOP
# ========================
def game_loop(Gui: Gui, canvas: tk.Canvas, producer_widgets: dict, upgrade_widgets: dict, stats_widgets: dict, stats_label: tk.Label) -> None:
    prod = Helpers.get_total_production(Helpers, game_state.state) / 10
    game_state.state["cups"] += prod
    game_state.state["money"] += prod
    gui.update_ui(stats_label, producer_widgets, upgrade_widgets, stats_widgets, game_state.state)
    Helpers.check_achievements(Helpers, root, game_state.state)
    hang_man_earn = EventHandler.random_events(EventHandler, root)
    game_state.state["cups"] += hang_man_earn
    game_state.state["money"] += hang_man_earn
    gui.update_ui(stats_label, producer_widgets, upgrade_widgets, stats_widgets, game_state.state)
    # Passive effects: tax evasion passive income (no penalty)
    # game_loop runs every 100ms so dt is 0.1 seconds
    dt = 0.1
    tax = game_state.state["upgrades"].get("tax_evasion")
    if tax and tax.get("purchased"):
        passive = tax.get("passive_income", 0)
        if passive:
            game_state.state["money"] += passive * dt

    root.after(100, lambda: game_loop(Gui, canvas, producer_widgets, upgrade_widgets, stats_widgets, stats_label))

# ========================
# SAVE/LOAD STATE
# ========================

def save_state() -> None:
    save_db_state()

def save_db_state() -> None:
    # first time we are saving, insert into db
    if db is not None:
        db.create(
            {
                "cups": game_state.state["cups"],
                "money": game_state.state["money"],
                "click_power": game_state.state["click_power"],
                "total_clicks": game_state.state["total_clicks"],
                "total_upgrades": game_state.state["total_upgrades"],
                "achievements": ", ".join(game_state.state["achievements"]),
                "producers": json.dumps(game_state.state["producers"]),
                "upgrades": json.dumps(game_state.state["upgrades"])
            }
        )

def load_state():
    load_db_state()

def load_db_state() -> None:
    record = db.read() if db is not None else None

    if record:
        game_state.state["cups"] = record[1]
        game_state.state["money"] = record[2]
        game_state.state["click_power"] = record[3]
        game_state.state["total_clicks"] = record[4]
        game_state.state["total_upgrades"] = record[5]
        game_state.state["achievements"] = record[6].split(", ") if record[6] else []

        try:
            game_state.state["producers"] = json.loads(record[7])
        except json.JSONDecodeError:
            game_state.state["producers"] = {}
            
        try:
            game_state.state["upgrades"] = json.loads(record[8])
        except json.JSONDecodeError:
            game_state.state["upgrades"] = {}


def on_close() -> None:
    save_state()
    root.destroy()

# ========================
# MAIN
# ========================

def _cheat_action(canvas: tk.Canvas, producer_widgets: dict, upgrade_widgets: dict, stats_widgets: dict, stats_label: tk.Label):
        # Give 100 of each producer
        for pid, p in game_state.state["producers"].items():
            p["qty"] = p.get("qty", 0) + 100

        # Ensure cups and money are large enough
        game_state.state["cups"] = max(game_state.state.get("cups", 0), 10000)
        game_state.state["money"] = max(game_state.state.get("money", 0), 100000)

        # Unlock / purchase all upgrades and apply their effects
        for uid, up in game_state.state["upgrades"].items():
            if not up.get("purchased", False):
                # apply effects
                if up.get("type") == "click":
                    game_state.state["click_power"] = game_state.state.get("click_power", 1) * up.get("mult", 1)
                elif up.get("type") == "producer":
                    target = up.get("target")
                    if target and target in game_state.state["producers"]:
                        game_state.state["producers"][target]["mult"] = game_state.state["producers"][target].get("mult", 1) * up.get("mult", 1)
                up["purchased"] = True
                game_state.state["total_upgrades"] = game_state.state.get("total_upgrades", 0) + 1

        # Trigger achievement checks (this will also show floating text on the UI)
        helper.check_achievements(canvas, game_state.state)

        # Refresh UI
        Gui.update_ui(stats_label, producer_widgets, upgrade_widgets, stats_widgets, game_state.state)

        # Print a short summary to the terminal so user sees the cheat ran
        print("Cheat activated: +100 to all producers, all upgrades purchased, achievements unlocked.")



def main() -> None:
    pygame.mixer.init()
    load_state()


    enable_cheat_mode(root, callback=_cheat_action, show_button=False)
    root.protocol("WM_DELETE_WINDOW", on_close)

    stats_label = gui.setup_stats_label(root)

    canvas = gui.setup_canvas(root)

# ========================

    # UI references
    producer_widgets = {}
    upgrade_widgets = {}
    stats_widgets = {}
    images = {}

    Gui.setup_brew_button(Gui, canvas, images, game_state.brew_click, stats_label, producer_widgets, upgrade_widgets, stats_widgets, game_state.state)
    Gui.setup_sound_bar(Gui, root)
    notebook = Gui.setup_notebook(Gui,root)

    gui.setup_producers_tab(notebook, images, stats_label, producer_widgets, upgrade_widgets, stats_widgets, game_state.state, game_state.buy_producer)
    gui.setup_upgrades_tab(notebook, images, upgrade_widgets, game_state.state, game_state.buy_upgrade, stats_label, producer_widgets, stats_widgets)
    gui.setup_stats_tab(notebook, stats_widgets)

    gui.update_ui(stats_label, producer_widgets, upgrade_widgets, stats_widgets, game_state.state)

    game_loop(gui, canvas, producer_widgets, upgrade_widgets, stats_widgets, stats_label)

    
    

    root.mainloop()

    pygame.mixer.quit()


# ========================
# START
# ========================
if __name__ == "__main__":
    main()
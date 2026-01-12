from tkinter.filedialog import Open
from Gui import Gui
from helpers import Helpers
from tool_tips import ToolTip
import play_sound
import pygame
import tkinter as tk
from tkinter import ttk
from play_sound import Play_Sound

class game_state:
    state = {
    "cups": 0.0,
    "money": 0.0,
    "click_power": 1,
    "total_clicks": 0,
    "total_upgrades": 0,
    "achievements": [],
    "producers": {
        "barista": {"name": "Hire Barista", "baseProd": 1, "baseCost": 2, "costMul": 1.15, "qty": 0, "mult": 1, "icon": "barista.png"},
        "machine": {"name": "Buy Coffee Machine", "baseProd": 5, "baseCost": 100, "costMul": 1.15, "qty": 0, "mult": 1, "icon": "machine.png"},
        "shop": {"name": "Open Coffee Shop", "baseProd": 20, "baseCost": 400, "costMul": 1.15, "qty": 0, "mult": 1, "icon": "shop.png"},
        "farmer": {"name": "Hire Coffee Farmer", "baseProd": 100, "baseCost": 2000, "costMul": 1.15, "qty": 0, "mult": 1, "icon": "shop.png"},
        "factory": {"name": "Build Coffee Factory", "baseProd": 500, "baseCost": 20000, "costMul": 1.15, "qty": 0, "mult": 1, "icon": "shop.png"},
        "franchise": {"name": "Start Global Franchise", "baseProd": 5000, "baseCost": 200000, "costMul": 1.15, "qty": 0, "mult": 1, "icon": "shop.png"},
        "solar_system_shop": {"name": "Open Solar System Coffee Shop", "baseProd": 50000, "baseCost": 2000000, "costMul": 1.15, "qty": 0, "mult": 1, "icon": "solar_system_shop.png"},
        "milkly_way_shop": {"name": "Open Milky Way Coffee Shop", "baseProd":500000, "baseCost":10000000, "costMul":1.15, "qty":0, "mult":1, "icon":"milkly_way.png"},
        "universal_shop": {"name": "Open Universal Coffee Shop", "baseProd":5000000, "baseCost":50000000, "costMul":1.15, "qty":0, "mult":1, "icon":"universe_shop.png"},
        "multiverse_shop": {"name": "Open Multiverse Coffee Shop", "baseProd":50000000, "baseCost":500000000, "costMul":1.15, "qty":0, "mult":1, "icon":"multiverse.png"},
    },
    "upgrades": {
        "stronger_hands": {"type": "click", "name": "Stronger Hands", "mult": 2, "cost": 200, "purchased": False, "unlock_at": {"money": 20}, "icon": "hands.png"},
        "turbo_brewing": {"type": "click", "name": "Turbo Brewing", "mult": 3, "cost": 1000, "purchased": False, "unlock_at": {"money": 100}, "icon": "turbo.png"},
        "better_beans": {"type": "producer", "name": "Better Beans", "target": "barista", "mult": 2, "cost": 500, "purchased": False, "unlock_at": {"producer": ("barista", 5)}, "icon": "beans.png"},
        "cold_brew": {"type": "producer", "name": "Cold Brew", "target": "barista", "mult": 2.5, "cost": 10000, "purchased": False, "unlock_at": {"producer": ("barista", 75)}, "icon": "beans.png"},
        "barista_mastery": {"type": "producer", "name": "Barista Mastery", "target": "barista", "mult": 1.5, "cost": 50, "purchased": False, "unlock_at": {"producer": ("barista", 10)}, "icon": "beans.png"},
        "machine_overclock": {"type": "producer", "name": "Machine Overclock", "target": "machine", "mult": 1.5, "cost": 500, "purchased": False, "unlock_at": {"producer": ("machine", 5)}, "icon": "turbo.png"},
        "shop_remodel": {"type": "producer", "name": "Shop Remodel", "target": "shop", "mult": 1.5, "cost": 2000, "purchased": False, "unlock_at": {"producer": ("shop", 5)}, "icon": "shop.png"},
        "farmer_irrigation": {"type": "producer", "name": "Farmer Irrigation", "target": "farmer", "mult": 1.5, "cost": 8000, "purchased": False, "unlock_at": {"producer": ("farmer", 10)}, "icon": "beans.png"},
        "factory_surge": {"type": "producer", "name": "Factory Surge", "target": "factory", "mult": 1.5, "cost": 50000, "purchased": False, "unlock_at": {"producer": ("factory", 20)}, "icon": "shop.png"},
        "franchise_investment": {"type": "producer", "name": "Franchise Investment", "target": "franchise", "mult": 1.5, "cost": 500000, "purchased": False, "unlock_at": {"producer": ("franchise", 25)}, "icon": "shop.png"},
        "master_barista": {"type": "click", "name": "Master Barista", "mult": 2, "cost": 5000, "purchased": False, "unlock_at": {"money": 2000}, "icon": "hands.png"},
        "double_tap": {"type": "click", "name": "Double Tap", "mult": 2, "cost": 10000, "purchased": False, "unlock_at": {"money": 5000}, "icon": "hands.png"},
        "caffeinated_fingers": {"type": "click", "name": "Caffeinated Fingers", "mult": 3, "cost": 50000, "purchased": False, "unlock_at": {"money": 20000}, "icon": "hands.png"},
        "coffee_god": {"type": "click", "name": "Coffee God", "mult": 5, "cost": 250000, "purchased": False, "unlock_at": {"money": 100000}, "icon": "hands.png"},
        "tax_evasion": {"type": "global", "name": "Tax Evasion", "mult": 2.5, "cost": 1250000, "bonus_money": 1000000, "passive_income": 5000, "purchased": False, "unlock_at": {"producer": ("franchise", 50)}, "icon": "hands.png"},
        "coffee_empire": {"type": "global", "name": "Coffee Empire", "mult": 10, "cost": 5000000, "bonus_money": 10000000, "passive_income": 100000, "purchased": False, "unlock_at": {"producer": ("franchise", 75)}, "icon": "hands.png"},
        "ultimate_coffee": {"type": "global", "name": "Ultimate Coffee", "mult": 25, "cost": 10000000, "bonus_money": 25000000, "passive_income": 250000, "purchased": False, "unlock_at": {"producer": ("barista", 150)}, "icon": "hands.png"},
        "click_frenzy": {"type": "click", "name": "Click Frenzy", "mult": 10, "cost": 50000000, "purchased": False, "unlock_at": {"money": 1000000}, "icon": "hands.png"}
    }
}




    def brew_click(self, canvas: tk.Canvas, stats_label: tk.Label, producer_widgets: dict, upgrade_widgets: dict, stats_widgets: dict, state: dict) -> None:
        gain = state["click_power"]
        state["cups"] += gain
        state["money"] += gain
        state["total_clicks"] += 1

        Helpers.floating_text(self, canvas, 60, 40, f"+{gain} coffee", color="saddlebrown")
        Helpers.check_achievements(Helpers, canvas, state)
        Gui.update_ui(Gui, stats_label, producer_widgets, upgrade_widgets, stats_widgets, state)
        


        Play_Sound().sound_play_on_click()

    def buy_producer(pid: int, notebook: ttk.Notebook, stats_label: tk.Label, producer_widgets: dict, upgrade_widgets: dict, stats_widgets: dict, state: dict) -> None:
        producer = state["producers"][pid]
        cost = Helpers.get_cost(Helpers, producer)

        if state["money"] >= cost:
            state["money"] -= cost
            producer["qty"] += 1
            Play_Sound().sound_play_on_click()

        Gui.update_ui(Gui, stats_label, producer_widgets, upgrade_widgets, stats_widgets, state)

    def buy_upgrade(uid: int, state: dict, canvas: tk.Canvas, stats_label: tk.Label, producer_widgets: dict, upgrade_widgets: dict, stats_widgets: dict) -> None:
        upgrades = state["upgrades"][uid]

        if upgrades["purchased"] or not Helpers.is_unlocked(Helpers, upgrades, state): return

        if state["money"] >= upgrades["cost"]:
            state["money"] -= upgrades["cost"]

            if upgrades["type"] == "click":
                state["click_power"] *= upgrades["mult"]
            elif upgrades["type"] == "producer":
                state["producers"][upgrades["target"]]["mult"] *= upgrades["mult"]
            elif upgrades["type"] == "global":
                # global upgrade: apply a multiplier to all producers and give a bonus
                mult = upgrades.get("mult", 1)
                bonus = upgrades.get("bonus_money", 0)
                if bonus:
                    state["money"] = state.get("money", 0) + bonus
                for p in state["producers"].values():
                    p["mult"] = p.get("mult", 1) * mult

            upgrades["purchased"] = True
            state["total_upgrades"] += 1
            Play_Sound().sound_play_on_click()

        Helpers.check_achievements(Helpers, canvas, state)
        Gui.update_ui(Gui, stats_label, producer_widgets, upgrade_widgets, stats_widgets, state)


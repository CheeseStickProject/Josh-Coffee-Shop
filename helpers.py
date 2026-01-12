import tkinter as tk
from tkinter import ttk


class Helpers:    
    def format_num(self, number: int) -> str:
        if number >= 1e6: return f"{number/1e6:.1f}M"
        if number >= 1e3: return f"{number/1e3:.1f}K"
        return f"{number:.0f}"

    def get_cost(self, producer: dict) -> int: return int(producer["baseCost"] * (producer["costMul"] ** producer["qty"]))

    def get_total_production(self, state: dict) -> int:
        return sum(p["qty"] * p["baseProd"] * p["mult"] for p in  state["producers"].values())

    def is_unlocked(self, upgrade: dict, state: dict) -> bool:
        cond = upgrade.get("unlock_at", {})

        if "money" in cond and  state["money"] < cond["money"]: return False

        if "producer" in cond:
            pid, qty = cond["producer"]

            if  state["producers"][pid]["qty"] < qty: return False

        return True

    def unlock_hint(self, upgrade: dict, state: dict) -> str:
        cond = upgrade.get("unlock_at", {})

        if "money" in cond: return f"Requires ${cond['money']}"

        if "producer" in cond:
            pid, qty = cond["producer"]
            return f"Requires {qty} { state['producers'][pid]['name']}(s)"
        
        return "Unlock condition unknown"
    
    def floating_text(self, canvas: tk.Canvas, x: int, y: int, text: str, color="black") -> None:
        label = tk.Label(canvas, text=text, fg=color, bg="white", font=("Arial", 10, "bold"))
        label.place(x=x, y=y)

        def animate(i=0):
            if i > 20: label.destroy(); return
            label.place(x=x, y=y - i)
            label.after(30, animate, i+1)

        animate()
    
    
    def check_achievements(self, canvas: tk.Canvas, state: dict) -> None:
        achievements = [
            ("First Brew", lambda: state["total_clicks"] >= 1),
            ("Apprentice Barista", lambda: state["producers"]["barista"]["qty"] >= 10),
            ("Bean Tycoon", lambda: state["cups"] >= 1000),
            ("Upgrade Enthusiast", lambda: state["total_upgrades"] >= 3),
            ("Coffee God", lambda: state["upgrades"]["coffee_god"]["purchased"] is True),
            ("Tax Evader", lambda: state["upgrades"]["tax_evasion"]["purchased"] is True),
            ("Master Brewer", lambda: state["producers"]["barista"]["qty"] >= 100),
            ("Franchise Owner", lambda: state["producers"]["franchise"]["qty"] >= 50),
            ("Coffee Connoisseur", lambda: state["cups"] >= 5000),
            ("Ultimate Upgrader", lambda: state["total_upgrades"] >= 10),
            ("Empire Builder", lambda: state["producers"]["franchise"]["qty"] >= 200),
            ("Coffee Baron", lambda: state["cups"] >= 10000),
            ("Legendary Brewer", lambda: state["producers"]["barista"]["qty"] >= 500),
            ("Ultimate Coffee God", lambda: state["upgrades"]["coffee_god"]["purchased"] is True and state["upgrades"]["tax_evasion"]["purchased"] is True),
            ("Click Master", lambda: state["total_clicks"] >= 10000),
            ("Coffee Emperor", lambda: state["producers"]["universal_shop"]["qty"] >= 1),
            ("Multiversal Mogul", lambda: state["producers"]["multiverse_shop"]["qty"] >= 1),
            ("Coffee Legend", lambda: state["cups"] >= 100000),
            ("Ultimate Coffee God", lambda: state["upgrades"]["ultimate_coffee"]["purchased"] is True),
            ("Click Frenzy", lambda: state["upgrades"]["click_frenzy"]["purchased"] is True),
            ("Global Dominator", lambda: state["total_upgrades"] >= 18),
            ("Coffee Overlord", lambda: state["producers"]["multiverse_shop"]["qty"] >= 1 and state["producers"]["universal_shop"]["qty"] >= 1),
            ("Coffee Tycoon", lambda: state["money"] >= 1000000),
            ("Ultimate Brewer", lambda: state["producers"]["barista"]["qty"] >= 1000),
        ]

        # Track current y position for stacking achievements
        current_y = 20
        
        for name, cond in achievements:
            if cond() and name not in state["achievements"]:
                state["achievements"].append(name)
                Helpers.floating_text(Helpers, canvas, 60, current_y, text=f"Achievement: {name}", color="green")
                current_y += 25  # Move down for next achievement



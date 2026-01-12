import tkinter as tk
import random
import threading
import time

class Coffee_Hangman():
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.wrong_guesses = 0

        self.dictionary = {
    "types_of_coffee": ["Espresso", "Americano", "Cappuccino", "Latte", "Macchiato", "Mocha", "Flat White",
    "Cortado", "Affogato", "Red Eye", "Cold Brew", "Nitro Coffee", "Iced Coffee",
    "Frappé", "Café au Lait", "Turkish Coffee", "Doppio", "Ristretto", "Breve", "Vienna Coffee"],

    # Coffee Beans & Origins
    "bean_origins": ["Arabica", "Robusta", "Liberica", "Excelsa", "Colombian", "Ethiopian", "Sumatran",
    "Guatemalan", "Brazilian", "Kenyan", "Kona", "Yirgacheffe", "Harrar", "Sidamo", "Mandheling"],

    # Brewing Methods & Equipment
    "brewing_methods": ["French Press", "Pour Over", "Chemex", "AeroPress", "Moka Pot", "Espresso Machine",
    "Percolator", "Drip Brewer", "Siphon", "Cold Dripper", "Grinder", "Tamper",
    "Portafilter", "Steam Wand", "Gooseneck Kettle", "Scale", "Coffee Filter"],

    # Flavor & Aroma Terms
    "flavors": ["Nutty", "Chocolatey", "Fruity", "Floral", "Earthy", "Caramel", "Spicy", "Smoky",
    "Bright", "Smooth", "Bitter", "Sweet", "Balanced", "Clean", "Full-bodied",
    "Acidity", "Aroma", "Roastiness"],

    # Roast Levels
    "roast_levels": ["Light Roast", "Medium Roast", "Dark Roast", "Blonde", "Cinnamon Roast", "City Roast",
    "Full City", "Vienna Roast", "French Roast", "Italian Roast"],

    # General Coffee Terms
    "general_coffee_terms": ["Barista", "Bean", "Roast", "Grind", "Extraction", "Crema", "Caffeine", "Decaf",
    "Shot", "Bloom", "Blend", "Single Origin", "Filter", "Brew Ratio", "Tamping",
    "Puck", "Doser", "Steaming", "Froth", "Cup Profile"]
        }

        self.category = random.choice(list(self.dictionary.keys()))
        
        self.word = list(random.choice(self.dictionary[self.category]))
        self.word = [w.lower() for w in self.word]

        self.label2 = tk.Label(self.root, text="Welcome to Hangman! \n Please Enter one letter at a time, IF you win, you will get $10,000 (and cups) \n PLEASE DO NOT PRESS THE 'X' BUTTON IN THE CORNER")
        self.label2.pack()

        self.text = ["_" for i in range(len(self.word))]
        
        self.label1 = tk.Label(self.root,text=str(self.text).replace("[","").replace("]","").replace(",","").replace("'","") )
        self.label1.pack()
        
        self.input = tk.Entry(self.root)
        self.guessed = []
        self.input.pack()

        self.input.bind("<Return>", lambda event: self.check_text())
        self.input.bind("<Escape>", lambda event: self.root.destroy())
        self.letters_guessed_text = tk.Label(self.root, text = f"guessed letters:{self.guessed}")
        self.letters_guessed_text.pack()

        self.category_label = tk.Label(self.root, text=f"Category: {self.category.replace('_',' ').title()}")
        self.category_label.pack()

        self.wrong_guesses_label = tk.Label(self.root, text=f"Wrong guesses: {self.wrong_guesses}")
        self.wrong_guesses_label.pack()

        self.outcome = None

        self.root.grab_set()

    def end(self) -> None:
        time.sleep(3)
        self.root.destroy()
        if Coffee_Hangman:
            return True
        else:
            return False
        
    def get_input(self) -> str:
        value = self.input.get()
        if value.isalpha() and len(value) == 1:
            return value.lower()
        else:
            return " "
    
    def reset_input(self) -> None:
        self.input.delete(0, tk.END)

    def check_text(self) -> None:

        if self.get_input() not in self.guessed:
            self.guessed.append(self.get_input())
            self.guessed.sort()
            self.letters_guessed_text.config(text=f"guessed letters:{str(self.guessed).replace('[','').replace(']','')}")

        if None in self.guessed:
            self.guessed.remove(None)
            self.letters_guessed_text.config(text=f"guessed letters:{str(self.guessed).replace('[','').replace(']','')}")

        if self.get_input() in self.word:
            for i in range(len(self.word)):
                if self.word[i] == self.get_input():
                    self.text[i] = self.get_input()
        elif self.get_input() == "":
            pass
        elif self.get_input() not in self.word or self.get_input() not in self.guessed:
            self.wrong_guesses += 1
            self.wrong_guesses_label.config(text=f"Wrong guesses: {self.wrong_guesses}")

        self.reset_input()
        
        if self.wrong_guesses > 6:

            game_over_text = tk.Label(self.root, text=f"Game Over! The word was {''.join(self.word)}")
            game_over_text.pack()

            self.thread = threading.Thread(target=self.end)
            self.thread.start()
            self.outcome = False
            

        self.label1.config(text=str(self.text).replace("[","").replace("]","").replace(",","").replace("'","") )

        if self.text == self.word:
            congrat_text = tk.Label(self.root, text="Congratulations")
            congrat_text.pack()
            self.thread = threading.Thread(target=self.end)
            self.thread.start()
            self.outcome = True

    def __eq__(self, other=True) -> bool:
        if self.outcome != None:
            return self.outcome == other
        else:
            return False

    def initialize(self, root):
        cof = Coffee_Hangman(root)
    
    


    def on_closing(self):
        self.root.destroy()
        return False

        
import tkinter as tk

import pygame
pygame.mixer.init()
#some point need to find a way if multiple sounds are playing
class Play_Sound():
    def __init__(self,sound_file:str="button_press_1s.ogg"):
    
        self.button_sound = pygame.mixer.Sound(sound_file)
        
    def sound_play_on_click(self, sound_level: float= 35/500) -> pygame.mixer.Sound:
        #sets the sound vol of the file
        self.button_sound.set_volume(sound_level)

        #when the function is called, it will play the sound.
        return self.button_sound.play() 
    
    def get_amount_getting_played(self) -> int:
        #checks how many times a button is getting played
        return self.button_sound.get_num_channels()
    
    def play_time(self, length_in_sec:int) -> int:
        #checks if the playtime is shorter or same as the desired length. Returns length
        if self.button_sound.get_length() > length_in_sec:
            self.button_sound.stop()
        else:
            pass
        return self.button_sound.get_length()
    

#Test Code
"""root = tk.Tk()
        
play = Play_Music()
play.loop_music()

button = tk.Button(text = "tetsing",
                   command = lambda:Play_Sound().sound_play_on_click())
                
                   

button.pack(padx=5, pady=0)

root.mainloop()
pygame.mixer.quit()"""

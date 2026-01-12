import tkinter as tk

import pygame
pygame.mixer.init()

#background music class
class Play_Music():
    
    def __init__(self, music_file="josh_game_music.wav", volume:float=70/500, fade_out=False):
        
        self.file = music_file
        self.volume = volume
        self.fade_out = fade_out
        pygame.mixer.music.load(self.file)
    def play(self) -> None:
        
        
        if self.fade_out:
            pygame.mixer.music.fadeout()
        else:
            pygame.mixer.music.play()
    def stop(self) -> None:
       pygame.mixer.music.stop()
    def restart(self) -> None:
        pygame.mixer.music.rewind()
    def play_time(self, length_in_sec:float) -> None:
        if pygame.mixer.music.get_pos() > length_in_sec:
            pygame.mixer.music.stop()
        else:
            pass
    def start_from(self, start_time:float) -> None:
        pygame.mixer.music.set_pos(start_time * 1000)
    
    def is_running(self) -> bool:
        return pygame.mixer.music.get_busy()
    
    def loop_music(self, times:int=-1) -> None:
        pygame.mixer.music.play(times)
    
    def set_volume(self, volume:float=0.7) -> None:
        pygame.mixer.music.set_volume(volume)
    def get_volume(self) -> float:
        return pygame.mixer.music.get_volume()
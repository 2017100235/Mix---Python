#funciona no pycharm 
from pygame import mixer

mixer.init()
mixer.music.load('disturbed_inside_the_fire.mp3')
mixer.music.play()
input()
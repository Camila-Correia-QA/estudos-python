import pygame
pygame.init()
pygame.mixer.music.load('leosantana.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

import webbrowser
webbrowser.open('testepy.wav')
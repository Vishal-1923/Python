# **************************************************** Assignment 11 ****************************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/94-Day-94-Exercise-11/.tutorial/Tutorial.md

'''
Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system
'''

from plyer import notification
import pygame
import time

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5  #duration in seconds
    )
def beep_notification():
    pygame.mixer.init()
    pygame.mixer.Sound('beep-01a.wav').play()  # Provide a path to a wav file
    time.sleep(5)
    

start_time = time.time()
while True:
    current_time = time.time()
    
    telapsed =  (current_time - start_time) / 3600
    if telapsed >= 2:
        show_notification("Reminder", "Have some water !!!")
        beep_notification()

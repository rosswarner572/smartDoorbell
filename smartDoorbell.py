#!/usr/bin/env python3

import telegram
import RPi.GPIO as GPIO
from time import sleep
from os import system
from pygame import mixer
import logging

tokenID = '637044422:AAHwS6DYxFlTu6UMZO3BfY6K1nx9jEn5RZg'
bot = telegram.Bot(token=tokenID)
chatID = 541823565

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        input_state = GPIO.input(17)
        if input_state == False:
            bot.sendMessage(chat_id=chatID, text="Doorbell is ringing")
            system("omxplayer -o alsa /home/pi/Music/doorbell-1.wav")
            sleep(2.0)
            continue

finally:
    bot.sendMessage(chat_id=chatID, text="doorbell is offline")
    GPIO.cleanup()



from datetime import datetime, timedelta
from email.mime.text import MIMEText
from Commends import Commends as cm
from Inputs import Paths as paths
import speech_recognition as sr
from selenium import webdriver
from termcolor import colored
from pyfiglet import Figlet
from Functions import Func as func
from pygame import mixer
from time import ctime
from gtts import gTTS 
import wget
import subprocess as sub
import pyfiglet.fonts
from zipfile import ZipFile
import pkg_resources
import webbrowser
import playsound
import pyautogui
import smtplib
import pyttsx3
import random
import getpass
import enum
import time
import os
import re

       
W = '\033[0m'  # Beyaz (normal)
R = '\033[31m'  # Kırmızı
G = '\033[32m'  # Yeşil
O = '\033[33m'  # Turuncu
B = '\033[34m'  # Mavi
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

f = Figlet(font='slant')

#CMD Size
def CMDSize():
    print(os.system(G))
    width = "150"
    height = "30"
    os.system("mode con cols="+width+"lines="+height)

#GameOne
def OpenGameOne():
    sub.Popen([paths.OpenGameOne],shell=True)
#gameTwo
def game_two():
    sub.Popen([paths.OpenGameTwo],shell=True)
#ShowIP
def MyIp():
    sub.call(["ipconfig"])      


def InstallBrowser():

	HaveOrNotFile = os.path.exists("chromedriver.exe")
	if HaveOrNotFile == False:
		try:
			url = "https://chromedriver.storage.googleapis.com/2.35/chromedriver_win32.zip"
			DownloadDriver = wget.download(url)
			print("\n\n")
			ExtractZIP = "chromedriver_win32.zip"
			with ZipFile (ExtractZIP,'r') as zip:
				zip.printdir()
				zip.extractall()
			os.remove("chromedriver_win32.zip")
		
		except KeyboardInterrupt:
			print("\n")
	else:
		print("")



	
		


def MyAssistan():
    print(f.renderText('TOKYO'))
    print(f.renderText('the daughter of the computer :)'))
    print(G+""" 

===============================================================================================================================================
                                                        
                                                        COMMANDS

** BROWSER **                                                       ** SYSTEM **
                        
- Google                   ==> [+] ör: (Open google...vb)           - Terminal (cmd)        ==> [+] ör: (Show terminal...vb)
- Facebook                 ==> [+] ör: (Open facebook...vb)         - Close                 ==> [+] ör: (Close: Tokyo is closed...vb)
- Auto Login Your Facebook ==> [+] ör: (Open My facebook...vb)      - shut down computer    ==> [+] ör: (shut down my computer...vb)
- Youtube                  ==> [+] ör: (Open youtube...vb)          - Create folder         ==> [+] ör: (Folder Created...vb)   
- Default Page             ==> [+] ör: (Open (my page name)...vb)   - Clear                 ==> [+] ör: (Clear terminal...vb)
- Youtube mp3 dowload Page ==> [+] ör: (Open youtube mp3...vb)      - Size                  ==> [+] ör: (My screen size...vb)
- Search google            ==> [+] ör: (Search google...vb)         - Ip                    ==> [+] ör: (My ip...vb)


________________________________________________________________________________________________________________________________________________

** PROPERTİES **                                                    ** DEFAULT **

- Time  ==> [+] ör: (What Time is it...vb)                         - how are you expressions  ==> [+] ör: (How are you...vb)
- Mail  ==> [+] ör: (Send Mail...vb)                               - Your Name                ==> [+] ör: (What is your name...vb)
- Word  ==> [+] ör: (Open Word...vb)                               - personality              ==> [+] ör: (hi,who is you...vb)
- Music ==> [+] ör: (Open Music...vb)
- Game  ==> [+] ör: (Open my game or My game...vb)
- Wifi  ==> [+] ör: (Show Wifi Password...vb)
- SS    ==> [+] ör: (Screenshot..vb)
- Find  ==> [+] ör: (Where is canada...vb)
               
=================================================================================================================================================

            """)

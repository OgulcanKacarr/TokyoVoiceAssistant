from datetime import datetime, timedelta
from email.mime.text import MIMEText
from Commends import Commends as cm
from Inputs import Paths
import speech_recognition as sr
from selenium import webdriver
from termcolor import colored
from pyfiglet import Figlet
from Functions import Func as func
from pygame import mixer
from time import ctime
from gtts import gTTS 
import subprocess as sub
import pyfiglet.fonts
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

f = Figlet(font='slant')

       
W = '\033[0m'  # Beyaz (normal)
R = '\033[31m'  # Kırmızı
G = '\033[32m'  # Yeşil
O = '\033[33m'  # Turuncu
B = '\033[34m'  # Mavi
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray



#SpeakMethod
def SpeakMethod(text):
        volume = 100
        engine = pyttsx3.init()
        engine.setProperty('volume', volume)
        engine.say(text)
        engine.runAndWait()

#SpeakErrorMethod
def SpeakErrorMethod(text):
        volume = 0.5
        engine = pyttsx3.init()
        engine.setProperty('volume', volume)
        engine.say(text)
        engine.runAndWait() 

#GetMic
def GetAudio(ask=False):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            SpeakErrorMethod("bip")
            audio = r.listen(source,phrase_time_limit = 3)
            said = ""
            if ask:
                print(ask)          
            try:
                said = r.recognize_google(audio,language="en")
                print(O+"[+] Command:",said)
            except sr.UnknownValueError:
                error=["I dont Understand","I can not understand","can you repeat","I did not understand what you have said","i don't think i understand","I did not hear","say it again"]
                mix = random.choice(error)
                time.sleep(0.1)
                print(mix)
                func.my_assistan()
            except RequestError:
                error=["I dont Understand!","I can not understand!","can you repeat!","I did not understand what you have said!","i don't think i understand","I did not hear","say it again"]
                mix = random.choice(error)
                time.sleep(0.1)
                print(mix)
                func.MyAssistan()

        return said.lower()

#DoFunc
def jarvis(text):
    if text in cm.how_are_You:
        speak(random.choice(cm.how_are_You_answer))
    if text in cm.your_name:
        speak(random.choice(cm.your_name_answer))
    if text in cm.system_commends:
        speak(random.choice(cm.system_commends_return))
        os.system("start cmd")
    if text in cm.close:
        speak(random.choice(cm.close_return))
        quit()
    if "open video" in text:
        speak("video programing starting")
        os.startfile([control_input.obsPath])
    if "where is" in text:
        driver_path = control_input.browser_control
        browser = webdriver.Chrome(executable_path=driver_path)
        data = text.split(" ")
        location_url = "https://www.google.com/maps/place/" + str(data[2])
        speak("of course i am researching immediately " + data[2] + " is.")
        maps_arg = location_url
        browser.get(maps_arg)
    if text in cm.music:
        playerPath = control_input.music
        speak(random.choice(cm.music_return))
        os.startfile(playerPath)    
    if text in cm.word:
        speak("Opening Microsoft Word")
        os.startfile(control_input.wordPath)
    if "open my game" in text:
        speak(control_input.gameOneName)
        openGameOne()
    if "my game" in text:
        openGameTwo()
    if text in cm.clock:
        speak(datetime.now().strftime('%H:%M:%S'))
        ax = datetime.now().strftime('%H:%M:%S')
        print(ax)
    elif text in cm.search:
        speak("what search google")
        searchh = get_audio("what do you want me to call")
        url = "https://www.google.com/search?q=" + cm.searchh
        webbrowser.get().open(url)
        speak("I found for your request") 
        d = get_audio()
        if "close page" in d:
            browser.close()
        elif "back" in d or "backpage" in d:
            driver.back()
    elif text in cm.open_google:
        driver_path = control_input.browserControlPath
        browser = webdriver.Chrome(executable_path=driver_path)
        speak("google is opening")
        browser.get("https://google.com")
        a = get_audio()
        if "close page" in a:
            browser.close()
    elif text in cm.my_facebook: 
        driver_path = control_input.browserControlPath
        browser = webdriver.Chrome(executable_path=driver_path)
        speak(random.choice(cm.my_facebook_return))
        browser.get("https://facebook.com")
        email_xpath=  '//*[@id="email"] ' 
        password_Xpath= ' //*[@id="pass"] ' 
        login_button_xpath=  '//*[@id="u_0_b"]' 
        email_element = browser.find_element_by_xpath(email_xpath)
        password_element = browser.find_element_by_xpath(password_Xpath)
        login_butto_element = browser.find_element_by_xpath(login_button_xpath)
        email_element.send_keys(opt_input.email_page)
        password_element.send_keys(password)
        login_butto_element.click()
        b = get_audio()
        if "close page" in b:
            browser.close()
    elif "my school page" in text:
        driver_path = control_input.browserControlPath
        browser = webdriver.Chrome(executable_path=driver_path)
        browser.get("https://bys.ibu.edu.tr/")
        kullanıcı_Adı = "o180214037"
        kullancı_paralosı = "Tayyonn1!"
        kullanıcı_Adı_pathx = '//*[@id="txtLogin"]'
        kullancı_paralosı_pathx = '//*[@id="txtPassword"]'
        login_pathx = '//*[@id="btnLogin"]'
        kullanıcı_Adı_element = browser.find_element_by_xpath(kullanıcı_Adı_pathx)
        kullancı_paralosı_element = browser.find_element_by_xpath(kullancı_paralosı_pathx)
        login_element = browser.find_element_by_xpath(login_pathx)
        kullanıcı_Adı_element.send_keys(kullanıcı_Adı)
        kullancı_paralosı_element.send_keys(kullancı_paralosı)
        login_element.click()
        c= get_audio()
        if "close page" in c:
            browser.close()
    elif text in cm.facebook:
        driver_path = control_input.browserControlPath
        browser = webdriver.Chrome(executable_path=driver_path)
        speak(random.choice(cm.facebook_return))
        browser.get("https://facebook.com")    
        e = get_audio()
        if "close page" in e:
            browser.close()
    elif text in cm.youtube:
        driver_path = control_input.browserControlPath
        browser = webdriver.Chrome(executable_path=driver_path)
        speak(random.choice(cm.youtube_return))
        speak("Switching to full screen mode")
        browser.maximize_window()
        browser.get("https://youtube.com")  
        d = get_audio()
        if "close page" in d:
            browser.close()
    elif text in cm.youtube_mp3_page:
        driver_path = control_input.browserControlPath
        browser = webdriver.Chrome(executable_path=driver_path)
        speak(random.choice(cm.youtube_mp3_page_return))
        browser.get("https://www.y2mate.com/tr/youtube-mp3/oKPJwNURr44")
        e = get_audio()
        if "close page" in e:
            browser.close()
    if "screenshot" in text:
        speak("screenshot saved")
        pyautogui.screenshot(control_input.screenshotSave)
        os.system(control_input.screenshotSave)
    if "my screen size" in text or"size" in text:
        speak("showing your screen size")
        a = pyautogui.size()
        print(a)
    if text in cm.clear_Screan:
        os.system("cls")
    if "crated Folder" in text or "folder crated" in text:
        speak("file created")
        os.mkdir("TOKYO")
    if "my ip" in text:
        speak("showing your ip address")
        my_ip()
    if text in cm.system_commends:
        speak(random.choice(cm.system_commends_return))
        os.system("start cmd")
    if "shutdown my pc" in text or "shutdown" in text:
        speak("the computer will shut down in a few minutes")
        speak("shutting down tokyo")
        os.system("shutdown -s -t 5")   
    if "show password wifi" in text:
        tts2 = gTTS(text="Computer Connected Previously Showing Wifi Passwords",lang='en')
        tts2.save("audio.mp3")
        playsound.playsound("daha.mp3")
        os.remove("audio.mp3")
        sub.call("netsh wlan show profiles")
        print(R+"""

                    Please Use This Command : netsh wlan show profiles "Network_Name" key=clear

                    [ör:/ netsh wlan show profiles TayyonNetwork key=clear]


             """)
        time.sleep(5)
        os.system("start cmd ")

#StartListing
wake = "tokyo"
def JarvisListening():
    while True:
        text = get_audio()
        if text.count(random.choice(wake)) > 0:
            TokyoSounds = ["My dear","Yes baby","Hello, I am Tokyo. Your personal Assistant.","Hello","I am Here","Sir","I'm listening","What do you want","I'm waiting","hi baby i am tokyo"]
            mix3= random.choice(TokyoSounds)
            SpeakMethod(mix3)
            while True:
                text = GetAudio()
                jarvis(text)


#ClearScreen (cmd)
os.system("cls")

func.cmd_size()
func.JarvisStartSpeak()
JarvisListening()
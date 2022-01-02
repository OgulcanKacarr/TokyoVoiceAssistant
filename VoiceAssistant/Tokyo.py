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
import playsound
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
                func.MyAssistan()
            except RequestError:
                error=["I dont Understand!","I can not understand!","can you repeat!","I did not understand what you have said!","i don't think i understand","I did not hear","say it again"]
                mix = random.choice(error)
                time.sleep(0.1)
                print(mix)
                func.MyAssistan()

        return said.lower()

#DoFunc
def Jarvis(text):
    if text in cm.HowAreYou:
        SpeakMethod(random.choice(cm.HowAreYouAnswer))
    if text in cm.YourName:
        speak(random.choice(cm.YourNameAnswer))
    if text in cm.SystemCommends:
        SpeakMethod(random.choice(cm.SystemCommendsReturn))
        os.system("start cmd")
    if text in cm.Close:
        SpeakMethod(random.choice(cm.CloseReturn))
        playsound.playsound("C:\\Users\\oglcn\\Desktop\\VoiceAssistant\\Sounds\\shutdown_hacker.mp3")
        quit()
    if text in cm.OpenVideoProgram:
        SpeakMethod(random.choice(cm.OpenVideoProgramReturn))
        os.startfile([paths.ObsPath])
    if "where is" in text:
        #DriverPath = os.path.abspath("chromedriver_win32.exe")
        DriverPath = "C:\\Users\\oglcn\\Desktop\\chromedriver.exe"
        browser = webdriver.Chrome(executable_path=DriverPath)
        data = text.split(" ")
        LocationURL = "https://www.google.com/maps/place/" + str(data[2])
        SpeakMethod("of course i am researching immediately " + data[2] + " is.")
        mapsArgs = LocationURL
        browser.get(mapsArgs)
    if text in cm.Music:
        MusicPaths = paths.MusicPath
        SpeakMethod(random.choice(cm.MusicReturn))
        os.startfile(MusicPaths)  
    if text in cm.Word:
        SpeakMethod("Opening Microsoft Word")
        os.startfile(paths.WordPath)
    if text in cm.OpenMyGame:
        SpeakMethod(paths.GameOneName)
        func.OpenGameOne()
    if text in cm.MyGame:
        SpeakMethod(paths.GameTwoName)
        func.OpenGameTwo()
    if text in cm.Clock:
        SpeakMethod(datetime.now().strftime('%H:%M:%S'))
        ax = datetime.now().strftime('%H:%M:%S')
        print(ax)
    elif text in cm.Search:
        SpeakMethod("what search google")
        LookingFor = GetAudio("what do you want me to call")
        url = "https://www.google.com/search?q=" + LookingFor
        webbrowser.get().open(url)
        SpeakMethod("I found for your request") 
    elif text in cm.OpenGoogle:
        #DriverPath = os.path.abspath("chromedriver_win32.exe")
        DriverPath = "C:\\Users\\oglcn\\Desktop\\chromedriver.exe"
        browser = webdriver.Chrome(executable_path=DriverPath)
        SpeakMethod("google is opening")
        browser.get("https://google.com")

    elif text in cm.MyFacebook: 
           #DriverPath = os.path.abspath("chromedriver_win32.exe")
        DriverPath = "C:\\Users\\oglcn\\Desktop\\chromedriver.exe"
        browser = webdriver.Chrome(executable_path=DriverPath)
        SpeakMethod(random.choice(cm.MyFacebookReturn))
        browser.get("https://facebook.com")
        email_xpath=  '//*[@id="email"]' 
        password_Xpath= '//*[@id="pass"]' 
        login_button_xpath= '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button'  
        PageUser = paths.FacebookEmail
        PagePassword = paths.FacebookPassword
        email_element = browser.find_element_by_xpath(email_xpath)
        password_element = browser.find_element_by_xpath(password_Xpath)
        login_button_element = browser.find_element_by_xpath(login_button_xpath)
        email_element.send_keys(PageUser)
        password_element.send_keys(PagePassword)
        login_button_element.click()

    elif text in cm.MyShcoolPage:
        DriverPath = "C:\\Users\\oglcn\\Desktop\\chromedriver.exe"
        browser = webdriver.Chrome(executable_path=DriverPath)
        browser.get("https://ubys.ibu.edu.tr/")
        PageUser = paths.SchoolPageUser
        PagePassword = paths.SchoolPagePassword
        UsernamePathx = '//*[@id="username"]'
        UserPasswordPathx = '//*[@id="password"]'
        LogainPathx = '//*[@id="loginForm"]/div[3]/div[1]/button'
        UsernameElement = browser.find_element_by_xpath(UsernamePathx)
        UserPasswordElement = browser.find_element_by_xpath(UserPasswordPathx)
        LoginElement = browser.find_element_by_xpath(LogainPathx)
        UsernameElement.send_keys(PageUser)
        UserPasswordElement.send_keys(PagePassword)
        LoginElement.click()
    elif text in cm.Facebook:
           #DriverPath = os.path.abspath("chromedriver_win32.exe")
        DriverPath = "C:\\Users\\oglcn\\Desktop\\chromedriver.exe"
        browser = webdriver.Chrome(executable_path=DriverPath)
        SpeakMethod(random.choice(cm.FacebookReturn))
        browser.get("https://facebook.com")    
    elif text in cm.Youtube:
           #DriverPath = os.path.abspath("chromedriver_win32.exe")
        DriverPath = "C:\\Users\\oglcn\\Desktop\\chromedriver.exe"
        browser = webdriver.Chrome(executable_path=DriverPath)
        SpeakMethod(random.choice(cm.YoutubeReturn))
        SpeakMethod("Switching to full screen mode")
        browser.maximize_window()
        browser.get("https://youtube.com")  
    if "screenshot" in text:
        SpeakMethod("screenshot saved")
        pyautogui.screenshot(paths.ScreenshotSave)
        os.system(paths.ScreenshotSave)
    if "my screen size" in text or"size" in text:
        SpeakMethod("showing your screen size")
        a = pyautogui.size()
        print(a)
    if text in cm.ClearScrean:
        os.system("cls")
    if text in cm.FolderCreate:
        SpeakMethod(random.choice(cm.FolderReturn))
        os.mkdir("New Folder")
    if text in cm.IP:
        SpeakMethod(random.choice(cm.IPReturn))
        func.MyIp()
    if text in cm.ClosePC:
        SpeakMethod(random.choice(cm.ClosePCReturn))
        SpeakMethod("shutting down tokyo")
        os.system("shutdown -s -t 5")   


#StartListing
wake = "tokyo"
def JarvisListening():
    while True:
        text = GetAudio()
        if text.count(random.choice(wake)) > 0:
            TokyoSounds = ["My dear","Yes baby","Hello, I am Tokyo. Your personal Assistant.","Hello","I am Here","Sir","I'm listening","What do you want","I'm waiting","hi baby i am tokyo"]
            mix3= random.choice(TokyoSounds)
            playsound.playsound("C:\\Users\\oglcn\\Desktop\\VoiceAssistant\\Sounds\\cyberpunk_message.mp3")
             
            SpeakMethod(mix3)
            while True:
                text = GetAudio()
                Jarvis(text)


def JarvisStartSpeak():     
    playsound.playsound("C:\\Users\\oglcn\\Desktop\\VoiceAssistant\\Sounds\\jarvis_on.mp3")     
    starting_sounds = ["Hello, system is starting","The system is starting","loading system","preparing system","system is being edited"]
    mix2 = random.choice(starting_sounds)
    SpeakMethod(mix2)



func.InstallBrowser()
os.system("cls")
func.CMDSize()
JarvisStartSpeak()
JarvisListening()
from gtts import gTTS
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import playsound
import speech_recognition as sr
import random
import getpass
import pyjokes

def speak(text):
    language = 'en'
    speech = gTTS(text = text,lang = language,slow = False)
    speech.save("speak.mp3")
    print(text)
    playsound.playsound("speak.mp3",True)
    os.system("rm speak.mp3")
driver = ""
command =""
text = ""
def getaudio():
    global text
    global command
    r = sr.Recognizer()	
    with sr.Microphone() as source:
        audio = r.adjust_for_ambient_noise(source)
        print("speak")
        audio = r.listen(source)
    list = ["Excuse me?","Sorry,I couldn't get you","Can you repeat what you just said","pardon"]
    k = random.choice(list)
    try:
        print("                                                                                                                                                                                   " + r.recognize_google(audio))
	text = r.recognize_google(audio)
        command = r.recognize_google(audio).lower()

    except sr.UnknownValueError:
        speak(k)
        getaudio()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def open_something():
    global command
    global driver
    if("google" in command):
        speak("What Can I google for you?")
        getaudio()
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")
        search = driver.find_element_by_name("q")
        search.send_keys(command)
        search.send_keys(Keys.RETURN)
    
    elif("spotify" in command):
        os.system("spotify")

    elif("youtube" in command):
        speak("What do you want to search on youtube?")
        getaudio()
        driver = webdriver.Chrome()
        driver.get("https://youtube.com/")
        search = driver.find_element_by_id("search")
        search.send_keys(command)
        search.send_keys(Keys.RETURN)
        
    elif(("whatsapp" or "watsapp") in command):
        driver = webdriver.Chrome()
	driver.get("https://web.whatsapp.com/")

    elif("gmail" in command):
        driver = webdriver.Chrome()
	driver.get("https://accounts.google.com/")
    
    elif("lms" in command):
        driver = webdriver.Chrome()
        driver.get("https://lms.iiitb.ac.in/moodle/login/index.php")
        username = driver.find_element_by_name("username")
        speak("Please enter your username")
        username.send_keys(raw_input("Username: "))
        speak("Please enter your password")
        password = driver.find_element_by_id("password")
        password.send_keys(getpass.getpass())
        username.send_keys(Keys.RETURN)
    elif("facebook" in command):
        driver = webdriver.Chrome()
	driver.get("https://www.facebook.com/")
        username = driver.find_element_by_name("email")
        speak("Please enter your username")
        username.send_keys(raw_input("Username: "))
        speak("Please enter your password")
        password = driver.find_element_by_id("pass")
        password.send_keys(getpass.getpass())
        password.send_keys(Keys.RETURN)

def play():
    global command
    global driver
    if("music" in command):
	speak("From where do you want me to play music?")
	getaudio()
	if("spotify" in command):
	    os.system("spotify")
	elif("youtube" in command):
	    speak("What song/music do you want me to play?")
            getaudio()
            driver = webdriver.Chrome()
            driver.get("https://youtube.com/")
            search = driver.find_element_by_id("search")
            search.send_keys(command)
            search.send_keys(Keys.RETURN)
    if("video" in command):
       	speak("What video do you want me to play?")
        getaudio()
        driver = webdriver.Chrome()
        driver.get("https://youtube.com/")
        search = driver.find_element_by_id("search")
        search.sendkeys(command)
        search.send_keys(Keys.RETURN)

def send():
    global command
    global driver
    if("message" in command):
	if("facebook" in command):
            driver = webdriver.Chrome()
            driver.get('https://www.facebook.com/')
            username = driver.find_element_by_id('email')
            speak("Please enter your username after I stop")
            username.send_keys(raw_input())
            password = driver.find_element_by_id("pass")
            speak("Plase enter your password after I stop")
            password.send_keys(getpass.getpass())
            password.send_keys(Keys.RETURN)
        elif("whatsapp" or "watsapp" in command):
            driver = webdriver.Chrome()
            driver.get("https://web.whatsapp.com/")

def find():
    global command
    global driver
    driver = webdriver.Chrome()
    if("eat" in command):
        driver.get("https://www.google.com/search?q=places+to+eat+nearby")
    elif("fun" in command):
        driver.get("https://www.google.com/search?q=fun+nearby")
    
def navigate():
    global driver
    global command
    speak("What is your starting point")
    getaudio()
    command1 = command
    speak("Where do you want to go?")
    getaudio()
    command2 = command
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/maps/dir/" + command1 + "/" + command2)

k = 0

def start():
    global driver
    global k
    global command
    speak("Hello, I am Heisenberg, what can I do for you?")
    while(k == 0):
        getaudio()
        if("open" in command):
            open_something()
        elif(("where am i" or "can you spot my location" or "find me") in command):
            driver = webdriver.Chrome()
            driver.get("https://www.google.com/maps/")

        elif(("i am bored" or "bored") in command):
            speak("Do you want to play a boring game?")
            getaudio()
            if(("yes" or "yup" or "yeah" or "yup") in command):
                driver = webdriver.Chrome()
                driver.get("https://www.boredbutton.com/")
            else:
                driver = webdriver.Chrome()
                driver.get("https://lifehacks.io/what-to-do-when-your-bored/")
        elif(("what song is this" or "identify this song" or "identify the song") in command):
            driver = webdriver.Chrome()
            driver.get("https://www.acrcloud.com/identify-songs-music-recognition-online/#record-div")
            button = driver.find_element_by_id("record")
            button.click()
        elif("play" in command):
            play()
        elif(("joke" or "tell me a joke") in command):
            speak(pyjokes.get_joke())
        elif("send" in command):
            send()
        elif(("hey" or "hi") in command):
            speak("Hey,what can I do for you?")
        elif("how are you" in command):
            speak("I'm fine")
        elif("who are you" in command):
            speak("Hello, I am Heisenberg")
        elif("search" in command):
            driver = webdriver.Chrome()
            driver.get("https://www.google.com/search?q=" + command)
	elif(("find" or "nearby") in command):
            find()
        elif(("read" or "news" )in command):
            driver = webdriver.Chrome()
            driver.get("https://news.google.com/")
    	elif("navigate" in command):
            navigate()
        elif(("close" or "bye bye" or "bye bye bye" or "seeya" or "see you next time" or "until next time") in command):
            k = 1
        else:
	    driver = webdriver.Chrome()
	    driver.get("https://www.google.com/search?q=" + command)



start()

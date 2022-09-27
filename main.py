import simpleaudio as sa # pipwin install simpleaudio
import speech_recognition as sr   # pip install SpeechRecognition
# pip install pipwin ----> pipwin install PyAudio

import RPi.GPIO as GPIO

r = sr.Recognizer() #initialize recognizer
#initialize audios
ansprechbar = "audios\\ansprechbar.wav"
stabile_seitenlage = "audios\\stabile-seitenlage.wav"
blut = "audios\\blut.wav"
wiederholen = "audios\\wiederholen.wav"
lehrkraft = "audios\\lehrkraft.wav"
atmen = "audios\\atmen.wav"
strom_feuer = "audios\\strom_feuer.wav"
einleitung = "audios\\einleitung.wav"
notaus = "audios\\notaus.wav"
sekretariat = "audios\\sekretariat.wav"
wiederbeleben = "audios\\wiederbeleben.wav"
umgebung = "audios\\umgebung.wav"
beruhigen = "audios\\beruhigen.wav"
blutung_abdruecken = "audios\\blutung_abdruecken.wav"
lehrkraft_warten = "audios\\lehrkraft_warten.wav"
lied_hlw = "audios\\lied-hlw.wav"
#
MyText = "START"

def playAudio(MyAudio):
    wave_obj = sa.WaveObject.from_wave_file(MyAudio) #take audio
    play_obj = wave_obj.play() #play audio
    play_obj.wait_done()

def checkStop(MyText):
    if MyText.lower() == "stop":
        exit(100)

def getAnswer():
    MyText = "START"
    with sr.Microphone() as source2:  # micro as input
        r.adjust_for_ambient_noise(source2, duration=0.2)  # adjust to backround noises
        audio2 = r.listen(source=source2, phrase_time_limit=3)  # listen to input(user talk)
    try:
        MyText = r.recognize_google(audio2, language="de-DE")  # using google to recognize, german as language
        MyText = MyText.lower()
        print(MyText)
        checkStop(MyText)
    except Exception as e:  # errorhandling
        print(e)
    wdh = True
    while wdh:
        if MyText == "":
            MyText = "ERROR"

        if MyText == "ja":
            return "ja"
        elif MyText == "nein":
            return "nein"
        else:
            print("wdhx")
            playAudio(wiederholen)
            with sr.Microphone() as source2:  # micro as input
                r.adjust_for_ambient_noise(source2, duration=0.2)  # adjust to backround noises
                audio2 = r.listen(source=source2, phrase_time_limit=3)  # listen to input(user talk)
            try:
                MyText = r.recognize_google(audio2, language="de-DE")  # using google to recognize, german as language
                MyText = MyText.lower()
                print(MyText)
                checkStop(MyText)
            except Exception as e:
                print(e)

                
# START
GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def startDSP():

    #EINLEITUNGSAUDIO
    playAudio(einleitung)
    ##########
    #IST EINE LEHRKRAFT ANWESEND?
    ##########
    playAudio(lehrkraft)

    if getAnswer() == "nein":
        playAudio(sekretariat)

    playAudio(strom_feuer)

    if getAnswer() == "ja":
        playAudio(notaus)

    playAudio(ansprechbar)

    if getAnswer() == "ja":
        playAudio(beruhigen)
        playAudio(blut)
        if getAnswer() == "ja":
            playAudio(blutung_abdruecken)
        playAudio(lehrkraft_warten)
    elif getAnswer() == "nein":
        playAudio(atmen)
        if getAnswer() == "ja":
            playAudio(stabile_seitenlage)
        elif getAnswer() == "nein":
            while 1 == 1:
                playAudio(lehrkraft_warten)
                playAudio(lied_hlw)

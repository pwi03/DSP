import simpleaudio as sa # pipwin install simpleaudio
import speech_recognition as sr   # pip install SpeechRecognition
# pip install pipwin ----> pipwin install PyAudio

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
MyText = ""
#functions for questions + textanalysis
def playAudio(MyAudio):
    wave_obj = sa.WaveObject.from_wave_file(MyAudio) #take audio
    play_obj = wave_obj.play() #play audio
    play_obj.wait_done() #wait for end
def checkStop(MyText):
    if MyText == "stopp":
        print("Programm durch 'Stopp' beendet.")
        exit(5)
#EINLEITUNGSAUDIO
playAudio(einleitung)
##########
#IST EINE LEHRKRAFT ANWESEND?
##########
playAudio(lehrkraft)
with sr.Microphone () as source2: # micro as input
    r.adjust_for_ambient_noise(source2, duration=0.2) #adjust to backround noises
    audio2 = r.listen(source=source2) # listen to input(user talk)
try:
    MyText = r.recognize_google(audio2, language = "de-DE") #using google to recognize, german as language
    MyText = MyText.lower()
    print(MyText)
    checkStop(MyText)
except Exception as e: #errorhandling
    MyText = "hallo"
wdh = True
while wdh:
    if MyText == "ja":
        wdh = False
    elif MyText == "nein":
        playAudio(sekretariat)
        wdh = False
    else:
        playAudio(wiederholen)
        with sr.Microphone () as source2: # micro as input
            r.adjust_for_ambient_noise(source2, duration=0.2) #adjust to backround noises
            audio2 = r.listen(source=source2) # listen to input(user talk)
        try:
            MyText = r.recognize_google(audio2, language = "de-DE") #using google to recognize, german as language
            MyText = MyText.lower()
            print(MyText)
            checkStop(MyText)
        except Exception as e:
            MyText = "hallo"
##########
#KONTAKT ZU STROM ODER FEUER?
##########
playAudio(strom_feuer)
with sr.Microphone () as source2: # micro as input
    r.adjust_for_ambient_noise(source2, duration=0.2) #adjust to backround noises
    audio2 = r.listen(source=source2) # listen to input(user talk)
try:
    MyText = r.recognize_google(audio2, language = "de-DE") #using google to recognize, german as language
    MyText = MyText.lower()
    print(MyText)
    checkStop(MyText)
except Exception as e:
    MyText = "hallo"
wdh = True
while wdh:
    if MyText == "ja":
        playAudio(notaus)
        wdh = False
    elif MyText == "nein":
        wdh = False
    else:
        playAudio(wiederholen)
        with sr.Microphone () as source2: # micro as input
            r.adjust_for_ambient_noise(source2, duration=0.2) #adjust to backround noises
            audio2 = r.listen(source=source2) # listen to input(user talk)
        try:
            MyText = r.recognize_google(audio2, language = "de-DE") #using google to recognize, german as language
            MyText = MyText.lower()
            print(MyText)
            checkStop(MyText)
        except Exception as e:
            MyText = "hallo"
##########
#IST DIE PERSON ANSPRECHBAR?
##########
playAudio(ansprechbar)
with sr.Microphone () as source2: # micro as input
    r.adjust_for_ambient_noise(source2, duration=0.2) #adjust to backround noises
    audio2 = r.listen(source=source2) # listen to input(user talk)
try:
    MyText = r.recognize_google(audio2, language = "de-DE") #using google to recognize, german as language
    MyText = MyText.lower()
    print(MyText)
    checkStop(MyText)
except Exception as e:
    MyText = "hallo"
answer_ansprechbar = False
wdh = True
while wdh:
    if MyText == "ja":
        answer_ansprechbar = True
        playAudio(beruhigen)
        wdh = False
    elif MyText == "nein":
        answer_ansprechbar = False
        wdh = False
    else:
        playAudio(wiederholen)
        with sr.Microphone () as source2: # micro as input
            r.adjust_for_ambient_noise(source2, duration=0.2) #adjust to backround noises
            audio2 = r.listen(source=source2) # listen to input(user talk)
        try:
            MyText = r.recognize_google(audio2, language = "de-DE") #using google to recognize, german as language
            MyText = MyText.lower()
            print(MyText)
            checkStop(MyText)
        except Exception as e:
            MyText = "hallo"
if answer_ansprechbar:
    playAudio(blut)
    with sr.Microphone () as source2: # micro as input
        r.adjust_for_ambient_noise(source2, duration=0.2) #adjust to backround noises
        audio2 = r.listen(source=source2) # listen to input(user talk)
    try:
        MyText = r.recognize_google(audio2, language = "de-DE") #using google to recognize, german as language
        MyText = MyText.lower()
        print(MyText)
        checkStop(MyText)
    except Exception as e:
        MyText = "hallo"
    wdh = True
    while wdh:
        if MyText == "ja":
            playAudio(blutung_abdruecken)
            playAudio(lehrkraft_warten)
            print("Ende")
            exit(1)
        elif MyText == "nein":
            playAudio(lehrkraft_warten)
            print("Ende")
            exit(1)
        else:
            playAudio(wiederholen)
            with sr.Microphone () as source2: # micro as input
                r.adjust_for_ambient_noise(source2, duration=0.2) #adjust to backround noises
                audio2 = r.listen(source=source2) # listen to input(user talk)
            try:
                MyText = r.recognize_google(audio2, language = "de-DE") #using google to recognize, german as language
                MyText = MyText.lower()
                print(MyText)
                checkStop(MyText)
            except Exception as e:
                MyText = "hallo"
else:
    playAudio(atmen)
    with sr.Microphone () as source2: # micro as input
        r.adjust_for_ambient_noise(source2, duration=0.2) #adjust to backround noises
        audio2 = r.listen(source=source2) # listen to input(user talk)
    try:
        MyText = r.recognize_google(audio2, language = "de-DE") #using google to recognize, german as language
        MyText = MyText.lower()
        print(MyText)
        checkStop(MyText)
    except Exception as e:
        MyText = "hallo"
    wdh = True
    while wdh:
        if MyText == "ja":
            playAudio(stabile_seitenlage)
            playAudio(lehrkraft_warten)
            print("Ende")
            exit(1)
        elif MyText == "nein":
            playAudio(lehrkraft_warten)
            playAudio(wiederbeleben)
            while 1 == 1:
                playAudio(lied_hlw)
print("Ende")
exit(-1)
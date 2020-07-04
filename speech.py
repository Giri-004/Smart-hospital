# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:12:22 2019

@author: Giri
"""
import speech_recognition as s_r
import pyttsx3
import os

Speech1 = s_r.Recognizer()

try:
    engine=pyttsx3.init()
except ImportError:
    print("Requested driver is not found")
except RuntimeError:
    print("Driver fails to initialise")

voices = engine.getProperty("voices")

# for voice in voices:
# print(voice.id)

engine.setProperty("voices", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0")
rate = engine.getProperty("rate")
engine.setProperty("rate", rate - 50)

engine.setProperty('voice', voices[0].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 5.0)


# engine.say("hello  this is current trial code")
 #engine.runAndWait();

def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait();


def read_voice_cmd():
    voice_text = ""
    print ("Listening AI....")
    with s_r.Microphone() as voice_source:
        audio = Speech1.listen(voice_source)

    try:
        voice_text = Speech1.recognize_google(audio)
    except s_r.UnknownValueError:
        pass
    except s_r.RequestError as e:
        print("Network Problem or Server Issues..")
    return voice_text



if __name__ == "__main__":
    speak_text_cmd("Hello Sir,I'M your Assistant")
    print("Hello Sir,I'M your Assistant")

    while True:
        voice_note = read_voice_cmd()

        print ("cmd : {}".format(voice_note))
        if "hello" in voice_note:
            speak_text_cmd("Hello Sir,How can i help you")
            continue
        elif "" in voice_note:
            os.system("explorer C:\\ '{}'".format(voice_note.replace("Open ", "")))
            continue
        elif "bye" in voice_note:
            speak_text_cmd("By Sir,happy to help you ,Good day.")
            exit()

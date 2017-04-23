import os
import speech_recognition as sr
from Game import feedback

def recognize_speech():
    r = sr.Recognizer()
    text = ''
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        save_audio(audio)
        
    # recognize speech using Microsoft Bing Voice Recognition
    BING_KEY = ""  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
    try:
        text = r.recognize_bing(audio, key=BING_KEY)
        print(text)
    except sr.UnknownValueError:
        print("Microsoft Bing Voice Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))    
    return text 

# saves a given audio file in WAV format
def save_audio(audio):
    i = 0
    while os.path.exists("game_audio_"+ str(i) + ".wav"):
        i += 1
    with open("game_audio_"+ str(i) + ".wav", "wb") as f:
        f.write(audio.get_wav_data())

text = recognize_speech()


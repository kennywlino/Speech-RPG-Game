import os
import speech_recognition as sr
import coloured_feedback
import time

# recognizes the speech of a user using Google Speech Recognition
def recognize_speech(enemy):
    r = sr.Recognizer()
    text = ''
    with sr.Microphone() as source:
        print("Think about the word in the blank and get ready to say the sentence!")
        start = False
        while start != True:
            time.sleep(10)
            start = True
        print("Say the sentence now!")
        audio = r.listen(source)
        # save_audio(audio)

    # recognize speech using Google Speech Recognition
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
       text = r.recognize_google(audio)
    #we make the call to print it with colors
       coloured_feedback.recolor(text,enemy) # otherwise print(text)
       print("\n")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return text

#     # recognize speech using Microsoft Bing Voice Recognition
#     BING_KEY = "474158a66c384965b039e414cbb00b66"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
#     try:
#         text = r.recognize_bing(audio, key=BING_KEY)
#         print(text)
#     except sr.UnknownValueError:
#         print("Microsoft Bing Voice Recognition could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
#     return text

# saves a given audio file in WAV format
def save_audio(audio):
    i = 0
    while os.path.exists("game_audio_"+ str(i) + ".wav"):
        i += 1
    with open("game_audio_"+ str(i) + ".wav", "wb") as f:
        f.write(audio.get_wav_data())

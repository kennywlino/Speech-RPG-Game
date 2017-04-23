'''
The module 'feedback' is used to give feedback for a speech processing system
in multiple forms, including ARPAbet, IPA, and text-to-speech

'''
from msspeak import msspeak

# Will probably be best to import modules that convert the text into each form

#     # this function returns the ARPAbet pronunciation of the given text
#     def arpabet(self): 
#         #TODO: Take the given text; for each word in the text
#         # take the word, get the ARPAbet pronunciation and store it in
#         # a string or a list
#         # return the ARPAbet pronunciation for the whole text
#         
#     
#     # this function returns the IPA pronunciation of the given text
#     def ipa(self):
#         #TODO: Take the given text; for each word in the text
#         # take the word, get the IPA pronunciation and store it in
#         # a string or a list
#         # return the IPA pronunciation for the whole text
    
    # this function returns the text to speech of the given text
    # using the Bing Speech system
def tts():
    subscription_key = '474158a66c384965b039e414cbb00b66'
    tts_msspeak = msspeak.MSSpeak(subscription_key,'/tmp/')
    output_filename = tts_msspeak.speak("This is the text I will speak to you", "en-US")
    # output_filename = tts_msspeak.speak(text, "en-US", "male", "audio-16khz-128kbitrate-mono-mp3")

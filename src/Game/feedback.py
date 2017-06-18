# -*- coding: utf-8 -*-

'''
The module 'feedback' is used to give feedback for a speech processing system
in multiple forms, including ARPAbet, IPA, and text-to-speech

The IPA Generator is taken from the following:
IPA GENERATOR 2.0
Author: Michael Phillips
Last update: 3/24/17
A simple script for converting English words into IPA notation.
The conversion relies on the CMU Phonetic Dictionary. As such, if a word entry is missing, the word is not converted
to IPA, and the original is returned. There are sometimes more than one correct pronunciations of a word, and so
this program can return either just the top result or every possible combination of results.
'''

import nltk
import re

# this function returns the ARPAbet pronunciation of the given text
def arpabet(sentence):
	arpabet = nltk.corpus.cmudict.dict() #It imports the dictionary that contains words translated to arpabet
	sentence = sentence.lower() #It converts the sentence to lower-case
	arpabet_return = [] #The list stores the arpabet phonemes
	arpabet_text = '' #It will store the final sentence translated to arpabet
	for word in sentence.split(): #for each word in the sentence
		try: #if it is in the dictionary
			arpabet_pronunciation=arpabet[word][0] #It stores the phonemes of the word
			for phoneme in arpabet_pronunciation:
				phoneme=re.sub("u|[0-9]","",phoneme) #It deletes "u" and numbers
				arpabet_return.append(str(phoneme)) #It appends the phoneme converted to string to the list
			arpabet_return.append(' - ') #It adds a hyphen between words
		except:
			arpabet_return.append(word) #If the word is not the dictionary, it prints the plain word.
	arpabet_text=arpabet_text.join(arpabet_return).rstrip(' - ') #It joins all the phonemes and deletes the final hyphen
	return(arpabet_text) #It returns the final string with all the phonemes

# this function returns the IPA pronunciation of the given text
def ipa(sentence):
    """takes the input sentence and returns the IPA notations """
    list_of_lines = []
    sentence_lowered = sentence.lower().split(" ")
    ipa = convert(sentence_lowered, retrieve='TOP')
    if type(ipa) == list: # if retrieve=ALL
        if len(ipa) > 1:
            print("List of possible transcriptions: ")
            for sent_num in range(len(ipa)):
                print(str(sent_num + 1) + ". " + ipa[sent_num])  # print list of numbered results
        else:
            print(ipa[0]) # when ALL is used but there's only one result
    else:
        return(ipa)

def cmu_words():
    """returns a dictionary of words from the CMU dictionary and their phonetic notation"""
    cmu_file = open('CMU_dict.txt', 'r+')  # assumes the file is in the same directory!
    words = []
    phonetics = []
    for line in cmu_file.readlines():
        words.append(line.split()[0])
        phonetics.append(' '.join(line.split()[1:]).split('%'))
    cmu_dict = {w: p for w, p in zip(words, phonetics)}
    return cmu_dict

def get_cmu(user_in):
    """converts the user's input to the CMU phonetics, returns a list of all entries found for each word"""
    cmu_list = []  # a list of CMU phonetic representations for the input words
    user_in = [re.sub("[:;,\.\?\"!]", "", word) for word in user_in]
    for word in user_in:
        if word in word_dict:
            # add the CMU phonetic representation(s) to the list
            cmu_list.append(word_dict[word])
        else:
            # If the word cannot be found in the CMU dictionary, we will ignore it
            cmu_list.append(['__IGNORE__' + word])
    return cmu_list

def cmu_to_ipa(cmu_list):
    """converts the CMU word lists into IPA transcriptions"""
    symbols = {"a": "ə", "ey": "e", "aa": "ɑ", "ae": "æ", "ah": "ə", "ao": "ɔ", "aw": "aʊ", "ay": "aɪ", "ch": "ʧ",
               "dh": "ð", "eh": "ɛ", "er": "ər", "hh": "h", "ih": "ɪ", "jh": "ʤ", "ng": "ŋ",  "ow": "oʊ", "oy": "ɔɪ",
               "sh": "ʃ", "th": "θ", "uh": "ʊ", "uw": "u", "zh": "ʒ", "iy": "i", "y": "j"}
    ipa_list = []  # the final list of IPA tokens to be returned
    for word_list in cmu_list:
        ipa_word_list = []  # the word list for each word
        for word in word_list:
            word = re.sub("[0-9]", "", word)  # ignore stress markings for now
            ipa_form = ''
            if word.startswith("__IGNORE__"):
                ipa_form = word.replace("__IGNORE__", "")
            else:
                for piece in word.split(" "):
                    if piece in symbols:
                        ipa_form += symbols[piece]
                    else:
                        ipa_form += piece
            ipa_word_list.append(ipa_form)
        ipa_list.append(list(set(ipa_word_list)))
    return ipa_list

def get_top(ipa_list):
    """Returns only the one result for a query. If multiple entries for words are found, only the first is used."""
    return ' '.join([word_list[-1] for word_list in ipa_list])

def get_all(ipa_list):
    """utilizes an algorithm to discover and return all possible combinations of IPA transcriptions"""
    final_size = 1
    for word_list in ipa_list:
        final_size *= len(word_list)
    list_all = ["" for s in range(final_size)]
    for i in range(len(ipa_list)):
        if i == 0:
            swtich_rate = final_size / len(ipa_list[i])
        else:
            swtich_rate /= len(ipa_list[i])
        k = 0
        for j in range(final_size):
            if (j+1) % int(swtich_rate) == 0:
                k += 1
            if k == len(ipa_list[i]):
                k = 0
            list_all[j] = list_all[j] + ipa_list[i][k] + " "
    final = [sent[:-1] for sent in list_all]
    return final

def get_ipa_list(words_in):
    """returns a list of all the discovered IPA transcriptions for each word"""
    if type(words_in) == str:
        words_in = words_in.lower().split(" ")
    cmu_list = get_cmu(words_in)
    ipa_words = cmu_to_ipa(cmu_list)
    return ipa_words

def isin_cmu(word):
    """checks if a word is in the CMU dictionary. Doesn't strip punctuation.
    If given more than one word, returns True only if all words are present."""
    if type(word) == list or len(word.split(" ")) > 1:
        if type(word)==str:
            word = word.split(" ")
        for w in word:
            if w.lower() not in word_dict:
                return False
        return True
    return word.lower() in word_dict

def convert(user_in, retrieve='TOP'):
    """takes either a string or list of English words and converts them to IPA"""
    if type(user_in) == str:
        user_in = user_in.lower().split(" ")
    cmu_list = get_cmu(user_in)
    ipa_words = cmu_to_ipa(cmu_list)  # converts the CMU phonetic pronunciations to IPA notation
    if retrieve.lower() == 'all':
        ipa_final = get_all(ipa_words)  # also an option
    else:
        ipa_final = get_top(ipa_words)  # gets top by default
    return ipa_final

word_dict = cmu_words()


def return_pronunciation_advice(each_phoneme,IPA_sentence): #returns the pronunciation advice for each phoneme contained in the sentence
	if each_phoneme=="ɪ" in IPA_sentence:
		pronunciation_advice="Relax the mouth and keep sound short."
	if each_phoneme=="æ":
		pronunciation_advice="Keep tongue front & low and jaws apart."
	if each_phoneme=="ʊ":
		pronunciation_advice="Keep Back of tongue high. Lips rounded but relaxed. Short."
	if each_phoneme=="ɔ":
		pronunciation_advice="Tongue low, back & fixed. Jaws together."
	if each_phoneme=="ɜ":
		pronunciation_advice="Fix tongue in central position. Long."
	if each_phoneme=="əʊ":
		pronunciation_advice="Tongue central. Then tightly round lips."
	if each_phoneme=="b":
		pronunciation_advice="Voiced. Vibration. Trap air with lips."
	if each_phoneme=="v":
		pronunciation_advice="Voiced. Friction with top teeth & bottom lip."
	if each_phoneme=="ð":
		pronunciation_advice="Voiced. Friction. Tongue between teeth."
	if each_phoneme=="d":
		pronunciation_advice="Tip of tongue behind top teeth."
	if each_phoneme=="k":
		pronunciation_advice="Voiceless stop: back of tongue to back roof."
	if each_phoneme=="s":
		pronunciation_advice="Voiceless: tip of tongue behind top teeth. Friction."
	if each_phoneme=="ʃ":
		pronunciation_advice="Voiceless. Friction. Front of tongue to palate."
	if each_phoneme=="h":
		pronunciation_advice="Quickly push air from throat out of mouth."
	if each_phoneme=="n":
		pronunciation_advice="Tongue touches alveolar ridge. Nasal."
	if each_phoneme=="ŋk":
		pronunciation_advice="Back of tongue to back roof. Nasal."
	if each_phoneme=="ŋ":
		pronunciation_advice="Voiced stop: back of tongue to back roof."
	if each_phoneme=="j":
		pronunciation_advice="Glide /j/(i:) the tongue quickly to next sound."
	if each_phoneme=="w":
		pronunciation_advice="Start with lips tightly rounded. Unround & glide."
	if each_phoneme=="ʤ":
		pronunciation_advice="Voiced: Tip to alveolar. Front to palate."
	return(pronunciation_advice)

def return_pronunciation_advice_list(phonemes_IPA,IPA_sentence): #returns a list with all the pronunciation advices that the sentence needs
	pronunciation_advice_list=[]
	for each_phoneme in phonemes_IPA:
		if each_phoneme in IPA_sentence:
			pronunciation_advice=return_pronunciation_advice(each_phoneme,IPA_sentence)
			pronunciation_advice_complete="The following information may help you to pronounce the phoneme /"+ each_phoneme +"/:\n\t"+pronunciation_advice
			pronunciation_advice_list.append(pronunciation_advice_complete)

	return(pronunciation_advice_list)

def minimal_pairs_advice(sentence, IPA_sentence):
	phonemes_IPA=("ɪ","æ","ʊ","ɔ","ɜ","əʊ","b","v","ð","k","s","ʃ","h","n","ŋk","ŋ","j","w","ʤ") #list of phonemes
	advice_final_list=return_pronunciation_advice_list(phonemes_IPA,IPA_sentence) #get the total advices for the specific sentence
	print("This is the advice we can give you to pronunce the sentence: \n" + sentence)
	print(IPA_sentence + "\n")
	for each_advice in advice_final_list:
			print(each_advice)

    # this function returns the text to speech of the given text
    # using the Bing Speech system
# def tts():
#     subscription_key = '474158a66c384965b039e414cbb00b66'
#     tts_msspeak = msspeak.MSSpeak(subscription_key,'/tmp/')
#     output_filename = tts_msspeak.speak("This is the text I will speak to you", "en-US")
# output_filename = tts_msspeak.speak(text, "en-US", "male", "audio-16khz-128kbitrate-mono-mp3")

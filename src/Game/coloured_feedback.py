# this module prints the sentence the user has said in different colours depending on how much
# coincidence there is between the sentence to be pronounced and the user's sentence.

import sys

class bcolors:
    OKGREEN = '\033[92m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def recolor(text,enemy):
    sentence = enemy.sentence # imports the sentence to be pronounced from enemies.py
    words_sentence = sentence.lower().split()
    words_list = text.lower().split()
    wordcount = 0
    num_words_sentence = len(words_sentence)
    all_words = words_sentence
    for word in words_list:
        if word in words_sentence:
            new_wordcount = wordcount + 1
            wordcount = new_wordcount
    if text.lower() == sentence.lower():
        sys.stdout.write(bcolors.OKGREEN +text+ bcolors.ENDC)
    elif wordcount > num_words_sentence/2:
        if len(words_list) == len(words_sentence):
            for word in words_list:
                if word == all_words[0]:
                    sys.stdout.write(bcolors.OKBLUE +word+' '+bcolors.ENDC)
                    all_words.pop(0)
                else:
                    sys.stdout.write(bcolors.FAIL+word+' '+bcolors.ENDC)
                    all_words.pop(0)
        else:
            for word in words_list:
                if word in all_words:
                    sys.stdout.write(bcolors.OKBLUE + word + ' ' + bcolors.ENDC)
                    all_words.pop(0)
                else:
                    sys.stdout.write(bcolors.FAIL + word + ' ' + bcolors.ENDC)
                    all_words.pop(0)
    elif wordcount <= num_words_sentence / 2 and wordcount >= 1:
        if len(words_list) == len(words_sentence):
            for word in words_list:
                if word in all_words:
                    sys.stdout.write(bcolors.WARNING + word + ' ' + bcolors.ENDC)
                    all_words.pop(0)
                else:
                    sys.stdout.write(bcolors.FAIL + word +' ' + bcolors.ENDC)
        else:
            for word in words_list:
                if word in all_words:
                    sys.stdout.write(bcolors.WARNING + word + ' ' +bcolors.ENDC)
                    all_words.pop(0)
                else:
                    sys.stdout.write(bcolors.FAIL + word + ' ' + bcolors.ENDC)
                    all_words.pop(0)
    else:
        print(bcolors.FAIL + text + bcolors.ENDC)

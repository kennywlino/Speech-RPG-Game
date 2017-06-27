#this module prints the sentence the user has said in different colours depending on how much coincidence there is between the sentence to be pronounced and the user's sentence.
import sys

class bcolors:
    OKGREEN = '\033[92m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def recolor(text,enemy):
    sentence=enemy.sentence #Here we need to import from enemies.py the sentence to be pronounced
    words_sentence=sentence.lower().split()
    num_words_sentence=len(words_sentence)
    #Here we need to import from speech.py the sentence the user has said
    words_list=text.lower().split()
    wordcount=0
    # for word in words_list:
    #     if word in sentence:
    #         new_wordcount=wordcount+1
    #         wordcount=new_wordcount
    # if wordcount==words_sentence:
    #     (bcolors.OKGREEN +text+ bcolors.ENDC)
    # elif wordcount>words_sentence/2:
    #     for word in words_list:
    #         if word in sentence.lower():
    #             sys.stdout.write(bcolors.OKBLUE +word+' '+bcolors.ENDC)
    #         else:
    #             sys.stdout.write(bcolors.FAIL+word+' '+bcolors.ENDC)
    # elif wordcount<=words_sentence/2 and wordcount>=1:
    #     for word in words_list:
    #         if word in sentence:
    #             sys.stdout.write(bcolors.WARNING +word+' '+ bcolors.ENDC)
    #         else:
    #             sys.stdout.write(bcolors.FAIL+word+' '+bcolors.ENDC)
    # else:
    #     print(bcolors.FAIL +text+ bcolors.ENDC)
    # print('\n')
    for word in words_list:
        if word in words_sentence:
            new_wordcount=wordcount+1
            wordcount=new_wordcount
    if wordcount==num_words_sentence:
        (bcolors.OKGREEN +text+ bcolors.ENDC)
    elif wordcount>num_words_sentence/2:
        for word in words_sentence:
            if word in words_list:
                sys.stdout.write(bcolors.OKBLUE +word+' '+bcolors.ENDC)
            else:
                sys.stdout.write(bcolors.FAIL+word+' '+bcolors.ENDC)
    elif wordcount<=num_words_sentence/2 and wordcount>=1:
        for word in words_sentence:
            if word in words_list:
                sys.stdout.write(bcolors.WARNING +word+' '+ bcolors.ENDC)
            else:
                sys.stdout.write(bcolors.FAIL+word+' '+bcolors.ENDC)
    else:
        print(bcolors.FAIL +text+ bcolors.ENDC)
    print('\n')

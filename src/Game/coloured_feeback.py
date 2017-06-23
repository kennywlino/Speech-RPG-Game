#this module prints the sentence the user has said in different colours depending on how much coincidence there is between the sentence to be pronounced and the user's sentence.
import sys
import enemies

class bcolors:
    OKGREEN = '\033[92m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def coloured_feedback(text):
sentence=enemy.sentence #Here we need to import from enemies.py the sentence to be pronounced
words_sentence=len(sentence.split())
#Here we need to import from speech.py the sentence the user has said
words_list=text.split()
wordcount=0
for word in words_list:
    if word in sentence:
        new_wordcount=wordcount+1
        wordcount=new_wordcount
if wordcount==words_sentence:
    print(bcolors.OKGREEN +text+ bcolors.ENDC)
elif wordcount>words_sentence/2:
    for word in words_list:
        if word in sentence:
            sys.stdout.write(bcolors.OKBLUE +word+' '+bcolors.ENDC)
        else:
            sys.stdout.write(bcolors.FAIL+word+' '+bcolors.ENDC)
elif wordcount<=words_sentence/2 and wordcount>=1:
    for word in words_list:
        if word in sentence:
            sys.stdout.write(bcolors.WARNING +word+' '+ bcolors.ENDC)
        else:
            sys.stdout.write(bcolors.FAIL+word+' '+bcolors.ENDC)
    print('\n')
else:
    print(bcolors.FAIL +text+ bcolors.ENDC)

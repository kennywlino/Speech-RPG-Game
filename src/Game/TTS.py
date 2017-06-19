#install espeak by $sudo apt-get install espeak
import os #this should go at the top of the program, we don't want to import it each time

def tts(sentence): #takes the sentence to be pronounced
	os.system("espeak '{0}'".format(sentence)) #it reads the sentence out loud

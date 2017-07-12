import sys
import nltk
from nltk.corpus import wordnet, brown
import re, random
import _pickle as cPickle

# reads a list of minimal pairs from a file and puts them into a list
# in the format of [[word1, word2]]
# this function should only be used once before the question generation
# to speed up access to the random sentences
def make_min_pair_list():
	mini_file = open("minimal_pairs.txt","r")
	mp_list = []
	lines = mini_file.readlines()
	for line in lines:
		line = line.split()
		mp_list.append(line)
	with open("min_pair_list.txt", "wb") as listFile:
		cPickle.dump(mp_list, listFile)

# returns one random minimal pair set from the minimal pair list
def get_min_pair(mp_list):
	minimal_pair = random.choice(mp_list)
	return minimal_pair

# creates a dictionary that maps [word, [sentences that contain word]]
# this function should only be used once before the question generation
# to speed up access to the random sentences
def make_word_sent_dict(mp_list):
	word_sent_dict = {}
	tokenized_corp = open("tokenized_corpus.txt", "r")
	corp_lines = tokenized_corp.readlines()
	for line in corp_lines:
		tokenized_line = re.findall("[\w]+['|-]*[\w]+", line)
		if len(tokenized_line) > 12: # if sentence is longer than 13 elements
			continue
		for mp in mp_list: # for each minimal pair in the list
			for word in mp: # for each word in the minimal pair
				if word in tokenized_line:
					sent = (' '.join(tokenized_line))
					if word in word_sent_dict:
						word_sent_dict[word].append(str(sent))
					else:
						word_sent_dict[word] = []
						word_sent_dict[word].append(str(sent))
	with open("word_sent_dict.txt", "wb") as dictFile:
		cPickle.dump(word_sent_dict, dictFile)

# gets random sentences with a minimal pair element and returns them in a dictionary
# {word 1: sentence 1, word 2: sentence 2}
def random_sentences(minimal_pair, word_sent_dict):
	word1 = minimal_pair[0]
	word2 = minimal_pair[1]
	sent1 = random.choice(word_sent_dict[word1]) # random sentence for word1
	sent2 = random.choice(word_sent_dict[word2]) # random sentence for word2
	return {word1 : sent1, word2 : sent2}

# decides the test word and reference word to be used in sentence gaps
# returns the words in a list [reference word, test word]
def get_test_word(rand_sents):
	randint = random.randint(0,1)
	min_pair = list(rand_sents.keys())
	test_word = min_pair[randint]
	ref_word = ''
	if (randint == 0):
		ref_word = min_pair[1]
	else:
		ref_word = min_pair[0]
	return [ref_word, test_word]

# finds synonyms, antonyms and word definitions for words in the min pair list
# and stores the information into a dictionary as {word:[syn, ant, def]}
def make_associations_dict(mp_list):
	synonyms=[]
	antonyms=[]
	definition=[]
	associations = {}
	for mp in mp_list:
		for word in mp:
			# stores all synsets in a list
			synsets_word = wordnet.synsets(word)
			for syn in synsets_word:
				for l in syn.lemmas(): # l for lemma
					if (l.name() not in synonyms) & (l.name()!= word) & (word not in l.name()): #to avoid repeating synonyms
						synonyms.append(l.name())
					if l.antonyms():
						if l.antonyms()[0].name() not in antonyms:#to avoid repeating antonyms
							antonyms.append(l.antonyms()[0].name())
			# remove not as close synonyms
			synonyms_cleaned = []
			for synonym in synonyms:
				for syn in wordnet.synsets(synonym):
					try:
						# compare the similarity between the synonym and the first sense of the mini.pair element
						simi = syn.wup_similarity(synsets_word[0])
						# lower score equals higher similarity
						if simi < 0.25:
							synonyms_cleaned.append(syn.lemmas()[0].name())
					except: continue
			synonyms_cleaned = list(set(synonyms_cleaned))
			# get the definition of the minimal pair
			definition = synsets_word[0].definition()
			# returns a list containing synonyms, antonyms and definition
			print(word)
			print(synsets_word)
			associations[word] = []
			associations[word].extend([synonyms_cleaned, antonyms, definition])
	with open("associations.txt", "wb") as dictFile2:
	 	cPickle.dump(associations, dictFile2)

def output(sentences, ref_and_test_word, associations):
	# the class is used to highlight minimal pairs in the sentences
	class bcolors:
		OKGREEN = '\033[92m'
		ENDC = '\033[0m'
	test_word = ref_and_test_word[1]
	ref_word = ref_and_test_word[0]
	ref_sent = sentences[ref_word]
	# creates a gap in the the test sentence containing the test word from the mp
	test_sent = sentences[test_word]
	# creates a list of associations (synonyms, antonyms, word definition) for the first minimal pair element
	word_info = associations[test_word] # returns the associated def, syns, ants
	# creates the output that user will see
	print("In the first sentence, the word in green should help you guess "
	"the missing word in the next one. Clue: they are almost twins! \n")
	ref_sent_split = ref_sent.split(' ')
	#print(words1)
	counter = 0
	for i, word in enumerate(ref_sent_split):
		if word == ref_word:
			print("1. " + ' '.join(ref_sent_split[:i]) + " " +
			str(bcolors.OKGREEN + ref_word + bcolors.ENDC) + ' '
			+ ' '.join(ref_sent_split[i+1:])+ "\n\n")
	print("2.",test_sent.replace(test_word, '________'))
	print("\n\t- Word definition: ", word_info[2])
	print("\n\t- Synonyms: ", end = " ")
	if not word_info[0]:
		print('n/a')
	else:
		print (', '.join(word_info[0]))
	print("\n\t- Antonyms: ", end = " ")
	if not word_info[1]:
		print('n/a')
	else:
		print(', '.join(word_info[1]),"\n\n")


# with open("word_sent_dict.txt", "rb") as dictFile:
#  	word_sent_dict = cPickle.load(dictFile)
# with open("min_pair_list.txt", "rb") as listFile:
# 	mp_list = cPickle.load(listFile)
# with open("associations.txt", "rb") as dictFile2:
# 	associations = cPickle.load(dictFile2)
# # make_min_pair_list() # this function only needs to be run once
# # make_word_sent_dict(mp_list) # this function only needs to be run once
# make_associations_dict(mp_list) # this function only needs to be run once
# min_pair = get_min_pair(mp_list)
# while ((min_pair[0] not in word_sent_dict) or (min_pair[1] not in word_sent_dict)):
# 	min_pair = get_min_pair(mp_list)
# random_sents = random_sentences(min_pair, word_sent_dict) # returns a dictionary of mp words to rand sents
# ref_and_test_word = get_test_word(random_sents)
# output(random_sents, ref_and_test_word, associations)

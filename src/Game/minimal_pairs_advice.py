import feedback

def return_pronunciation_advice(each_phoneme,IPA_sentence): #returns the pronunciation advice for each phoneme contained in the sentence
#It will return the feedback only for what has been said wrong
    pronunciation_advice=''
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

def return_pronunciation_advice_list(user_text,phonemes_IPA,sentence): #returns a list with all the pronunciation advices that the sentence needs, only for the wrongly pronounced words.
    pronunciation_advice_list=[]
    words_sentence=sentence.lower().split()
    for word in words_sentence:
        if word in user_text:
            continue
        else:
            ipa_word=feedback.ipa(word)
            for each_phoneme in ipa_word:
                if each_phoneme in phonemes_IPA:
                    pronunciation_advice=return_pronunciation_advice(each_phoneme,ipa_word)
                    pronunciation_advice_complete=("The following information may help you to pronounce the phoneme /"+ each_phoneme +"/:\n\t"+pronunciation_advice)
                    pronunciation_advice_list.append(pronunciation_advice_complete)
    return(pronunciation_advice_list)

def minimal_pairs_advice(user_text,sentence,IPA_sentence):
    phonemes_IPA=("ɪ","æ","ʊ","ɔ","ɜ","əʊ","b","v","ð","k","s","ʃ","h","n","ŋk","ŋ","j","w","ʤ") #list of phonemes
    advice_final_list=return_pronunciation_advice_list(user_text,phonemes_IPA,sentence) #get the total advices for the specific sentence
    print("This is the advice we can give you to pronunce the sentence: \n" + sentence)
    print(IPA_sentence + "\n")
    for each_advice in advice_final_list:
        print(each_advice)

# import important modules
from fidel.word import sep_words
from fidel.distance import distance
from googletrans import Translator 
from symspellpy import SymSpell, Verbosity
from fidel.dictionary import dict 
def translate(text):
	list_inp = sep_words(text)  # separating words
	added_word = "" 
	main_dic = dict() # prepare dictionary
	for words in list_inp:
		added_word += main_dic.get(words,words)  # add every changed characters
	main_word = added_word.strip(" ") 	 # remove unneccesary spaces
	return main_word
def correct(word):# check the word correct or not
	trans = Translator()
	translation_en = trans.translate(text=word,dest="en")
	translation_am = trans.translate(text=str(translation_en.text),dest="am")# translate from amh to eng and eng to amh
	dis = distance(word,str(translation_am.text)) # get the distance from pure text and tranlsted word
	if len(word) <=3 : # return True if the word is less than 4 and the distance is less that 2
		if dis <= 1:
			return True
	elif  dis <= 3  : # retune True if the word is less greater than 3 and the distance is less than 4
		return True
	return False 
def auto_correct_trans(text):
	result = "" # corrected words added to this list
	sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
	dictionary_path = "word_list.txt"
	a = sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)# preparing word list dictionary
	main_input = text.split(" ") # split by spaces
	for i in main_input :
		if correct(i) == True: # if the word is correct pass the statement once
			result += i + " "
			continue
		suggestions = sym_spell.lookup(i,Verbosity.CLOSEST,max_edit_distance=2,ignore_token=r"\w+\d",include_unknown=True) # get alternative words
		for suggestion in suggestions:
			result1 = str(suggestion).split(",")# append  suggested word
			result2 = result1[0] # get silimilar value for the word
			if len(i) != len(result2) : # exception and add the result to the main result
				result += i + " "
			else :
				result += result2 + " "
			break
	return result 

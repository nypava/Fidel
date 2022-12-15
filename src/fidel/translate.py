from fidel.word import sep_words
from symspellpy import SymSpell, Verbosity
from fidel.dictionary import dict 
import os

PROJECT_DIR = os.path.dirname(__file__)

class Translate():
	'''
	Args:
		text: The string being translated.
		AutoCorrect: boolean to turn on and off auto correct default.
	'''
	def __init__(self,text:str,AutoCorrect:True) -> str:
		self.text = text
		self.autocorrect = False
		self.autocorrect = AutoCorrect
	def translate(self):
		'''
		Args:
			``None``
		return:
			string that (translated) or (translated + autocorrect) deepend on AutoCorrect Value.
		'''
		if self.autocorrect == True:
			result = func.auto_correct(func.translate(self.text))
			return result
		else:
			result = func.translate(self.text)
			return result


class func():
	def translate(text:str) -> str:
		'''
		Args:
			text: The string being translated.
		'''
		list_inp = sep_words(text) # Separating words
		added_word = "" 
		main_dic = dict() # Prepare dictionary
		for words in list_inp:
			added_word += main_dic.get(words,words) # Add every changed characters
		main_word = added_word.strip(" ") # Remove unneccesary spaces
		return main_word
	def auto_correct(text:str) -> str:
		'''
		Args:
			text: The string being corrected.
		'''
		result = "" # Corrected words added to this string
		sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
		dictionary_path = os.path.join(PROJECT_DIR,"data/word_list.txt")
		a = sym_spell.load_dictionary(dictionary_path ,term_index=0, count_index=1,encoding="UTF-8") # Preparing word list dictionary
		trans_word = text.split(" ") # Translate and split by spaces
		for word in range(len(trans_word)):
			suggestions = sym_spell.lookup(trans_word[word],verbosity=Verbosity.CLOSEST,max_edit_distance=2,ignore_token=r"\w+\d",include_unknown=True) # Get closest words
			for suggestion in range(len(suggestions)): # For each closest word
				if len(str(suggestions[suggestion].term)) == len(trans_word[word]): # If the closest word have equal length as input word 
					result += suggestions[suggestion].term + " " # Add the the closest word to result string
					break
		return result

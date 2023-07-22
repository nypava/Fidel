from fidel.utilities.word import sep_words
from symspellpy import SymSpell, Verbosity
from fidel.utilities.dictionary import dict
from fidel.helpers.filter import filter_symbol
import os

PROJECT_DIR = os.path.dirname(__file__)

class Translate:
	'''
	Args:
		text: The text to be translated.
		autocorrect: Boolean to enable and disable auto correct default.
		symbol: Boolean to enable and disable symbol changing.
	''' 
	def __init__(self, text:str, autoCorrect:bool=False, symbol=True):
		self.text = text
		self.autocorrect = autoCorrect
		self.symbol = symbol  

	def translate(self) -> str:
		result = func(func(self.text).translate(self.symbol)).auto_correct() if self.autocorrect == True else func(self.text).translate(self.symbol)
		
		return result

def Reverse(text:str, symbol:True) -> str:
	'''
	Reverse translate.
	Args:
		text: The text to be translated.
		symbol: Boolean to enable and disable symbol changing.
	'''
	main_dic = dict(symbol)
	reversed_dic = {key:value for value,key in main_dic.items()} # Swap key and value and form new dictionary
	translated_ver = ""

	for letters in text:
		translated_ver += reversed_dic.get(letters, letters)

	return translated_ver.replace("h⨳"," ")

class func:
	def __init__(self, text:str):
		self.text = text

	def translate(self,symbol: bool) -> str:

		list_inp = sep_words(self.text) # Separating words
		translated_ver = ""
		main_dic = dict(symbol) # Prepare dictionary
		for letters in list_inp:
			translated_ver += main_dic.get(letters, letters.replace("`","")) # Add every changed characters
		translated_ver = translated_ver.strip(" ") # Remove unneccesary spaces
		
		return translated_ver

	def auto_correct(self) -> str:
		result = "" # Corrected words added to this string
		sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
		dictionary_path = os.path.join(PROJECT_DIR, "data/word_list.txt")
		a = sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1, encoding="UTF-8") # Preparing word list dictionary
		trans_word = self.text.split(" ") # Translate and split by spaces
		for word in range(len(trans_word)):
			pure_text = filter_symbol(trans_word[word])
			suggestions = sym_spell.lookup(pure_text.encode(),verbosity=Verbosity.CLOSEST, max_edit_distance=2, ignore_token=r"\w+\d", include_unknown=True) # Get closest words
			for suggestion in range(len(suggestions)): # For each closest word
				if len(str(suggestions[suggestion].term)) == len(trans_word[word]): # If the closest word have equal length as input word ?
					result += pure_text.decode(suggestions[suggestion].term + " ") # Add the the closest word to result string
					break

		return result
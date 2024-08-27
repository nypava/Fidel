from fidel.utils.separate import separate_text 
from fidel.utils.dictionary import alphabet_dictionary 
from fidel.utils.filter import FilterSymbol 
from symspellpy import SymSpell, Verbosity
import os

PROJECT_DIR = os.path.dirname(__file__)

class Transliterate:
    '''
    Args:
        text (str): The text to be translated.
        auto_correct (bool, optional): Boolean to enable or disable autocorrect. Defaults to `False`.
        symbol (bool, optional): Boolean to enable or disable symbol changing. Defaults to `False`.
    ''' 
    def __init__(
            self, 
            text:str, 
            auto_correct:bool=False, 
            symbol:bool= False
    ):
        self.text = text
        self.auto_correct = auto_correct
        self.symbol = symbol

    def transliterate(self) -> str:
        '''
        Transliterate from English character to Geez.
        Returns: 
            str: The transliterated text.
        '''
        transliterated_text = self._transliterate()
        if self.auto_correct:
            return self._auto_correct(transliterated_text)

        return transliterated_text

    def reverse_transliterate(self) -> str:
        '''
        Transliteration from Geez character to English.
        Returns: 
            str: The reversed transliterated text.
	    '''
        alphabet_dict = alphabet_dictionary(self.symbol)
        reversed_dict = {key: value for value, key in alphabet_dict.items()}
        translated_ver = ""

        for letters in self.text:
            translated_ver += reversed_dict.get(letters, letters)

        return translated_ver.replace("h⨳"," ")

    def _transliterate(self) -> str:
        list_inp = separate_text(self.text)
        translated_ver = ""
        alphabet_dict = alphabet_dictionary(self.symbol)
        for letters in list_inp:
            translated_ver += alphabet_dict.get(letters, letters.replace("`","")) 

        return translated_ver.strip() 

    def _auto_correct(self, text) -> str:
        corrected_text = "" 
        sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
        dictionary_path = os.path.join(PROJECT_DIR, "data/word_list.txt")
        sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1, encoding="UTF-8")
        for word in text.split():
            filtered_text = FilterSymbol(word)
            suggestions = sym_spell.lookup(filtered_text.encode(),
                                           verbosity=Verbosity.CLOSEST, 
                                           max_edit_distance=2, 
                                           ignore_token=r"\w+\d", # type: ignore
                                           include_unknown=True,
            ) 
            for suggestion in range(len(suggestions)): 
                if len(str(suggestions[suggestion].term)) == len(word):
                    corrected_text += filtered_text.decode(suggestions[suggestion].term + " ")
                    break

        return corrected_text

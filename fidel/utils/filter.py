import re

class FilterSymbol():
    def __init__(self, text) -> None:
        self.text = text
		
    def encode(self) -> str:
        self.filtered_symbols = []
        for letter in self.text:
            if letter in r",./']}+=_-)(*&^%$#@!~!|\)።፣??-":
                self.filtered_symbols.append(letter)
                self.text = self.text.replace(letter, "1")
				
        return self.text
	
    def decode(self, decode_text) -> str:
        for symbol in self.filtered_symbols:
            decode_text = decode_text.replace("1", symbol, 1)
			
        return decode_text

def unwanted_filter(text:str) -> tuple[str, list]:
    """
    Find and replace words with "|" that don't want to be translated.
    Args:
		text: Input text.
	Return:
		Replaced words list and words that don't wanted to be translated replaced with "|" string.
    """

    return (
        re.sub(r"`\w*`", "|", text), 
        re.findall(r"`\w*`", text)
    )

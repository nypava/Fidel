def filter_change(text:str) -> tuple:
	"""
	Find and replace words with "|" that doesn't want to be translated.
	Args:
		text: Input text.
	Return:
		Replaced words list and words that doesn't wanted to be translated replaced with "|" string.
	"""
	result_str = text
	result_list = []
	state = True
	temp_str = ""

	for letter in text:
		if letter == "`":
			if state == True:
				state = False
			else:
				state = True
				result_list.append(f"`{temp_str}`")
				result_str = result_str.replace(f"`{temp_str}`","|")
				temp_str = ""
		else:
			if state == False:
				temp_str += letter
			else:
				pass
			
	return result_str, result_list

class filter_symbol():
	def __init__(self, text) -> None:
		self.text = text
		
	def encode(self) -> str:
		self.filtered_symbols = []
		for letter in self.text:
			if letter in ",./']}+=_-)(*&^%$#@!~!|\)።፣??-":
				self.filtered_symbols.append(letter)
				self.text = self.text.replace(letter ,"1")
				
		return self.text
	
	def decode(self, decode_text) -> str:
		for symbol in self.filtered_symbols:
			decode_text = decode_text.replace("1",symbol,1)
			
		return decode_text
		
	
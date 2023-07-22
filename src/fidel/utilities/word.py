from fidel.helpers.filter import filter_change

def sep_words(text:str) -> str:
	'''
	Separate the text.
	Args:
		text: String that being separated.
	Return:
		Separated text.
	'''
	text, filtered_words = filter_change(text)
	final_text = f" {text.lower()} " # Format the text
	vowles = "aeiou" # Vowles letters list
	c_pass = False # Used for special cases
	con = "bcdfghjklmnpqrstvwxyz" # Consonant letters list
	all_alpha = f"{con}{vowles}" # All letters
	words = [] # List that the separated words added 
	filtered_index = 0 # unchanged words index
	try:
		for index, letter in enumerate(final_text): 
			if letter in con:
				# Special case on "gn" -> ግን
				if letter in "g" and final_text[index+1] in "n" and final_text[index+2] not in all_alpha and final_text[index-1] not in all_alpha:
					words.append(letter)
				# Special case on "gn(vowles) " -> የ ኘ ዘሮች
				elif letter in "g" and final_text[index+1] in "n" and final_text[index+2] in vowles:
					words.append(f"gn{final_text[index+2]}")
					c_pass = True
				# Special case on "gn" -> ኝ
				elif letter in "g" and final_text[index+1] in "n" and final_text[index+2] not in vowles:
					words.append("gn")
					c_pass = True
				# 3 digit alphabets -> ዘሸቸ
				elif letter in "spcz" and final_text[index+1] in "h" and  final_text[index+2] in vowles:
					words.append(f"{letter}h{final_text[index+2]}")
					c_pass = True
				# "sh,ph,ch,zh"
				elif letter in "scpz" and final_text[index+1] in "h" and  final_text[index+2] not in vowles:
					words.append(f"{letter}h")
					c_pass = True
				# Another 3 digit alphabets -> ፀ
				elif letter in "t" and final_text[index+1] in "s" and  final_text[index+2] in vowles:
					words.append(f"{letter}s{final_text[index+2]}")
					c_pass = True
				elif letter in "t" and final_text[index+1] in "s" and  final_text[index+2] not in vowles:
					words.append(f"{letter}s")
					c_pass = True
				# <consonant> <vowles> that the vowle is ie | double vowle|
				elif final_text[index+1] in "i" and final_text[index+2] in "e":
					c_pass = True
					words.append(f"{letter}ie")
				# The 8th or "ዲቃላ" vowles 
				elif final_text[index+1] in "u" and final_text[index+2] in "a":
					if c_pass == True:
						pass
					else:
						c_pass = True
						words.append(f"{letter}ua")
				# Two letters which are <consonant><vowles>
				elif final_text[index+1] in vowles:
					if c_pass == True:
						c_pass = False
						pass
					else:
						words.append(f"{letter}{final_text[index+1]}")
				else:
					if c_pass == True:
						c_pass = False
						pass
					# Add single consonant -> the 7th alphabet of amh | ሳድስ ፊደል |
					else:
						words.append(letter)
			# Add single vowles | የ አ ዘሮች |  
			elif letter in vowles and final_text[index-1] not in con:
				# Special case "ere" -> ኸረ 
				if letter in "e" and final_text[index+1] in "r" and  final_text[index+2] in "e" and final_text[index-1] not in all_alpha and final_text[index+3] not in all_alpha:
					words.append("ere")
					c_pass = True
				# Add single vowles "aeiou" -> | የአ ዘሮች|
				elif letter in "i" and final_text[index+1] in "e":
					words.append("ie")
					c_pass = True
				else :
					if c_pass == True:
						c_pass = False
						pass
					else:
						words.append(letter)
			# Add other characters including white space
			elif letter not in all_alpha:
				if letter == "|":
					if len(filtered_words)-1 >= filtered_index and len(filtered_words) != 0:
						words.append(filtered_words[filtered_index])
						filtered_index += 1
				else:
					words.append(letter)
	# Exceptional
	except IndexError:
		pass 

	return words

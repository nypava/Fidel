def sep_words(text:str) -> str:
	'''
	separate the text 
		Args:
			text : string that being separated
		Return:
			separated text   
	'''
	final_text = f" {text.lower()} " # Format the text
	words = [] # List that the separated words added
	index = 0 # Index
	vowles = "aeiou" # Vowles
	c_pass = False # Used for special cases
	c2_pass = False # Used for special cases
	con = "bcdfghjklmnpqrstvwxyz" # Consonant
	al_alpha = f"{con}{vowles}" # Alphabet
	try:
		for letter in final_text: 
			if letter in con:
				# Special case on "gn" -> ግን
				if letter in "g" and final_text[index+1] in "n" and final_text[index+2 ] not in al_alpha and final_text[index-1] not in al_alpha:
					words.append(letter)
				# Special case on "gn(vowles) " -> የ ኘ ዘሮች
				elif letter in "g" and final_text[index+1] in "n" and final_text[index+2] in vowles :
					words.append(f"gn{final_text[index+2]}")
					c_pass = True
				# Special case on "gn" -> ኝ
				elif letter in "g" and final_text[index+1] in "n" and final_text[index+2] not in vowles   :
					words.append("gn")
					c_pass = True
				# 3 digit alphabets -> ዘሸቸ
				elif letter in "spcz" and final_text[index+1] in "h" and  final_text[index+2] in vowles  :
					words.append(f"{letter}h{final_text[index+2]}")
					c_pass = True
				# "sh,ph,ch,zh"
				elif letter in "scpz" and final_text[index+1] in "h" and  final_text[index+2] not in vowles :
					words.append(f"{letter}h")
					c_pass = True
				# Another 3 digit alphabets -> ፀ
				elif letter in "t" and final_text[index+1] in "s" and  final_text[index+2] in vowles  :
					words.append(f"{letter}s{final_text[index+2]}")
					c_pass = True
				elif letter in "t" and final_text[index+1] in "s" and  final_text[index+2] not in vowles :
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
					if c_pass == True :
						c_pass = False
						pass
					else:
						words.append(f"{letter}{final_text[index+1]}")
				else :
					if c_pass == True:
						c_pass = False
						pass
					# Add single consonant -> the 7th alphabet of amh | ሳድስ ፊደል |
					else:
						words.append(letter)
			# Add single vowles | የ አ ዘሮች |  
			elif letter in vowles and final_text[index-1] not in con:
				# Special case "ere" -> ኸረ 
				if letter in "e" and final_text[index+1] in "r" and  final_text[index+2] in "e" and final_text[index-1] not in al_alpha and final_text[index+3] not in al_alpha :
					words.append("ere")
					c_pass = True
				# Add single vowles "aeiou" -> | የአ ዘሮች|
				elif letter in "i" and final_text[index+1] in "e":
					words.append("ie")
					c_pass = True
				else :
					if c_pass == True :
						c_pass = False
						pass
					else:
						words.append(letter)
			# Add other characters and white spaces
			elif letter not in al_alpha:
				words.append(letter)
			index += 1
	# Exceptional
	except IndexError:
		pass
	return words

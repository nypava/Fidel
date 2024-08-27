from fidel.utils.filter import unwanted_filter 

CONSONANTS = "bcdfghjklmnpqrstvwxyz" 
VOWLES = "aeiou" 
ALPHABETS = CONSONANTS + VOWLES

def separate_text(text:str) -> list:
    '''
	Separate the text.
	Args:
		text (str): String that being separated.
	Return:
        list: Separated text.
	'''
    text, filtered_words = unwanted_filter(text)
    text = f" {text} " 

    c_pass = False 
    filtered_index = 0

    words = [] 

    try:
        for index, letter in enumerate(text): 
            if letter in CONSONANTS:
				# Special case on "gn" -> ግን
                if letter in "g" and text[index+1] in "n" and text[index+2] not in ALPHABETS and text[index-1] not in ALPHABETS:
                    words.append(letter)
				# Special case on "gn(VOWLES) " -> የ ኘ ዘሮች
                elif letter in "g" and text[index+1] in "n" and text[index+2] in VOWLES:
                    words.append(f"gn{text[index+2]}")
                    c_pass = True
				# Special case on "gn" -> ኝ
                elif letter in "g" and text[index+1] in "n" and text[index+2] not in VOWLES:
                    words.append("gn")
                    c_pass = True
				# 3 digit ALPHABETS -> ዘሸቸ
                elif letter in "spcz" and text[index+1] in "h" and  text[index+2] in VOWLES:
                    words.append(f"{letter}h{text[index+2]}")
                    c_pass = True
				# "sh,ph,ch,zh"
                elif letter in "scpz" and text[index+1] in "h" and  text[index+2] not in VOWLES:
                    words.append(f"{letter}h")
                    c_pass = True
				# Another 3 digit ALPHABETS -> ፀ
                elif letter in "t" and text[index+1] in "s" and  text[index+2] in VOWLES:
                    words.append(f"{letter}s{text[index+2]}")
                    c_pass = True
                elif letter in "t" and text[index+1] in "s" and  text[index+2] not in VOWLES:
                    words.append(f"{letter}s")
                    c_pass = True
				# <consonant> <VOWLES> that the vowle is ie | double vowle|
                elif text[index+1] in "i" and text[index+2] in "e":
                    c_pass = True
                    words.append(f"{letter}ie")
				# The 8th or "ዲቃላ" VOWLES 
                elif text[index+1] in "u" and text[index+2] in "a":
                    if not c_pass:
                        c_pass = True
                        words.append(f"{letter}ua")
				# Two letters which are <consonant><VOWLES>
                elif text[index+1] in VOWLES:
                    if c_pass:
                        c_pass = False
                        continue
                    words.append(f"{letter}{text[index+1]}")
				# Add single consonant -> the 7th alphabet of amh | ሳድስ ፊደል |
                else:
                    if c_pass:
                        c_pass = False
                        continue
                    words.append(letter)
			# Add single VOWLES | የ አ ዘሮች |  
            elif letter in VOWLES and text[index-1] not in CONSONANTS:
				# Special case "ere" -> ኸረ 
                if letter in "e" and text[index+1] in "r" and  text[index+2] in "e" and text[index-1] not in ALPHABETS and text[index+3] not in ALPHABETS:
                    words.append("ere")
                    c_pass = True
				# Add single VOWLES "aeiou" -> | የአ ዘሮች|
                elif letter in "i" and text[index+1] in "e":
                    words.append("ie")
                    c_pass = True
                else :
                    if c_pass == True:
                        c_pass = False
                    else:
                        words.append(letter)
			# Add other characters including white space
            elif letter not in ALPHABETS:
                if letter == "|":
                    if len(filtered_words)-1 >= filtered_index and len(filtered_words) != 0:
                        words.append(filtered_words[filtered_index])
                        filtered_index += 1
                else:
                    words.append(letter)
    except IndexError:
        pass 

    return words

def sep_words(inp):
 final_inp = f" {inp.lower()} " #format the input
 words = [] #list that the separated words added
 index = 0 #index
 vowles="aeiou" #vowles
 c_pass = False #used for special cases
 c2_pass = False #used for special cases
 con = "bcdfghjklmnpqrstvwxyz" #consonant
 al_alpha = f"{con}{vowles}" #alphabet
 try:
  for letter in final_inp: 
  	if letter in con:
  		#special case on "gn" -> ግን
  		if letter in "g" and final_inp[index+1] in "n" and final_inp[index+2 ] not in al_alpha and final_inp[index-1] not in al_alpha:
  			words.append(letter)
  		#special case on "gn(vowles) " -> የ ኘ ዘሮች
  		elif letter in "g" and final_inp[index+1] in "n" and final_inp[index+2] in vowles :
  			words.append(f"gn{final_inp[index+2]}")
  			c_pass = True
  		#special case on "gn" -> ኝ
  		elif letter in "g" and final_inp[index+1] in "n" and final_inp[index+2] not in vowles   :
  			words.append("gn")
  			c_pass = True
  		# 3 digit alphabets -> ዘሸቸ
  		elif letter in "spcz" and final_inp[index+1] in "h" and  final_inp[index+2] in vowles  :
  			words.append(f"{letter}h{final_inp[index+2]}")
  			c_pass = True
  			# "sh,ph,ch,zh"
  		elif letter in "scpz" and final_inp[index+1] in "h" and  final_inp[index+2] not in vowles :
  			words.append(f"{letter}h")
  			c_pass = True
  		# another 3 digit alphabets -> ፀ
  		elif letter in "t" and final_inp[index+1] in "s" and  final_inp[index+2] in vowles  :
  			words.append(f"{letter}s{final_inp[index+2]}")
  			c_pass = True
  		elif letter in "t" and final_inp[index+1] in "s" and  final_inp[index+2] not in vowles :
  			words.append(f"{letter}s")
  			c_pass = True
  	  # <consonant> <vowles> that the vowle is ie | double vowle|
  		elif final_inp[index+1] in "i" and final_inp[index+2] in "e":
  			  	c_pass = True
  			  	words.append(f"{letter}ie")
  		# the 8th or "ዲቃላ" vowles 
  		elif final_inp[index+1] in "u" and final_inp[index+2] in "a":
  			if c_pass == True:
  				pass
  			else:
  				c_pass = True
  				words.append(f"{letter}ua")
  	  # two letters which are <consonant><vowles>
  		elif final_inp[index+1] in vowles:
  			if c_pass == True :
  				c_pass = False
  				pass
  			else:
  				words.append(f"{letter}{final_inp[index+1]}")
  		else :
  			if c_pass == True:
  				c_pass = False
  				pass
  			#add single consonant -> the 7th alphabet of amh | ሳድስ ፊደል |
  			else:
  				words.append(letter)
  	#add single vowles | የ አ ዘሮች |  
  	elif letter in vowles and final_inp[index-1] not in con:
  	# special case "ere" -> ኸረ 
  		if letter in "e" and final_inp[index+1] in "r" and  final_inp[index+2] in "e" and final_inp[index-1] not in al_alpha and final_inp[index+3] not in al_alpha :
  		         	words.append(f"ere")
  		         	c_pass = True
  		 # add single vowles "aeiou" -> | የአ ዘሮች|
  		else :
  			if c_pass == True :
  				c_pass = False
  				pass
  			else:
  				words.append(letter)
  	#add other characters and white spaces
  	elif letter not in al_alpha:
  		words.append(letter)
  	index += 1
 #exceptional
 except IndexError:
 	pass
 return words

def dict():
   dic = {"ere":"ኸረ"}   #dictional that pairs of amh and eng letter added
   cons_vow = [] #list that consonant and vowles list added in pair
   amh = [
   "ለሉሊላሌልሎሏ","መሙሚማሜምሞሟ",
   "ረሩሪራሬርሮሯ","ሰሱሲሳሴስሶሷ","ሸሹሺሻሼሽሾሿ",
   "ቀቁቂቃቄቅቆቋ","በቡቢባቤብቦቧ","ቨቩቪቫቬቭቮቯ",
   "ተቱቲታቴትቶቷ","ቸቹቺቻቼችቾ ","የዩዪያዬይዮ ",
   "ነኑኒናኔንኖኗ","ኘኙኚኛኜኝኞኟ",
   "ከኩኪካኬክኮኳ","ወዉዊዋዌውዎ ",
   "ዘዙዚዛዜዝዞዟ","ዠዡዢዣዤዥዦዧ","ደዱዲዳዴድዶዷ",
   "ጀጁጂጃጄጅጆ ","ገጉጊጋጌግጎጓ","ጠጡጢጣጤጥጦጧ",
   "ጨጩጪጫጬጭጮጯ","ጸጹጺጻጼጽጾ ","ጰጱጲጳጴጵጶጷ",
   "ፈፉፊፋፌፍፎፏ","ፐፑፒፓፔፕፖፗ","አኡኢ ኤእኦኧ","ሀሁሂ ሄህሆኋ" ] # amharic alphabets
   vowles=["e","u" ,"i","a","ie","","o","ua"] #vowles that pair with consonant
   index = 0
   AH_index = 26 
   amh_eng = [
   "l","m","r","s","sh","q","b","v","t",
   "ch","y","n","gn","k","w","z","zh","d",
   "j","g","x","c","ts","ph","f","p"
    ] #letters that pair with vowles
   H_vow = ["a","u","i","⨳","e","","o","ua"] #vowles used for "ሀ"
   A_vow = ["a","u","i","⨳","ie","e","o","ua"] #vowles used for "አ"
   AH_alpha = ["","h"] #consonant used for "u and አ"
   AH_eng= ["አኡኢኤእኦ","ሀሁሂሄህሆ"] #ሀ and አ amharic alphabet
   
   for spaces in range(29): #loop that append "[]" that used for add pair of letters
   	cons_vow.append([])
 	
   for each_alpha in range(26): #loop that add pair of letter | consonants and vowles
       for each_vow in range(8):
       	l = cons_vow[index]
       	l.append(f"{amh_eng[each_alpha]}{vowles[each_vow]}")
       index += 1
   
   for each_AHalpha in range(2): #loop that add pair of letter "አሀ" special case
   	for each_AHvow in range(8):
   		l = cons_vow[AH_index]
   		if AH_alpha[each_AHalpha] == "":
   			l.append(f"{AH_alpha[each_AHalpha]}{A_vow[each_AHvow]}")
   		elif AH_alpha[each_AHalpha] == "h":
   				l.append(f"{AH_alpha[each_AHalpha]}{H_vow[each_AHvow]}")
   	AH_index += 1
   
   for index1 in range(28): #final loop that pair amharic alpha to consonant and vowles pair
   	for index2 in range(8):
   		amh_get = amh[index1][index2]
   		cons_vow_get = cons_vow[index1][index2]
   		dic[cons_vow_get] = amh_get
   return dic
   
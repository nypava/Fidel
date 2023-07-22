def dict(symbol:bool) -> dict:
    '''
        Args:
           symbol: True - Enable symbol, False - Disable symbol.
        Return:
            Dictionary each alphabets with their English character value  
    '''
    
    dic = {"ere":"ኸረ"}   # Dictionary that pairs of Amharic and English letter added
    cons_vow = [] # List that consonant and vowles list added in pair
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
    "ፈፉፊፋፌፍፎፏ","ፐፑፒፓፔፕፖፗ","አኡኢ ኤእኦኧ","ሀሁሂ ሄህሆኋ"
    ] # Amharic alphabets
    vowles=["e","u" ,"i","a","ie","","o","ua"] # Vowles 
    index = 0
    AH_index = 26 
    amh_eng = [
    "l","m","r","s","sh","q","b","v","t",
    "ch","y","n","gn","k","w","z","zh","d",
    "j","g","x","c","ts","ph","f","p"
     ] # Consonant
    H_vow = ["a","u","i","⨳","e","","o","ua"] # Vowles used for "ሀ"
    A_vow = ["a","u","i","⨳","ie","e","o","ua"] # Vowles used for "አ"
    AH_alpha = ["","h"] # Empty string and Consonant used for "u and አ"
    AH_eng= ["ሀሁሂሄህሆኋ","አኡኢኣኤእኦ"] # ሀ and አ Amharic alphabet
    for spaces in range(29): # Loop that append "[]" that used for add pair of letters
        cons_vow.append([])
 	
    for each_alpha in range(26): # Loop that add pair of letter | consonants and vowles
        for each_vow in range(8):
            l = cons_vow[index]
            l.append(f"{amh_eng[each_alpha]}{vowles[each_vow]}")
        index += 1
   
    for each_AHalpha in range(2): # Loop that add pair of letter "አሀ" special case
        for each_AHvow in range(8):
            l = cons_vow[AH_index]
            if AH_alpha[each_AHalpha] == "":
                l.append(f"{AH_alpha[each_AHalpha]}{A_vow[each_AHvow]}")
            elif AH_alpha[each_AHalpha] == "h":
                l.append(f"{AH_alpha[each_AHalpha]}{H_vow[each_AHvow]}")
        AH_index += 1
   
    for index1 in range(28): # Final loop that pair Amharic alpha to consonant and vowles pair
        for index2 in range(8):
            amh_get = amh[index1][index2]
            cons_vow_get = cons_vow[index1][index2]
            dic[cons_vow_get] = amh_get
    
    # Add symbols to dictionary if it is True
    if symbol == True:
        for key, value in [(".","።"),(",","፣"),(":","፡")]:
            dic[key] = value
    else:
        pass

    return dic
   
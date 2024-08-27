from typing import Dict

GEEZ_CHAR = [
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
] 

GEEZ_AH_CHAR = ["ሀሁሂሄህሆኋ","አኡኢኣኤእኦ"] # ሀ and አ Amharic alphabet

AM_VOWLES = ["e","u" ,"i","a","ie","","o","ua"]
AM_CONSONANTS = [
    "l","m","r","s","sh","q","b","v","t",
    "ch","y","n","gn","k","w","z","zh","d",
    "j","g","x","c","ts","ph","f","p"
] 

H_VOWELES = ["a","u","i","⨳","e","","o","ua"] # Vowles used for "ሀ"
A_VOWELES = ["a","u","i","⨳","ie","e","o","ua"] # Vowles used for "አ"

AH_ALPHABET = ["","h"] 

def alphabet_dictionary(symbol:bool) -> Dict:
    '''
    Args:
        symbol (bool): `True` - Enable symbol, `False` - Disable symbol.
    Return:
        dict: Dictionary each alphabets with their English character value.
    '''
    pair_result = {"ere":"ኸረ"}   
    cons_vow_pair = [] 
    index = 0
    for _ in range(29):
        cons_vow_pair.append([])
 	
    for alphabet in range(26): # Loop that add pair of letter | consonants and vowles
        for vowel in range(8):
            cons_vow_pair[index].append(f"{AM_CONSONANTS[alphabet]}{AM_VOWLES[vowel]}")
        index += 1
   
    for alphabet in range(2): # Loop that add pair of letter "አሀ" special case
        for vowel in range(8):
            if AH_ALPHABET[alphabet] == "":
                cons_vow_pair[index].append(f"{AH_ALPHABET[alphabet]}{A_VOWELES[vowel]}")
                continue
            cons_vow_pair[index].append(f"{AH_ALPHABET[alphabet]}{H_VOWELES[vowel]}")
        index += 1
   
    for index1 in range(28): # Final loop that pair Amharic alpha to consonant and vowles pair
        for index2 in range(8):
            amh_get = GEEZ_CHAR[index1][index2]
            cons_vow_get = cons_vow_pair[index1][index2]
            pair_result[cons_vow_get] = amh_get
    
    # Add symbols to dictionary if it is True
    if symbol:
        for key, value in [(".", "።"), (",", "፣"), (":", "፡")]:
            pair_result[key] = value

    return pair_result

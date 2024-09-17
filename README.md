# **Fidel / ፊደል**
## What is **Fidel / ፊደል** ?
**Fidel** is a Python package that can transliterate Latin characters to Geez characters and vice versa. <br>
> **For example: abebe beso bela -> አበበ በሶ በላ**


## **Dependencies**
* [Symspellpy](https://github.com/mammothb/symspellpy)


## **Installation** 
```
pip install fidel
```
## **Upgrade**
```
pip install --upgrade fidel
```
#

## **Usage**

### **Basic Usage**
``` python
from fidel import Transliterate 
text = "bexam xru sew new"
translated = Transliterate(text).transliterate()
print(translated)
```
output
```
በጣም ጥሩ ሰው ነው
```

### **Autocorrect**
``` python
from fidel import Transliterate 
text = "betam tiru sew nw"
translated = Transliterate(text=text, auto_correct=False).transliterate() # The default is False
corrected = Transliterate(text=text, auto_correct=True).transliterate()
print(f"Translated : {translated}")
print(f"Corrected: {corrected}")

```
output
```
Translated: በታም ቲሩ ሰው ንው
Corrected: በጣም ጥሩ ሰው ነው
```
### **Amharic Symbol**
``` python 
from fidel import Transliterate 
text = "abebe, kebede ena ayele bexam xru sew nachew."
symbol_true = Transliterate(text=text, symbol=True).transliterate() # The default is True
symbol_false = Transliterate(text=text, symbol=False).transliterate()
print(f"True symbol: {symbol_true}")
print(f"False symbol: {symbol_false}")
```
output
```
True symbol:  አበበ፣ ከበደ እና አየለ በጣም ጥሩ ሰው ናቸው።
False symbol: አበበ, ከበደ እና አየለ በጣም ጥሩ ሰው ናቸው.
```
### **Exclude words** and **Split words**
**Exclude words** from being translated.
- To prevent words from being translate, put the words inside "``" 
``` python
from fidel import Transliterate
text = "`Alex` xru sew new"
transliterated = Transliterate(text).transliterate()
print(transliterated)

```
output
```
Alex ጥሩ ሰው ነው
```
**Split words**
- To prevent words from being ዲቃላ (The eigth letters) we should put "|" between consonants.
``` python
from fidel import Transliterate
text = "ljtua t|sewer" # Without "|" the output is "ልጅቷ ጸወር"
transliterated = Transliterate(text).transliterate()
print(transliterated)
```
output
```
ልጅቷ ትሰወር
```

### **Reverse Translate**
``` python
from fidel import Transliterate
text = "በጣም ጥሩ ሰው ነው።"
reversed = Transliterate(text, symbol=True).reverse_transliterate() # The default symbol value is True 
print(reversed)
```
output
```
betam xru sew new.
```

## **Rules** 
There are some **rules** that should be apply when writing a text.
 1. For **1st alphabets (ለግዕዝ)** use "e" example: "le" - ለ
 2. For **2nd alphabets (ለካእብ)** use "u" example: "lu" - ሉ
 3. For **3rd alphabets (ለሳልስ)** use "i" example: "li" - ሊ
 4. For **4rh alphabets (ለራዕብ)** use "a" example: "la" - ላ
 5. For **5th alphabets (ለሀምስ)** use "ie" example: "lie" - ሌ
 6. For **6th alphabets (ለሳድስ)** use only vowel example: "l" - ል
 7. For **7th alphabets (ለሳብዕ)** use "o" example: "lo" - ሎ
 8. For **8th alphabets(ለዲቃላ ቃላት)** use "ua" example: "ua" -  ሏ 

**Note** The above rules may be violated for some alphabets families. Check out ambiguous alphabets.
## **Ambiguous alphabets**

| ግዕዝ | ካእብ | ሳልስ | ራዕብ | ሀምስ | ሳድስ | ሳብዕ |
|-----|-----|-----|-----|------|-----|-----|
|  **ሀ**  |  **ሁ**  |  **ሂ**  |  **ሀ**  |  **ሄ**   |  **ህ**  |  **ሆ**  |
| ha  | hu  | hi  | ha  | hie  |  h  |  ho |
|  **አ**  |  **ኡ**  |  **ኢ**  |  **ኣ**  |  **ኤ**   |  **እ**  |  **ኦ**  |
|  a  |  u  |  i  |  a   |  ie  |  e  |  o  |
|  **ተ**  |  **ቱ**  |  **ቲ**  |  **ታ**  |  **ቴ**   |  **ት**  |  **ቶ**  |
|  te |  tu  |  ti  |  ta  |  tie   |  t  |  to  |
|  **ጠ**  |  **ጡ**  |  **ጢ** | **ጣ**  |  **ጤ**   |  **ጥ**  |  **ጦ**  |
|  xe  |  xu  |  xi  |  xa  |  xie   |  x  |  xo  |
|  **ቸ**  | **ቹ**  |  **ቺ**  |  **ቻ**  |  **ቼ**   |  **ች**  |  **ቾ**  |
|  che  |  chu  |  chi  |  cha  |  chie   |  ch  |  cho  |
|  **ጨ**  |  **ጩ** |  **ጪ**  |  **ጫ**  |  **ጬ**   | **ጭ** |  **ጮ**  |
|  ce  |  cu  |  ci  |  ca  |  cie   |  c  |  co  |
|  **ጰ**  |  **ጱ**  |  **ጲ**  |  **ጳ**  |  **ጴ**   |  **ጵ**  |  **ጶ**  |
|  phe  |  phu  |  phi  |  pha  |  phie   |  ph  |  pho  |
|  **ፐ**  |  **ፑ**  |  **ፒ**  |  **ፓ**  |  **ፔ**   |  **ፕ**  |  **ፖ**  |
|  pe  |  pu |  pi  |  pa  |  pie   |  p  |  po  |

**Addition** <br>
|Alphabets |ሸ| ኘ| ዥ| ጸ| 
|-----|-----|-----|-----|------|
|Prefix |sh |gn |zh| ts|

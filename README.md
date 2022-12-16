# **Fidel / ፊደል**
## What is **Fidel / ፊደል** ?
**Fidel** is a python package that can change Amharic language that written in English alphabet to Amharic alphabet character. <br>
**| For example: abebe beso bela -> አበበ በሶ በላ**


## **Dependencies**
* [Symspellpy](https://github.com/mammothb/symspellpy)


## **Installation** 
```
pip install fidel
```


## **Usage**

### **Without Autocorrect**
``` python
from fidel import Translate
text = "bexam xru sew new"
trans_word = Translate(text=text,AutoCorrect=False).translate()
print(trans_word)
```
output
```
በጣም ጥሩ ሰው ነው
```

### **Autocorrect Mode**
``` python
from fidel import Translate
text = "betam tiru sew nw"
trans_word = Translate(text=text,AutoCorrect=False).translate()
corrected_word = Translate(text=text,AutoCorrect=True).translate()
print(f"translated : {trans_word}")
print(f"corrected_word : {corrected_word}")
```
output
```
translated : በታም ቲሩ ሰው ንው
corrected_word : በጣም ጥሩ ሰው ነው
```


## **Rules** 
There are some **rules** that should be apply when writing the text
 1. For **1st alphabets (ለግዕዝ)** use "e" example: "le" - ለ
 2. For **2nd alphabets (ለካእብ)** use "u" example: "lu" - ሉ
 3. For **3rd alphabets (ለሳልስ)** use "i" example: "li" - ሊ
 4. For **4rh alphabets (ለራዕብ)** use "a" example: "la" - ላ
 5. For **5th alphabets (ለሀምስ)** use "ie" example: "lie" - ሌ
 6. For **6th alphabets (ለሳድስ)** use only vowel example: "l" - ል
 7. For **7th alphabets (ለሳብዕ)** use "o" example: "lo" - ሎ
 8. For **8th alphabets(ለዲቃላ ቃላት)** use "ua" example: "ua" -  ሏ 

**Note** The above rules may violate for some alphabets family check out ambiguous alphabets.
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


## **Donate and feedback** 

contact me : [![image](https://img.icons8.com/color/20/null/telegram-app--v1.png)](https://t.me/ny_off_tm) [Telegram](https://t.me/ny_off_tm) <br>
        [![image](https://img.icons8.com/fluency/20/000000/instagram-new.png)](https://www.instagram.com/ny.off.ig/) [Instagram](https://www.instagram.com/ny.off.ig/) 


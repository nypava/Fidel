# Fidel / ፊደል
## What is Fidel / ፊደል ?

**Fidele** is a tool that can change Amharic language that written in English alphabet translater to pure Amharic alphabet characters 
 * It will be Used for social medias specially on telegram 
## Dependencies
* [Googletrans](https://py-googletrans.readthedocs.io) 
* [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance)
* [Symspellpy](https://github.com/mammothb/symspellpy)
## Installation 
```
pip install fidel
```
## Usage
###### Without Autocorrect
It takes < 1sec and If rules are applied it is more effective than autocorrect mode
``` python
from fidele import translate
text = "mukera"
trans_word = translate.translate(text)
```
###### +Autocorrect
Delay upto 10 sec
``` python
from fidele import translate
text = "mukera"
trans_word = translate.translate(text)
corrected_word = translate.auto_correct_trans(trans_word)
```
## Rules 
There are some rules that should applied when writing text to be translate 
 1. For 1st alphabets (ለግዕዝ ) use "e" example: "le" - ለ
 2. For 2nd alphabets ( ለካእብ ) use "u" example: "lu" - ሉ
 3. For 3rd alphabets (ለሳልስ ) use "i" example: "li" - ሊ
 4. For 4rh alphabets (ለራዕብ ) use "a" example: "la" - ላ
 5. For 5th alphabets (ለሀምስ ) use "ie" example: "lie" - ሌ
 6. For 6th alphabets (ለሳድስ) use only vowel example: "l" - ል
 7. For 7th alphabets (ለሳብዕ) use "o" example: "lo" - ሎ
 8. For 8th alphabets(ለዲቃላ ቃላት) use "ua" example: "ua" -  ሏ
 9. The above rules not works for "አ" and "ሀ" family in  "አ" and "ሀ" 4th alphabets are removed because it have the same sound as 1th alphabet
 10. for "አ" and "ሀ" 1st alphabets uses " a " 
## More About Corrector
In amharic threre are too many words and I try to scrap some words from [this web](https://corpora.fi.muni.cz/habit/run.cgi/wordlist?corpname=amwac16&refs=&wlmaxitems=1000&wlsort=f&subcnorm=freq&corpname=amwac16&reload=&wlattr=word&usengrams=0&ngrams_n=2&ngrams_max_n=2&nest_ngrams=0&wlpat=&wlminfreq=1&wlmaxfreq=0&wlfile=&wlblacklist=&wlnums=frq&wltype=simple&wlpage) there are around 1 million words 
but as translator its not affortable it have long time delay symspellpy load 5000 words per second which means 
it delay 200 sec for 1M word so I scrap 20 pages to decrease the delay if you want increase accuracy word_list.txt is changable you can get 
word list from [this web](https://corpora.fi.muni.cz/habit/run.cgi/wordlist?corpname=amwac16&refs=&wlmaxitems=1000&wlsort=f&subcnorm=freq&corpname=amwac16&reload=&wlattr=word&usengrams=0&ngrams_n=2&ngrams_max_n=2&nest_ngrams=0&wlpat=&wlminfreq=1&wlmaxfreq=0&wlfile=&wlblacklist=&wlnums=frq&wltype=simple&wlpage) 

## Donate and feedback :)
contact : [telegram](https://t.me/ny_off_tm)





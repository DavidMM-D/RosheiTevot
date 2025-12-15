import re
import json
# for text of mechon-mamre.org (w/out vowels & cantiltn)
# This script creates a dict of verses (book, chap, verse) : verse text
# like ('בראשית', 1, 1): "בראשית ברא א' את השמים ואת הארץ"
# Using that, it writes a dict of words <word number 0-indexed> : (word, (book, chap, verse))
# That dict is written to a file named 'word_bk_ch_v.txt'
# Then, it writes a string of all first letters '...בבאאהוה'.
# That string is written to a file name 'allRT.txt'
letters = "אבגדהוזחטיכלמנסעפצקרשת"
gem = {} # to store dictionary of gematriot
for c in letters[:10]: # defining א - י
    gem[c] = letters.find(c) + 1
for c in letters[10:19]: # defining כ - ק
    gem[c] = 10 * letters.find(c) - 80
for c in letters[19:]: # defining ר - ת
    gem[c] = 100 * letters.find(c) - 1700

pasuk = {}
bk = "??" # default definition in case no book name found
books = [
    "בראשית",
    "שמות",
    "ויקרא",
    "במדבר",
    "דברים",
    "יהושע",
    "שופטים",
    "שמואל א",
    "שמואל ב",
    "מלכים א",
    "מלכים ב",
    "ישעיהו",
    "ירמיהו",
    "יחזקאל",
    "הושע",
    "יואל",
    "עמוס",
    "עבדיה",
    "יונה",
    "מיכה",
    "נחום",
    "חבקוק",
    "צפניה",
    "חגי",
    "זכריה",
    "מלאכי",
    "תהלים",
    "משלי",
    "איוב",
    "שיר השירים",
    "רות",
    "איכה",
    "קהלת",
    "אסתר",
    "דניאל",
    "עזרא",
    "דברי הימים א",
    "דברי הימים ב"
    ]
# Faulty text in that it represents Ktiv followed by Kri equally and w/out note.
with open("Torah.txt", 'r', encoding='utf-8') as f:
        text = f.read()
print("Torah.txt opened")
for i in range(len(text)):
    if text[i] == ',' and text[i+1] in letters: # find pasuk label indicated by <comma> not followed by space
        ch = gem[text[i-1]]
        if text[i-2] in letters:
            ch += gem[text[i-2]]
            if text[i-3] in letters:
                ch += gem[text[i-3]] # chapter number stored
        i += 1
        v = gem[text[i]]
        i += 1
        if text[i] in letters:
            v += gem[text[i]]
            i += 1
            if text[i] in letters:
                v += gem[text[i]] # verse number stored
                i += 1
        if (ch, v) == (1, 1): # when we see ch 1, v 1...
            j = 1
            while text[i-j].isspace() == False: # cycle back thru non-space verse lable
                j += 1
            while text[i-j].isspace(): # and thru preceding spaces
                j += 1
            itle = text[i-j-2:i-j+1] # slice is last 3 letters of book name
            for book in books: # Last-2-letter test sufficient for Torah. Used 3 for more robust handling of book names.
                if itle == book[-3:]: #  To add Na"CH search, we have to account for repeats like מיכה and איכה
                    bk = book
                    break
        i += 1 
        j = 0
        while text[i+j] != '.':
            j += 1
            if i+j == len(text):
                print('!! last verse may not be copied correctly !!')
                break
        pasuk[(bk, ch, v)] = text[i:i+j]
        while True: # find all '{' and delete them and their following char. This handles break markings {ס}, {פ}, {ש}, {ר}
            d = pasuk[(bk, ch, v)].find('{')
            if d == -1: break
            pasuk[(bk, ch, v)] = pasuk[(bk, ch, v)][:d] + pasuk[(bk, ch, v)][d+2:]
        pasuk[(bk, ch, v)] = re.split(r'\W+', pasuk[(bk, ch, v)])
print('pasuk dict created')
# write 2 files
# make new dict using int's to index each word as key to value containing a list containing [word, book, chapter, verse], in that order.
# Faulty handling of Kri/Ktiv
word = {}
i = 0
for key, value in pasuk.items():
    for w in value:
        word[i] = (w, key)
        i += 1
print('word dict created')
# Write word dictionary in a file
with open("word_bk_ch_v.txt", 'w', encoding='utf-8') as w:
    w.write(str(word))
print('word_bk_ch_v.txt written')
# Copy word dictionary into JSON file
i = 0
for key, value in pasuk.items(): # reformat *word* json friendly (no tuples)
    for w in value:
        word[i] = [w, key[0], key[1], key[2]]
        i += 1
print('word dict reformatted')
with open("word_bk_ch_v.json", "w", encoding="utf-8") as w:
    json.dump(word, w, ensure_ascii=False)
print('word_bk_ch_v.json written')
# Join each word's first letter into a string and write it into its file
allRT = ''.join([item[0][0] for item in word.values()])
print('allRT str created')
with open("allRT.txt", 'w', encoding='utf-8') as a:
    a.write(allRT)
print('allRT.txt written')
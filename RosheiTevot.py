import re
def hprint(text):
    h = list(text)
    h.reverse()
    print(''.join(h))
    return

def find_roshei_tevot(name, filepath='Torah.txt'):    
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
            
    # Split on any whitespace or specified punctuation
    words = re.split(r'[ \t\n\r\f\v:.,;\-{}?!]+', text)
    # Remove any empty strings, just in case
    words = [w for w in words if w]
    #pesukim = text.split('.')
    #pasuk = []
    results = []
    

    for i in range(len(words) - len(name) + 1):
        # Take a slice of consecutive words
        window = words[i:i+len(name)]
        
        # Get Roshei Tevot (first letters)
        roshei_tevot = ''.join(word[0] for word in window if word)
        
        if roshei_tevot == name:
           # pasuk.append([p for p in pesukim if window in p])
            window = [word[:1] + '"' + word[1:] for word in window]
            results.append(window)
    
    if results:
        print("Match at words: ")
        for e in results:
            hprint(' '.join(e))
    else:
        print("No matches found.")

name_to_find = input("Enter the name: ")
find_roshei_tevot(name_to_find)

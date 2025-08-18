import re  #special splitting

# right to left printing 
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
    
    results = [] # to store matches    

    for i in range(len(words) - len(name) + 1):
        # Take a slice of consecutive words
        window = words[i:i+len(name)]
        
        # Get Roshei Tevot
        roshei_tevot = ''.join(word[0] for word in window)
        # check for match
        if roshei_tevot == name:
            # reformat as R"oshei T"evot for display
            window = [word[:1] + '"' + word[1:] for word in window]
            results.append(window)
    # Display results
    if results:
        print("Match at words: ")
        for e in results:
            hprint(' '.join(e))
    else:
        print("No matches found.")

name_to_find = input("Enter the name: ")
find_roshei_tevot(name_to_find)

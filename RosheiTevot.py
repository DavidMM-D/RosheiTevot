import re  #special splitting

# right to left printing 
def hprint(text):
    h = list(text)
    h.reverse()
    print(''.join(h))
    return

def find_roshei_tevot(name, filepath='Torah.txt'):   
    # replace all final letters in 'name' with normal counterparts
    fin = 'ךםןףץ'
    nor = 'כמנפצ'
    for i in range(len(name)):
        if name[i] in fin:
            name = name[:i] + nor[fin.find(name[i])] + name[i+1:]

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
            # reformat as R"oshei T"evot in context for display
            context = []
            if i > 6:
                context = words[i-7:i]
            context += [word[:1] + '"' + word[1:] for word in window]
            if i < (len(words) - len(name) - 6):
                context += words[i + len(name):i + len(name) + 7]
            results.append(context)
    # Display results
    print("name entered: ")
    hprint(name)
    print("Number of matches: {}".format(len(results)))
    for e in results:
        hprint(' '.join(e))
# Interface
print("***Welcome to Roshei Tevot finder!***\n > Search for where a name (or word) appears as Roshei Tevot in the Torah.\n > At any time, enter 'exit' to exit.")
while True:
    name_to_find = input("Enter a name: ")
    if name_to_find.lower() == 'exit': break
    find_roshei_tevot(name_to_find)

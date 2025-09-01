def unfinal(name): # replace all final letters in 'name' with normal counterparts
    fin = 'ךםןףץ'
    nor = 'כמנפצ'
    for i in range(len(name)):
        if name[i] in fin:
            name = name[:i] + nor[fin.find(name[i])] + name[i+1:]
    return name

def RT(name):
    results = []
    start = 0
    while True:
        i = allRT.find(unfinal(name), start)
        if i == -1: break
        results.append(i)
        start = i + 1

     # Display results
    print("name entered: ", name[::-1])
    print("number of matches: {}".format(len(results)))
    for e in results: # for each element, that being the index of the first word of the match
        display = ''
        for i in range(len(name)):
            display += '{} '.format(word[e+i][0]) # build string of all words making up the match
        print(display[::-1], str(word[e][1][1]) + ',', word[e][1][2], word[e][1][0][::-1]) # print text words RTL, ch(add comma), v, book RTL
    return

with open('word_bk_ch_v.txt', 'r', encoding='utf-8') as w:
    word = eval(w.read())
with open('allRT.txt', 'r', encoding='utf-8') as a:
    allRT = a.read()

# Interface
print("***Welcome to Roshei Tevot finder!***\n > Search for where a name (or word) appears as Roshei Tevot in the Torah.\n > At any time, enter 'exit' to exit.\n > A result spanning more than 1 pasuk cites only the opening pasuk.")
while True:
    name = input("Enter a name: ")
    if name.lower() == 'exit': break
    RT(name)
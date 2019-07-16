import sys, re, string
from collections import defaultdict

def parse_words(lines):
    # lines is list !!
    # first parse words
    res_words = defaultdict(int)
    for line in lines:
        char_list = []
        findNonWord = False
        for char in line:
            if re.match("[a-z]", char) and not findNonWord:
                char_list.append(char)
            # finished parsing one word
            elif re.match("\s",char):
                # only add if that's a word length > 0
                # check the next comment
                if not findNonWord and len(char_list) > 0:
                    res_words[''.join(char_list)] += 1
                char_list = []
                findNonWord = False
            # not char nor whitespace 
            # wait until finding a whitespace
            # meaning that a new word is to begin
            else:
                findNonWord = True
                char_list = []
            
            # the end of line is also a whitespace, but not listed as \n as we're parsing it in str obj
            if char == line[-1] and not findNonWord and len(char_list) > 0:
                res_words[''.join(char_list)] += 1
                char_list = []
    
    res = []
    for key in sorted(res_words.keys()):
        res.append(key+" "+str(res_words[key]))

    return res

def parse_letters(lines):
    letters = dict(zip(string.ascii_lowercase, [0]*26))
    for line in lines:
        for char in line:
            if char in string.ascii_lowercase:
                letters[char] += 1

        res = []
    for key in sorted(letters.keys()):
        res.append(key+" "+str(letters[key]))

    return res

lines = sys.stdin.readlines()
print('words\n'+'\n'.join(parse_words(lines)))
print('letters\n'+'\n'.join(parse_letters(lines)))
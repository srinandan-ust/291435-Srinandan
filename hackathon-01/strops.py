#This module has the following functions

def getspan(s, r):
    count = 0
    spans = []
    start = 0
    while True:
        start = s.find(r, start)
        if start == -1:
            break
        end = start + len(r)
        spans.append((start, end))
        count += 1
        start += 1  # Move to the next character to find subsequent occurrences
    return count, spans 
# Input
#s = 'mississippi'
#r = 'ss'
 
def reverseWords(s):
    print(s[::-1])

def removePunctuations(stringe):
    string2 = ''
    #punctuation = "\".,\"'-?:!;"
    for item in stringe:
        if item.isalnum() or item == ' ':
            string2 = string2 + item          
    #print("Punctuation removed sentence: ") 
    print(string2)
#removePunctuations("He!11o! My #@@!##$#@#@#$@#$@#$hello")

def countWords(input_sentence):
    import re
    wordsreg = r'\w+'
    words = re.findall(wordsreg, input_sentence)
    return len(words)
#countWords2("This is for counting the words from this sentence")

def charactermap(word1):
    ch1 = {}
    for c in word1.lower():
        if c in ch1.keys():
            ch1[c] = ch1[c] + 1
        else:
            ch1[c] = 1
    return ch1
#word1 = "Aabbccdefff"
#charactermap(word1)

def makeTitle(string):
    import re
    rs = r'^[A-Z]'
    k = len(re.findall(rs,string))
    if(k == 1):
        print("The first letter is already capitalised")
    else:
        word_list = string.split()
        new_word = [word.capitalize() for word in word_list]
        capitalised_string = ' '.join(new_word)
        print("Capitalised: ",end = "")
        print(capitalised_string)
 #makeTitle("ahis sentence need to be titled")

def normalizeSpaces(input_sentence):
    no_space_list = []
    sFlag = False
    for item in input_sentence:
        if(item != ' '):
            no_space_list.append(item)
            sFlag = False
        elif not sFlag:
            no_space_list.append(' ')
            sFlag = True
    fixed_list = ''.join(no_space_list)     
    print("Sentence:", fixed_list)
#normalizeSpaces("     Check     this  list   with       excessive spaces")

def transform(string):
    list_of_strings = list(string)
    #print(list_of_strings)
    reversed_list = list_of_strings[::-1]
    reversed_sentence = "".join(reversed_list)
    new_sentence = reversed_sentence.swapcase()
    print("Translated/transformed sentence is:- ")
    print(new_sentence)
#transform("thIs Is A beAuTiFul day!!!")

def get_permutations(s, step=0, result=None):
    if result is None:
        result = []
    if step == len(s):
        result.append("".join(s))#append each word to a list
        return
    for i in range(step, len(s)):
        s_list = list(s)
        s_list[step], s_list[i] = s_list[i], s_list[step]  # Swap characters
        get_permutations(s_list, step + 1, result)  # Recursive call
    return list(set(result))
#permutations = permute("aaa") 
#print(permutations)
    
#Example usage
#permutations = get_permutations("aaa")
#print(permutations)

if __name__ == "__main__":
    # Test getspan
    string, substring = "mississippi", "ss"
    count, spans = getspan(string, substring)
    print(f"getspan('{string}', '{substring}'): ({count}, {spans})")
 
    # Test reverseWords
    s = "Reversethewords"
    print(f"reverseWords('{s}'): {reverseWords(s)}")
 
    # Test removePunctuation
    s = "Thi!is S$ent!e#n*c)e i%s f^ree of- Punc!tu&at+ions"
    print(f"removePunctuation('{s}'): {removePunctuation(s)}")
 
    # Test countWords
    s = "The number of words in this sentence should be 10"
    print(f"countWords('{s}'): {countWords(s)}")
 
    # Test characterMap
    s = "ALLAHABAD"
    print(f"charecterMap('{s}'): {characterMap(s)}")
 
    # Test makeTitle
    s = "srinandan"
    print(f"makeTitle('{s}'): {makeTitle(s)}")
 
    # Test normalizeSpaces
    s = "This     has  so      many        spaces"
    print(f"normalizeSpaces('{s}'): {normalizeSpaces(s)}")
 
    # Test transform
    s = "Hello"
    print(f"transform('{s}'): {transform(s)}")
 
    # Test getPermutations
    s = "ASSASSINATION"
    print(f"getPermutations('{s}'): {getPermutations(s)}")
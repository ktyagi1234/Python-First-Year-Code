#function that counts number of vowels in a given word

def countVowels(s):
    count = 0
    i = 0
    while( i < len(s)):
        if s[i].upper() == "A" or s[i].upper() == "E" or s[i].upper() == "I" or s[i].upper() == "O" or s[i].upper() == "U":
            count += 1
        i +=1
    
    return count
  
  
#print(countVowels("apple"))

#function that tests to see if a word has two of the same letter next to each other

def hasDoubleLetters(s):
    i = 0
    while i < len(s):
        if i != len(s) - 1:
            if s[i].upper() == s[i+1].upper():
                return True
            else:
                i += 1
        else:
            return False

#print(hasDoubleLetters("Aaron"))

#function that finds a common phrase of letters in two words

def lcp(s1,s2):
    word = ""
    if len(s1) < len(s2):
        mini = len(s1)
    else:
        mini = len(s2)
    
    for i in range(mini):
        if s1[i] == s2[i]:
            word = word + s1[i]
        else:
            break
    return word

#print(lcp("flow","flip"))


    







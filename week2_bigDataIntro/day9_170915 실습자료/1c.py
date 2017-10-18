import random

def computeLongestPalindrome(text):
    n = len(text)
    if n == 0:
        return 0
    elif n==1:
        return 1
    elif n > 1 and text[0]==text[-1]:
        return 2 + computeLongestPalindrome(text[1:-1])
    elif n > 1 and text[0] != text[-1]:
        return max(computeLongestPalindrome(text[0:-1]),
                   computeLongestPalindrome(text[1:-1]))
      #  computeLongestPalindrome(text[0:n-2])
      #  computeLongestPalindrome(text[1:n-1])
    
print 1, computeLongestPalindrome("")
print 2, computeLongestPalindrome("ab")
print 3, computeLongestPalindrome("aa")
print 4, computeLongestPalindrome("animal")



import random
numChars = 5
length = 400
random.seed(42)
text = ' '.join(chr(random.randint(ord('a'), ord('a') + numChars - 1)) for _ in range(length))

from collections import defaultdict
memory = defaultdict(int) #if memory[x] doesn't exist, default dict returns default value of int, which is 0
def cpl(text):
    n = len(text)
    if n == 0: return 0
    elif n == 1: return 1
    else:
        if text in memory:
            return memory[text]
        else:
            if text[0] == text[-1]:  #first letter and very last one match
                memory[text] = 2+ cpl(text[1:-1]) #2nd letter to second to last letter
            else:
                memory[text] = max(cpl(text[0:-1]), cpl(text[1:]))
            return memory[text]


print 'text =', text[:50]
print 5, cpl(text)
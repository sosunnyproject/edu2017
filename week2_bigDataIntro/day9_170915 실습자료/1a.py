
def computeMaxWordLength(text):
#1
    words = text.split()
#2
    #max_len = len(max(words))  #wrong bc max(words) returns the word that starts with last character in alphabetical order
    #print max_len

    #or...
    #max_len=0
    #for word in words:
    #   if len(word)>max_len:
    #       max_len=len(word)
    #print max_len
    #or....
    max_len = max([len(word) for word in words])

#3
    #sorting in max to min order, but not really necessary here...
    longest_words = [word for word in words if len(word) == max_len]

    #or...
    #longest_words = []
    #for word in words:
    #    if len(word) == max_len:
    #        longest_words.append(word)
    #print longest_words

    #or...
    #print [word for word in words if len(word) == max_len]

#4 SORT by alphabetical order
    longest_words =  sorted(longest_words, key= lambda x:x)

    #or...
    #longest_words =  sorted(longest_words, key=str.lower)   #also alphabetical order

#5
    return longest_words[-1]


print 1, computeMaxWordLength('which is the longest word')
print 2, computeMaxWordLength('a b cat sun dog')
print 3, computeMaxWordLength(' '.join(str(x) for x in range(100000)))
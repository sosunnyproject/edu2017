def computeMostFrequentWord(text):

    words = text.split()   #string of words

#dictionary type :: storing w : freqNum
    word_freqs = {}
    '''
    for w in words:
        if w not in word_freqs.keys():
            word_freqs[w] = 1
        else :
            word_freqs[w] += 1
    '''
    #using get function
    for w in words:
        word_freqs[w] = word_freqs.get(w, 0) + 1
        #word_freqs[w] = 1 if word_freqs.get(w,0) == 0 else word_freqs[w]+1

#max value
    max_cnt = max(word_freqs.values())


#find the most frequent words - can be multiple
    # word_freqs.keys () = max_cnt
    frequent_words = set()
    #for w in word_freqs:
    #    if word_freqs[w] == max_cnt:
    #        frequent_words.add(w)

    for word, freq in word_freqs.items():
        if freq == max_cnt:
            frequent_words.add(word)

    return (frequent_words, max_cnt)


#    mostFreqWord = [w for w in word_freqs if word_freqs[w] == max_cnt]
#    freqStr = ', '.join(mostFreqWord)
    #finalStr = freqStr + ", " + str(max_cnt)

#    return (freqStr, max_cnt)

print 1, computeMostFrequentWord('the quick brown fox jumps over the lazy fox')
print 2, computeMostFrequentWord('the quick brown fox jumps over the lazy dog')
import math, collections

SENTENCE_BEGIN = '-BEGIN-'

corpus = [
    'I am Sam',
    'Sam I am',
    'I do not like green'
]
    
# Counting
unigram_counts = collections.defaultdict(int)

# BEGIN_YOUR_CODE
for sentence in corpus:
    sentence = SENTENCE_BEGIN + " " + sentence
    for word in sentence.split():
        unigram_counts[word] += 1

def unigram(word):
    return float(unigram_counts[word]) / sum(unigram_counts.values())

#BIGRAM
bigram_counts = collections.defaultdict(int)
for sentence in corpus:
    sentence = SENTENCE_BEGIN + " " + sentence
    for n in range(len(sentence.split())-1):
        #while n + 1 < len(sentence.split()): #while loop not necessary bc len - 1
        #print sentence.split()[n], sentence.split()[n+1]
        bigram_counts[(sentence.split()[n], sentence.split()[n+1])] += 1
        #n += 1
print bigram_counts
# END_YOUR_CODE
        
# Bigram function
def bigram(prev_word, curr_word):
    # BEGIN_YOUR_CODE
    raw_p = float(bigram_counts[(prev_word, curr_word)]) / float(unigram_counts[prev_word])
    return raw_p
    # END_YOUR_CODE

# Printing results
print('\n- Probabilities - ')
print('* (-BEGIN-, I) = %f'%bigram(SENTENCE_BEGIN, 'I'))    
print('* (-BEGIN-, Sam) = %f'%bigram(SENTENCE_BEGIN, 'Sam'))    
print('* (I, do) = %f'%bigram('I', 'do'))
print('* (like, green) = %f'%bigram('like', 'green'))

# Bigram function (negative loglikelihood)
def bigram2(prev_word, curr_word):
    # BEGIN_YOUR_CODE
    logResult = -math.log(bigram(prev_word, curr_word))
    return logResult
    # END_YOUR_CODE

#closer to 0, higher the likelihood
print('\n- Negative loglikelihood - ')
print('* (-BEGIN-, I) = %f'%bigram2(SENTENCE_BEGIN, 'I'))    
print('* (-BEGIN-, Sam) = %f'%bigram2(SENTENCE_BEGIN, 'Sam'))    
print('* (I, do) = %f'%bigram2('I', 'do'))
print('* (like, green) = %f'%bigram2('like', 'green'))


'''
for sentence in corpus:
    words = [SENTENCE_BEGIN] + sentence.split()
    #unigram
    for word in words:
        unigram_counts[word] += 1
    #bigram
    for idx in range(len(words) - 1):
        bigram_counts[(words[idx], words[idx+1])] += 1
'''

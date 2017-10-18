
#practice set 8

def letter_dict(sentence):
    ch_dict = {}
    for w in sentence:
        if (w in ch_dict):
            ch_dict[w] += 1
        else:
            ch_dict[w] = 1
    #keys = list(ch_dict.keys())
    #vals = list(ch_dict.values())
    return ch_dict
    #print(max(vals))
    #max_k = keys[max(vals)]
    #print(max_k)


def max_letter(letter_dict, sentence):
    #make dictionary of num: chars
    same_nums = {}
    for ch in letter_dict:
        if letter_dict[ch] in same_nums:
            same_nums[letter_dict[ch]].append(ch)
        else:
            same_nums[letter_dict[ch]] = [ch]
    #print(same_nums)

    same_num_keys = list(same_nums.keys())
    #find max number
    max_keys = max(same_num_keys)
    #find the values in that max num key
    max_chars = same_nums[max_keys]

    each_by_order = []
    for i in range(len(max_chars)):
        each = max_chars[i]
        ind = sentence.index(each)
        print("index of", each, ":", ind)
        each_by_order.insert(ind, each)
    # find the index of max_chars in sentence
    # minimum index
    first_max_ch = min(each_by_order)
    return(first_max_ch)


def add_dict(dict1, dict2):
    c = dict1
    origin_keys = list(dict1.keys())
    for i in b:
        #if key is already in a, add values
        if i in origin_keys:
            c[i] = c[i] + b[i]   #add values in b's i key to c's i key
        #else, add key to a {}
        else :
            c[i] = 1   #create i key in c dict
    return(c)



a = letter_dict('red apple')
print("original string:", a)

m = max_letter(a, "red apple")
print("maximum first letter in the sentence:", m)

b = letter_dict('yellow banana')
c = add_dict(a,b)
new_str = "red apple" + "yellow banana"
print(c)
print("maximum first letter:", max_letter(c, new_str))
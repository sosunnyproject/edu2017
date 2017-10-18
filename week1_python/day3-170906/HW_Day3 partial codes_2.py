#coding=utf-8
#Dictionary
#딕셔너리 실습문제
"""
sentence = input("Enter a sentence: ")
#sentence 문자 하나하나 for loop 돌려서 분해
letter_dict = {}
for w in sentence:
    if (w in letter_dict):
        letter_dict[w] += 1
    else:
        letter_dict[w] = 1

print(letter_dict)

#Chapter: FILE
#problem_set1
# file input, dictionary, num of word frequencies

f = open("test.txt", "r")
#word: frequency

data = f.read()
#data is string type
data_ls = data.split()
print(data_ls)

diction = {}
for word in data_ls:
    if(word in diction):
        diction[word] += 1
    else:
        diction[word] = 1
print(diction)

for key in diction:
    print(key, diction[key])


#-------------------------
#딕셔너리 docx 실습문제2
L1 = ['one', 'two', 'three', 'four']
L2 = [1, 2, 3, 4]
print(dict(zip(L1, L2)))

#딕셔너리 docx 실습문제1
d = {'youn': 1, 'park': 2, 'kim': 10}
print(d.values())
for v in d.values():
    print(v, end=" ")

#딕셔너리 docx 실습3 알파벳기준정렬
{'one':1, 'two':2, 'three':3, 'four':4, 'five':5}

#sort - alpha_order
origin_d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
list_d = list(origin_d)
alpha_d = sorted(list_d)
#for loop - dictionary[key] = value
for ele in alpha_d:
    print(ele, origin_d[ele])
"""
#파일 챕터 docx 실습4

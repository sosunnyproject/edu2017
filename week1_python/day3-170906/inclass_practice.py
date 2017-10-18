#coding=utf-8
"""
ls = []
for i in range(1,6):
    ls.append(i)

print(ls)

print([i for i in range(1,6)])
print(max(ls))

L1 = [1,2,3]
L2 = [4,5,6]
for_append = [x*y for x in L1 for y in L2]
#append 하는 방법 - 매우 유용. 기존 append보다 빠름
print(for_append)
#outer for loop - 1 2 3
#inner for loop - 4 5 6
# 1 - 4,5,6 / 2 - 4,5,6 / 3 - 4,5,6
# 4,5,6/ 8, 10, 12 / 12, 15, 18

#tuple
t = ()
print(type('t'))
#list, tuple 자료형 서로 바꿀 수도 있음
ls = [1,2,3]
ls_t = tuple(ls)
print(ls)
print("this is now tuple: ", ls_t)
a, b, c = ls_t
x, y, z = ls
print(a,b,c,x,y,z)

t = tuple(range(1,7))
print(t)
#tuple to list
l = list(t)
print(l)

#* with tuple: repeats inner elements inside tuple
print(t*3)

#집합 set - auto deletes any repetitive elements
s1 = set([1,2,3,2,1,35,67,3,4])
print(s1)

s2 = {3,4,5}
print(type(s2))

word = "Hello" *2
word_ls = list(word)
print(word_ls)

set_word = set(word_ls)
print(set_word)

s4 = set("Hello")
print(s4)

s = {1,2,3,4,5,6,7}
s.discard(7)

#dictionary
d = {}
print(type(d))
d["kim"] = 3
d["park"] = 5
d["lee"] = 4
d["kang"] = 1
d["jeon"] = 2
print(d)
print(d["park"])
#doesn't really have special order rule
print(d.keys())
print(d.values())
print(d.items()) #tupe형태로 쌍으로 묶어서 리스트로 반환함
print('kim' in d)
print(d['kim'])

del d['kim']
print(d)
d.clear()
print(d)
"""


#파일읽기
f = open("input.txt", "r+")
for i in range(1,6):
    data = "%d line\n" % i
    f.write(data)
#read first line (following the file cursor)
f.close()










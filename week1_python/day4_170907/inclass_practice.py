#coding=utf-8
import random
'''
def add(a,b):
    result = a+b
    return result

#len() 구현
def my_len(l):
    length = 0
    for i in l:
        length += 1
    return length

print(my_len([4,5,6,6]))

def sub(a,b):
    result = a-b
    return result

def mul(a,b):
    result = a*b
    return result

def div(a,b):
    result = a/b
    return result

a=1
b=2
a = add(a,b)
s = sub(a,b)
m = mul(a,b)
d = div(a,b)
print(a,s,m,d)


def count_even_vv(*n):
    cnt = 0
    for v in n:
        if v%2 == 0:
            cnt += 1
    return cnt

def count_even_list(n):
    cnt = 0
    for v in n:
        if v % 2 == 0:
            cnt += 1
    return cnt

cnt_even=count_even_vv(1,2,3,4)
cnt_even2 = count_even_list([1,2,3,4])
print(cnt_even)
print(cnt_even2)


def Factorial(num):
    fact = 1
    for n in range(1, num+1):
        fact = fact * n
    return fact
random.sample(list(range(1, 46)), 6)

print(Factorial(5))

def pow(n,a):
    result =n**a
    return result
print(pow(3,5))

def printName(firstName, secondName="Lee"):
    print('my name is', firstName, '', secondName + '.')

printName('Chulsoo', 'Kim')
printName('Chulsoo')

a = 3
b = 4
def sum_and_mul(a,b):
    return(a+b, a*b)
sum, mul = sum_and_mul(a,b)
print(sum)
print(mul)

def hour_min_sec(second):
    min = second//60
    sec = second%60
    if (min>=60):
        hour = min//60
        min = min%60
    print(hour, "hour,", min, "min,", sec, "seconds")
    return hour, min, sec

print(hour_min_sec(57894))

l = [3,5,9,1,2]
def get_min_max(l):
    mini = min(l)
    maxi = max(l)
    l.remove(mini)
    l.remove(maxi)
    return mini, maxi


min, max = get_min_max(l)
print(min, max, l)
'''

#lottery
lottery = random.sample(list(range(1,46)), 6)
print(lottery)




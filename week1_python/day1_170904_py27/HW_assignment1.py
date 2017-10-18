#coding=utf-8

#1

a = 5
b = 8
mul = a*b
print("%d * %d = %d" %(a, b, mul))

#2
x = 10
y = 20
print("Before - x: %d , y : %d" %(x,y))
z = x
x = y
y = z
print("After - x: %d, y: %d" % (x,y))

s1 = "read apple"
s2 = "yellow banana"
s3 = s1[:3] + " " + s2[7:]
print(s3)
s4 = s2[:7] + s1[5:]
print(s4)

import math

# 원의 반지름
pi = math.pi
radius = input("반지름을 입력하시오: ")
circumf = 2 * radius * pi
area = pi * radius**2
print("원 둘레: %.2f" % circumf)
print("원 넓이: %.2f" % area)

number = raw_input("실수를 입력하시오: ")
realnum = float(number)
intnum = int(realnum)
decimal = realnum - intnum
print("정수부: %d " %intnum)
print("실수부: %.2f " %decimal)

#sentence into a list of chars
sentence=raw_input("한 문장을 입력하시오: ")
a = ','
s1 = a.join(sentence)
s2 = s1.split(',')
print(s2)
#you can also do this : list(sentence)

numbers = raw_input("Enter two integers: ")
numSplit = numbers.split()
num1 = int(numSplit[0])
num2 = int(numSplit[1])
print("%d + %d = %d" %(num1, num2, num1+num2))
print("%d - %d = %d" %(num1, num2, num1-num2))
print("%d * %d = %d" %(num1, num2, num1*num2))
print("%d / %d = %d" %(num1, num2, num1/num2))
print("%d %% %d = %d" %(num1, num2, num1 % num2))


#sum and average
twoIntString = raw_input("Enter two integers: ")
twoIntArray = twoIntString.split()
int1 = int(twoIntArray[0])
int2 = int(twoIntArray[1])
intf1 = float(twoIntArray[0])
intf2 = float(twoIntArray[1])
print("The sum of %d and %d is %d" %(int1, int2, int1+int2))
print("The average of numbers is %.1f" % ((intf1+intf2)/2))

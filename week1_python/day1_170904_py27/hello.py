#coding:utf-8

#python2 version
'''this is
commented
out'''

print"hello"
print"안녕"

number = raw_input("Enter a number: ")
print(number)
print(type(number))


print("You entered: %d " % int(number))
ty = type(number)
print("Your input's type is: %s " % ty)

print "life " "is " "too short"
print "life"+" is"+" too short"
print "life", "is", "too short"

a = 100
b = 200
sum = a + b
print a,"+", b, "=", sum
print "python " * 3

num = 10
day = "two"
print "I eat %d apples" % 3
print "I ate %d cups of coffee, so I got sick for %s days." % (num, day)
# %s can accept any types - int, float, string

temp = 24.15234
print "Today's temperature is %.2f degree celsius" % temp

#실습문제1

print("\n")
print("-" * 50)
print("실습문제1")

tempF = input("화씨온도를 입력하세요: ")
tempC = (tempF-32) * 5.00/9.00
print"화씨온도: %f" %tempF
print"섭씨온도: %.10f" %tempC

#실습문제2
print("\n")
print("-" * 50)
print("실습문제2")

insert = input("투입한 돈은 얼마입니까? ")
price = input("물건 가격은 얼마입니까? ")
change = insert - price
fiveH = change // 500
oneH = (change - fiveH*500) // 100

print("투입한 돈: %d" %insert)
print("물건 값: %d" %price)
print("거스름돈: %d" %change)
print("500원짜리: %d 개" %fiveH)
print("100원짜리: %d " %oneH)

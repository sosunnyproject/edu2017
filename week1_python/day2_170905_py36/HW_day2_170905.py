#coding=utf-8
"""
#조건문 실습1
eng_score=int(input("영어 점수 입력: "))
math_score =int(input("수학 점수 입력: "))
if ((eng_score+math_score)>=110):
    if (eng_score < 40):
        print("불합격: 영어 점수 부족")
    elif (math_score < 40):
        print("불합격: 수학 점수 부족")
    else: print("합격")
else :
    print("불합격: 총합 점수 부족")
"""
"""
#조건문 실습 2
nums=[]
print("세 개의 정수를 입력하시오: ")
for i in range(3):
    lines = input()
    nums.append(lines)
a,b,c = list(map(int, nums))
if (a>=b):
    if (a>=c):
        print("가장 큰 수는", a, "입니다.")
    elif (c>=a):
        print("가장 큰 수는", c, "입니다.")
elif (b>=a):
    if (b>=c):
        print("가장 큰 수는", b, "입니다.")
    elif (c>=b):
        print("가장 큰 수는", c, "입니다.")



#반복문 실습2 별 그리기
stars = input("4자리 자연수를 입력하세요: ")
for n in stars:
    print (int(n) * "*")

for i in stars:
    s = ""
    for x in range(int(i)):
        s = "*" + s
    print(s)

''''
num_star=list(map(int, stars))
print("*" * num_star[0])
print("*" * num_star[1])
print("*" * num_star[2])
print("*" * num_star[3])
'''

#input - midterm score
mid = input("Enter your midterm score: ")
#input - final score
fin = input("Enter your final score: ")
# mid + final /2
avg = (float(mid) + float(fin)) /2
print("Average: ", avg)
if avg >= 90:
    print("Grade: A")
elif 80 <= avg < 90:
    print("Grade: B")
elif 70 <= avg < 80:
    print("Grade: C")
elif 60 <= avg < 70:
    print("Grade: D")
else:
    print("Grade F")


number = input("Enter a num: ")

if (int(number) % 2 == 0):
    print(number, "is an even number")
else:
    print(number, "is an odd number")


word = input("enter a word: ")
a = 0
while a < len(word):
    print(word[a])
    a += 1

word = input("enter a word: ")
for x in word:
    print(x)

for i in range(10,0,-1):
    print(i, end=",")
print("Happy new year!!")


nums = input("Enter two integers: ")
a, b = map(int, nums.split())
sum = 0
if (a <= b):
 for x in range(a, b+1):
     print(x)
     sum = x + sum
 print("The sum from", a, "to", b, "is", sum)

else:
    print("The first integers can't be bigger than b")

word = input("Enter a word: ")
sum = 0
for x in word:
    #if true, a becomes 1.
    # add it to return var
    a = ('a'==x)
    sum = sum + a
print("Total number of 'a':", sum)


for x1 in range(0,10):
     print(x1, end=" ")
print("")
for x2 in range(0, 55, 5):
     print(x2, end=" ")
print("")
for x3 in range(10, 0, -1):
     print(x3, end=" ")


colors = ["red", "green", "blue"]

for x in colors:
    print(x)


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for num in a:
    if (num%2 == 0):
        print(num, end=" ")

# 9*9
n = input("출력하고 싶은 단을 입력하세요: ")
for x in range(1,10):
    print(n, "*", x, "=", int(n)*x)

for a in range(1,10):
    print("")
    for b in range(1,10):
        print(b, "*", a, "=", a*b, end="\t")

sentence = input("Enter a sentence: ")
i = 1
while i < len(sentence.split()):
    for x in sentence.split():
        print("word", i, x)
        i += 1
"""
result = []
while True:
    untilDone = input("Enter a number: ")
    if untilDone != "done":
        result.append(float(untilDone))
    else:
        break
average = sum(result) / len(result)
print("Average: ", average)
print("Maximum: ", max(result))
print("Minimum: ", min(result))

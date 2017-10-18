#coding:utf-8

w = "012345"
print(w[:])
print(w[::-1])
print(w[1:5:-1])
print(w[-1:-5:-1])
print(w[:3])
print(w[2:])
print(w[::2])
print(w[-1:-5:2])

# value 'in' data


#string related functions
#len, count, index, join, split


#실습문제3



#리스트
lst = range(1,10)
print(lst)
#list in list
lst_1 = [1,2,3,4,5,6,7,8,9,[10,11,12]]
print lst_1

cities = ['seoul', 'incheon', 'suwon', 'yongin', 'pohang','busan']
print(cities[0])
print(cities[1:5])
print(cities[::-1])
# 멤버 확인 - true, false - in, not in
print('seoul' in cities)
print('daejeon' not in cities)


#실습문제4
date = input("날짜를 입력하세요(연/월/일 형식대로): ")


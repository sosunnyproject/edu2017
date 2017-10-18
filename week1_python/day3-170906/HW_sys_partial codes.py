#coding=utf-8
import sys
# sys 파일 실습문제

sentence = sys.argv[1:]
endstr = []
for word in sentence:
    ch = word.upper()
    endstr.append(ch)
result=' '.join(endstr)
print(result)

#-------------------------------------
#FILE docx 실습문제2- all upper case
import os

filename = input("Enter a file name: ")
if os.path.exists(filename):
    f2 = open(filename, "r")
    data2 = f2.read()
    print(data2.upper())
else: print("That file does not exist.")
f2.close()


#------------------------------
args = sys.argv[1:]
f = open(args[0],"r")
#counting num of lines

#num_words=0
data = f.read()
num_words = len(data.split())
f.seek(0)
num_lines = 0
for line in f:
    num_lines += 1

print(num_lines, num_words)
f.close()


#src.txt copy to dst.txt
inputs = sys.argv[1:]
#argv[0] = ex4.py
#argv[1] = inputs[0] = src.txt
#argv[2] = inputs[1] = dst.txt
src = open(inputs[0], "r")
copy = src.read()
dst = open(inputs[1], "w")
dst.write(copy)
src.close()
dst.close()


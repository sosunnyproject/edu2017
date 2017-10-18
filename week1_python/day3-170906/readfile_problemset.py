
f = open("input.txt", "r")
print(f.tell())

line = f.readline()
print("line: ",line, end=" ")
print(f.tell())
#read lines after the first one (file pointer is there)


lines = f.readlines()
#print(lines[0][:-1])
for i in lines:
    print(i[:-1])

#print("lines: ", lines)

d = f.read()
print(d)
f.close()

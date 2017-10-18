import sys

#global
#f = open("students.txt", "r")
#lines = f.readlines()
#f_name = sys.argv[1]
#if(f_name == "students.txt" or ""):
f = open("students.txt", "r")
#lines = f.readlines()
#else:
 #   print("Do you mean students.txt?")

#each_line: ID = [name, mid, final]
#f = open("students.txt", "r")
stu_list = f.readlines()
total_stu = []
for stu in stu_list:
    stu = stu[:-1].split("\t")  #store each row data into single array
    total_stu.append(stu)    #append all rows into array
print(total_stu)

row = ['20170002', 'Lee Jieun', '92', '89']
print(total_stu[0])
i = total_stu.index(row)
print(i)
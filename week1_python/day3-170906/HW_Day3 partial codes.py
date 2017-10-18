#파일 docx 실습 5 : score.txt report.txt
score = open("score.txt", "r")
row_score = ['ID', 'midterm', 'final']
report = open("report.txt", "w")

lines = score.readlines()

#splitting data in score.txt
total = []
for line in lines[:]:
    splited = line[:-1].split()
    each_dict = dict(zip(row_score, splited)) # each student's dictionary
    total.append(each_dict)  #total list of dictionary of students

#writing on report.txt
for n in range(len(total)):
    #using each element in a row
    mid = total[n]['midterm']
    fin = total[n]['final']
    avg = (float(mid)*40/100) + (float(fin)*60/100)
    grade=""
    if avg >= 90:
        grade="A"
    elif 80 <= avg < 90:
        grade="B"
    elif 70 <= avg < 80:
        grade ="C"
    elif 60 <= avg < 70:
        grade ="D"
    else:
        grade ="F"
    grade = "(" + grade + ")"

    #writing a list of each student
    oneStudent = []
    oneStudent.append(total[n]['ID'])
    oneStudent.append(mid)
    oneStudent.append(fin)
    oneStudent.append(str(round(avg,2)))
    oneStudent.append(grade)
    #combine a list into a string
    oneLine = ' '.join(oneStudent) +"\n"
    #write on report.txt
    report.write(oneLine)
score.close()
report.close()
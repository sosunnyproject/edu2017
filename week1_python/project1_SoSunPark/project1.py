import sys
import os
import math

copy_origin = [] #listinlist of old origin text - id, name, midterm, final


def openText(filename):
    if(filename == "students.txt" or ""):
        f = open("students.txt", "r")
        lines = f.readlines()
        return lines
    else:
        print("Do you mean students.txt?")

def copyGlobal(list):
    for stu in list:
        stu = stu[:-1].split("\t")  # store each row data into single array
        copy_origin.append(stu)  # append all rows into array
    return copy_origin

#----------------------------------
def newList(list):

    total_stu = []              #local variable
    for splited in list:

        studentID, name = splited[0], splited[1]
        mid, fin = splited[2], splited[3]
        avg = (float(mid) + float(fin))/2
        str_avg = str(round(avg, 1))        #only first decimal point

        if avg >= 90.0:
            grade = "A"
        elif 80.0 <= avg < 90.0:
            grade = "B"
        elif 70.0 <= avg < 80.0:
            grade = "C"
        elif 60.0 <= avg < 70.0:
            grade = "D"
        else:
            grade = "F"

        #store each student data in single_stu list
        single_stu = []
        single_stu.append(studentID)
        single_stu.append(name)
        single_stu.append(mid)
        single_stu.append(fin)
        single_stu.append(str_avg)
        single_stu.append(grade)

        #append to a larger list
        total_stu.append(single_stu)

    #sort entire list in reverse order by average value
    ordered_stu = sorted(total_stu, key=lambda s : float(s[4]), reverse=True)
    return ordered_stu

def show(list):
    print("Student" + "\t\t" + "Name" + "\t\t" + "Midterm" + "\t" + "Final" + "\t" + "Average" + "\t" + "Grade")
    print("---" * 23)
    for stu in list:
        #each student data list into string
        student = "\t".join(stu)
        print(student)

def changescore():
    global copy_new
    global copy_origin
    ask_id = input("Student ID: ")
    save_row = []

    #find student from copy_origin
    for stu_list in copy_origin:
        if(stu_list[0] == str(ask_id)):
            save_row = stu_list

    if (save_row != []):

        # find student from copy_new before changescore
        IDlist = []
        for i in range(len(copy_new)):
            id = copy_new[i][0]
            IDlist.append(id)

        new_index = 0     # store original index from copy_new
        if ask_id in IDlist:
            new_index = IDlist.index(ask_id)
        print_old = list(copy_new[new_index])
        str_old = '\t'.join(print_old)

        # ask midterm or final
        ask_test = input("Type Midterm or Final: ")
        ask_test = ask_test.lower()

        # ask score
        ask_score = input("score: ")
        index = copy_origin.index(save_row)

        ask_scoreFloat = float(ask_score)
        if (0.0<=ask_scoreFloat<=100.0):
            print("Student Added.")

            #if midterm, index 2. if final, index 3
            if (ask_test == "midterm"):
                copy_origin[index][2] = ask_score
            elif (ask_test == "final"):
                copy_origin[index][3] = ask_score
            else:
                print("You put wrong data in test name. Please start again.")
                order()
        else :
            print("wrong score range. Start again.")
            order()

        copy_new = newList(copy_origin)

        #find student data row from copy_new after changescore
        newIDlist = []
        for i in range(len(copy_new)):
            id = copy_new[i][0]
            newIDlist.append(id)

        new_ind = 0
        if ask_id in newIDlist:
            new_ind = newIDlist.index(ask_id)
        print_new = copy_new[new_ind]
        str_new = '\t'.join(print_new)

        print("Student" + "\t\t" + "Name" + "\t\t" + "Midterm" + "\t" + "Final" + "\t" + "Average" + "\t" + "Grade")
        print("---" * 23)
        print(str_old)
        print("SCORE CHANGED")
        print(str_new)

    else:
        print("No Such Person.")

def add():
    global copy_new
    ask_id = input("Student ID: ")

    yes = 0
    for i in range(len(copy_new)):
        if (ask_id == copy_new[i][0]):
            yes += 1
    if (yes != 0):
        print("Already exists.")
    else:
        #add info to copy_origin
        ask_name = input("Name: ")
        ask_mid = input("Midterm score: ")
        ask_final = input("Final score: ")
        #change string type score values into float
        ask_midFloat = float(ask_mid)
        ask_finalFloat = float(ask_final)
        if (0.0<=ask_midFloat<=100.0 and 0.0<=ask_finalFloat<=100.0):
            copy_origin.append([ask_id, ask_name, ask_mid, ask_final])
            print("Student Added.")
        else :
            print("wrong score range.")
            order()
    copy_new = newList(copy_origin)
    order()

def searchgrade():
    global copy_new
    ask_grade = input("Grade to search: ")
    if ask_grade not in ['A', 'B', 'C', 'D', 'F']:
        print("No such grade. Please try again.")
        order()
    else:
        match_list = []
        for i in range(len(copy_new)):
        #[ [stu1], [stu2], ... ]
            if (copy_new[i][5] == ask_grade):
                single_stu = '\t'.join(copy_new[i])
                match_list.append(single_stu)
        match_str = '\n'.join(match_list)
        if (match_list ==[]):
            print("No Results.")
        else:
            print(match_str)
    order()

def search():
    ask_id = input("Student ID: ")

    #making a list with IDs only
    IDlist = []
    for i in range(len(copy_new)):
        id = copy_new[i][0]
        IDlist.append(id)

     # store original index from copy_new
    if ask_id in IDlist:
        id_index = IDlist.index(ask_id)
        stu_data = copy_new[id_index]
        stu_str = '\t'.join(stu_data)
        print(stu_str)
    else:
        print("No such person")
    order()


def remove():
    global copy_origin, copy_new
    if (copy_new == []):
        print("List is empty.")
    else:
        ask_id = input("Student ID: ")
        #making list of IDs only from copy_new
        IDlist = []
        for i in range(len(copy_origin)):
            id = copy_origin[i][0]
            IDlist.append(id)

        index = 0  # store original index from copy_new
        if ask_id in IDlist:
            index = IDlist.index(ask_id)
            copy_origin.remove(copy_origin[index])
        else:
            print("No Such Person.")

    #update data
    copy_new = newList(copy_origin)
    order()

def quit():
    ask_quit = input("Save data?[yes/no]: ")
    ask_quit = ask_quit.lower()
    if ask_quit == "yes":
        #copy_origin save
        stu_data = []
        for i in range(len(copy_origin)):
            stu_line = '\t'.join(copy_origin[i])
            stu_data.append(stu_line)
        stu_txt = '\n'.join(stu_data)
        print("Data below will be saved to your new file.")
        print(stu_txt)

        ask_filename = input("File name (no need to write .txt) : ")
        ask_filename = ask_filename + ".txt"
        newfile = open(ask_filename, "w")
        newfile.write(stu_txt)
        newfile.close()
        print("File saved. Bye...")
    elif ask_quit == "no":
        print("Not quitting.")

    else:
        print("I don't understand what you just said. Please answer yes or no.")
        quit()


def order():
    keyword = input("#: ")
    keyword = keyword.lower()
    if(keyword == "show"):
        updated = newList(copy_origin)
        show(updated)
        order()
    elif(keyword == "changescore"):
        changescore()
        order()
    elif (keyword == "search"):
        search()
        order()
    elif (keyword == "add"):
        add()
        order()
    elif (keyword == "searchgrade"):
        searchgrade()
        order()
    elif (keyword == "remove"):
        remove()
        order()
    elif (keyword == "quit"):
        quit()
    else:
        order()

f_name = sys.argv[1]
original_lines = openText(f_name)
copyGlobal(original_lines) #return copy_origin
copy_new = newList(copy_origin) #return copy_new
show(copy_new) #show student data at first time
order()  #start keyword orders



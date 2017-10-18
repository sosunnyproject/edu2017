class Person:

    name =""
    age = 0
    department =""

    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.department = dept

    def get_name(self, name):
        return self.name

class Professor(Person):

    stuList = []
    stuStr= ""

    def __init__(self, name ="", age=0, dept="", position="", lab=""):
        Person.__init__(self, name=name, age=age, dept =dept)
        self.position = position
        self.lab = lab

    def reg_student(self, stu):
        self.stuList.append(stu.name)
        self.stuStr = ', '.join(self.stuList)
        return self.stuStr

    def printing(self):
        print "My name is " + self.name + ", age is " + str(self.age) \
                  + ", department is " + self.department + ", advising " + self.stuStr


class Student(Person):

    #advisor = Professor()

    def __init__(self, name = "", age = 0, dept ="", id=0, gpa=0.0):
        Person.__init__(self, name = name, age = age, dept = dept)
        self.id = id
        self.gpa = gpa

    def reg_advisor(self, prof):
        self.advisor = prof.name

    def printing(self):
        print "My name is " + self.name + ", age is "+ str(self.age) \
              + ", department is " +  self.department +\
              ", advisor is " + self.advisor



stu1 = Student("Kim", 30, 'Computer',20001234, 4.5)
stu2 = Student("Park", 22, "Statistics",20101234, 0.5)
prof1 = Professor('Lee', 55, 'Computer', 'Full', 'KLE')
stu1.reg_advisor(prof1)
stu2.reg_advisor(prof1)
prof1.reg_student(stu1)
prof1.reg_student(stu2)
stu1.printing()
stu2.printing()
prof1.printing()
class Set:

    member = []

    def __init__(self, member):
        self.member = member

    def append(self, a):
        #a is num. has to be in list to be added.
        if a in self.member:
            print "already exists"
        else:
            self.member.extend([a])
        return self.member

    def delete(self, a):
        self.member.remove(a)
        return self.member

    def union(self, s2):
        return self.member + s2.member

        #or...
        #self.member.extend(s2.member)
        #return self.member

    def __add__(self, s2):
       return self.union(s2)

    def difference(self, s2):
        for i in range(len(s2.member)):
             if s2.member[i] in self.member:
                 self.member.remove(s2.member[i])
        return self.member

    def __sub__(self, s2):
        return self.difference(s2)

    def intersection(self, s2):
        bothArr = []
        for i in range(len(s2.member)):
            if s2.member[i] in self.member:
                bothArr.append(s2.member[i])
        return bothArr

    def __div__(self, s2):
        return self.intersection(s2)


a = Set([1,2,3])
b = Set([2,3,4])

print "a member: ", a.member
print "append: ", a.append(1)
print "delete: ", a.delete(2)

u = a.union(b)
print "union: ", u

d = a.difference(b)
print "difference", d

b.append(3)
b.append(2)
b.append(1)
print "new b: ", b.member
print "intersection"
e = a.intersection(b)
print e

div = a / b
print "overload  /", div

minus = a-b
print "overload -", minus

plus = a+b
print "overload +", plus



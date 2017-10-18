import collections

def manhattanDistance(loc1, loc2):
    # BEGIN_YOUR_CODE
    '''
    print 'p1-dim0', loc1[0]
    print 'p1-dim1', loc1[1]
    print 'p2-dim0', loc2[0]
    print 'p2-dim1', loc2[1]
    '''

    '''
    length1 = len(loc1)
    length2 = len(loc2)

    if length1 == length2:
        manDis = 0
        for i in range(length1):
            manDis += abs(loc1[i] - loc2[i])
        return manDis
    else: print("your location sizes are different")
    '''

    '''
    #when you want to give error message
    assert len(loc1) == len(loc2)
    #gives assertionError    
    '''
    #alternative, shorter than for loop above
    return sum([abs(loc1[dim] - loc2[dim]) for dim in range(len(loc1))])

    #below return is just for 2dim manhattan distance
    #return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])


print 1, manhattanDistance((0, 0), (5, 5))
print 2, manhattanDistance((2, 3), (2, 3))
print 3, manhattanDistance((3, 5), (1, 9))
print 4, manhattanDistance((3, 5, 7), (1, 9, 2))
print 5, manhattanDistance((3,), (1,))
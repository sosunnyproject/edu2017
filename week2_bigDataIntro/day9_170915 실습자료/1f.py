import collections

def sparseVectorDotProduct(v1, v2):
    '''
    k1 = v1.keys()
    k2 = v2.keys()
    dim = 0
    for k in k1:
        #for keys that match in k1 and k2
        if k in k2:
            dim += v1[k] * v2[k]
        else:
            dim += 0
    return 
    '''

    #x in dict --> automatically finds x among dict's keys()
    #nonexisiting keys are 0 by default bc of defaultdict properties
    return sum(v1[key]*v2[key] for key in v1)
    #return v1['a']*v2['a'] + v1['b']*v2['b'] + v1['c']*v2['c']
    
v1 = collections.defaultdict(float, {'a': 5}) #default value: 0. b = 0
v2 = collections.defaultdict(float, {'b': 2, 'a': 3})
print 1, sparseVectorDotProduct(v1, v2)

v1 = collections.defaultdict(float, {'c': 5})  #returns 0
v2 = collections.defaultdict(float, {'b': 1, 'a': 2})
print 2, sparseVectorDotProduct(v1, v2)

v1 = collections.defaultdict(float, {'a': 5, 'b': 4})
v2 = collections.defaultdict(float, {'b': 2, 'a': -1})
print 3, sparseVectorDotProduct(v1, v2)

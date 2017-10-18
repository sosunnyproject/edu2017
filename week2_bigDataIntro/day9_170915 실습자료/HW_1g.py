import collections

def incrementSparseVector(v1, scale, v2):
    # BEGIN_YOUR_CODE
    v2_dict = collections.defaultdict(float, {})
    # scale * v2
    for key in v2:
        v2_dict[key] =(scale * v2[key])

    # + v1
    final_dict = v2_dict
    for key in v1:
        final_dict[key] = final_dict.get(key, 0) + v1.get(key, 0)

    result = []
    for k, f in final_dict.items():
         result.append((k, f))
    return result
    #return final_dict
    # return
    # END_YOUR_CODE

v1 = collections.defaultdict(float, {'a': 5, 'c' : 3})
scale = 2
v2 = collections.defaultdict(float, {'b': 2, 'a': 3})
result = incrementSparseVector(v1, 2, v2)
print 1, result


keys=set([v1.keys, v2.keys])

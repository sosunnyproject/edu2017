#coding=utf-8

def add_comma(val):
    result = []
    #if int % 1000 != 0, int is bigger than 1000. need comma
    while (val // 1000 != 0):
    # int % 1000 => string array (insert)
        #print(val)
        a = val
        b = val % 1000
        c = (a-b) // 1000
        #to prevent 0 to be deleted in printing b
        str_val = str(val)
        str_val_ls =[]
        for n in str_val[-3:]:
            str_val_ls.append(n)
        str_v = ''.join(str_val_ls)
        str_n = "," + str_v
        #update val (original - last 3 nums)
        val = c
        #print("str: ", str_n)
        result.insert(0,str_n)
    str_n = str(val)
    result.insert(0,str_n)
    final = ''.join(result)
    return final

def main():
    comma_added_1234 = add_comma(1234)
    comma_added_12345678 = add_comma(12345678)
    comma_added_12 = add_comma(12)
    comma_added_12045078 = add_comma(12045078)
    print(comma_added_1234)
    print(comma_added_12345678)
    print(comma_added_12)
    print(comma_added_12045078)
    # ‘1,234’
    # ‘12,345,678’
    # ‘12’

#run main function
#main()

if __name__=='__main__':
    main()



#------------------------------------------
#memo
# a = int
# b = int % 1000
# c = (int - int%1000) // 1000
# a = c
# str_n = "," + str(c)

#else str_n = str(c)
#result.insert(0, c)
#final = ''.join(result)
#coding=utf-8
def check_prime(num):
    #create an empty list to add all T/F checked values
    result = []
    # default = prime number
    value = 1

    #divide num by 2 ~ n-1
    for n in range(2,num):
       if (num % n == 0):
           # if modulo is 0, return 0, not a prime num
           value = 0
    # add a value 0 to result list
    result.append(value)
    if (0 in result):
        # if there's any number of 0 added into the list, it's not a prime number
        return False
    else:
        return True

def main():
    a = 13
    b = 15
    if check_prime(a):
        print(str(a) + " IS A PRIME NUMBER")
    else:
        print(str(a) + " IS NOT A PRIME NUMBER")
    if check_prime(b):
        print(str(b) + " IS A PRIME NUMBER")
    else:
        print(str(b) + " IS NOT A PRIME NUMBER")

#run main function
#main()

if __name__=='__main__':
    main()

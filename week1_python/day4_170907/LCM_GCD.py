#coding=utf-8
import random

#LCM 최소공배수 least common multiple
def LCM(num_list):
    mul = 1
    #deleting any repeated numbers
    ls = set(num_list)
    for n in ls:
        mul = mul * n
    return mul

#------------------------------------------
#GCD 최대공약수 greatest common divisor
def GCD(num_list):
    ls = sorted(num_list, reverse=True)
    big = max(ls)
    #finiding the divisors of the biggest num
    big_divs =[]
    for n in range(1,big):
        if(big % n == 0):
            big_divs.append(n)
    #biggest to smallest divisors
    big_divs = sorted(big_divs, reverse=True)

    #outer loop: big_divs numbers
    #inner loop: ls numbers
    #check if big_divs are still divisors of other numbers

    for gcd in big_divs:
        #print("divisor", n)
        bool = 0
        for ele in ls:
            #print("element", ele)
            if(ele % gcd == 0):
                bool += 1
            else:
                bool += 0
        #print("bool", bool, "\n")
        if(bool == len(ls)):
            return(gcd)
            break
#------------------------------------------
#main
def main():
    a=[]
    for i in range(10):
        a.append(random.randint(1,100)) # 1에서 100 중 정수 하나
    print("Randomly selected list is:", a)
    lcm_value=LCM(a)
    gcd_value=GCD(a)
    print("LCD:", lcm_value, "GCD:", gcd_value)
#------------------------------------------
#run main function
#main()

if __name__=='__main__':
    main()

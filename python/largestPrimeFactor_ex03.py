#largestPrimeFactor_ex03.py
#code 2.
#time :  0.47982215881347656
#find primefactor : 71, 839, 1471, 6857
#code1 execution time is good better than code2

import time

def IsPrimeFactor(number):
    div = 2

    if(number <= 2):
        return 2

    while(1):
        if(div == number):
            return number

        if(number % div == 0):
            return div

        div = div + 1


def findPrimeFactor(number,list):
    returnvalue = 0  # save PrimeFactor check function return value.
    primefactor = 1 # next primefactor.
    listItem = 0 # use for loop. save primefactorlist item value.
    measuretime = 0

    primefactorlist = [] # save primefactor to find prev loop

    if(number < 3):
        print("Please input other number. number 2 is prime factor")

    measuretime = time.time()

    while(1):
        primefactor = primefactor + 1

        if(primefactor >= number):
            break

        if (number == IsPrimeFactor(number)):
            list.append(number)
            break

        for listItem in primefactorlist:
            if (number % listItem == 0):
                number = number // listItem
                list.append(listItem)

        returnvalue = IsPrimeFactor(primefactor)

        if(returnvalue != primefactor) :
            continue
        else:
            primefactorlist.append(primefactor)

    print("time : ", time.time() - measuretime)

if __name__ == "__main__":
    primefactorlist = []
    number = 600851475143
    findPrimeFactor(number, primefactorlist)

    print(primefactorlist)


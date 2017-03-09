#ex05_SmallestMultiple.py
#time :  184.64769291877747
#value : 232792560
#this code is not good. execution time is very long...
#need to modify algorithm...

import time

def findSmallestMultiple():
    findSmallestNumber = 20
    IsPossiabledivide = 0
    measureTime = time.time()

    while(1):
        for number in range(2, 20):
            if (findSmallestNumber % number == 0):
                IsPossiabledivide = 1
            else:
                IsPossiabledivide = 0
                break

        if(IsPossiabledivide == 1):
            print("smallest Number is", findSmallestNumber)
            break
        else:
            findSmallestNumber += 1

    print("time : ", time.time() - measureTime)

if __name__ == "__main__":
    findSmallestMultiple()

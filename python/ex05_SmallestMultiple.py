#ex05_SmallestMultiple.py

def findSmallestMultiple():
    findSmallestNumber = 20
    IsPossiabledivide = 0

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
            print("searching...(number :", findSmallestNumber, ")")
            findSmallestNumber += 1

if __name__ == "__main__":
    findSmallestMultiple()

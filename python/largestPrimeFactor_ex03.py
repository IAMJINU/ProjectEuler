#largestPrimeFactor_ex03.py

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
    returnvalue = 0
    primefactor = 2

    if(number < 3):
        print("Please input other number. number 2 is prime factor")

    while(1):
        if(primefactor >= number):
            break

        returnvalue = IsPrimeFactor(primefactor)
        if(returnvalue != primefactor) :
            primefactor = primefactor + 1
            continue
        elif (number%primefactor == 0):
            number = number // primefactor
            list.append(primefactor)
            primefactor = 2

            if(number == IsPrimeFactor(number)):
                list.append(number)
                break

        primefactor = primefactor + 1



if __name__ == "__main__":
    primefactorlist = []
    number = 600851475143
    findPrimeFactor(number, primefactorlist)

    print(primefactorlist)

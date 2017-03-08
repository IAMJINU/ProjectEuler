#ex04_LargestPalindromeProduct.py
#time :  0.8152897357940674
#value : 906609(993 x 913)

import time

def findLargestPalindromeProduct():
    productNumber = 0 #save product result
    largestPalindromeProduct = 0 #save largest palindrome product
    findFirstNumber = 0
    findSecondNumber = 0
    returnValue = 0 #has value 1 that if product number is palindrome product
    measuretime = 0

    firstNumber = 999

    measuretime = time.time()

    #first loop
    while firstNumber >= 100:
        secondNumber = 999

        #second loop
        while secondNumber >= 100:
            productNumber = firstNumber * secondNumber
            convertIntToString = str(productNumber)
            lengthString = len(convertIntToString)

            #check if product number length is even
            if(lengthString%2 == 0) :
                IsPalindromeCnt = 0
                returnValue = 1

                #check if product number is palindrome number
                while(IsPalindromeCnt < (lengthString//2)):
                    if(convertIntToString[IsPalindromeCnt] != convertIntToString[lengthString - 1 - IsPalindromeCnt]):
                        returnValue = 0
                        break;

                    IsPalindromeCnt += 1

            if(returnValue != 0):
                returnValue = 0
                if (largestPalindromeProduct < productNumber):
                    largestPalindromeProduct = productNumber
                    findFirstNumber = firstNumber
                    findSecondNumber = secondNumber

            secondNumber -= 1

        firstNumber -= 1

    print(findFirstNumber, findSecondNumber)
    print(largestPalindromeProduct)

    print("time : ", time.time() - measuretime)

if __name__ == "__main__":
    findLargestPalindromeProduct()




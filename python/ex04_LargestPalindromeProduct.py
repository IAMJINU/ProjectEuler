#ex04_LargestPalindromeProduct.py

def findLargestPalindromeProduct():
    productNumber = 0
    largestPalindromeProduct = 0
    findFirstNumber = 0
    findSecondNumber = 0
    returnValue = 0

    firstNumber = 999

    while firstNumber >= 100:
        secondNumber = 999

        while secondNumber >= 100:
            productNumber = firstNumber * secondNumber
            convertIntToString = str(productNumber)
            lengthString = len(convertIntToString)

            if(lengthString%2 == 0) :
                IsPalindromeCnt = 0
                returnValue = 1

                while(IsPalindromeCnt < (lengthString//2)):
                    #print(convertIntToString[IsPalindromeCnt], convertIntToString[lengthString - 1 - IsPalindromeCnt])
                    if(convertIntToString[IsPalindromeCnt] != convertIntToString[lengthString - 1 - IsPalindromeCnt]):
                        returnValue = 0
                        break;

                    IsPalindromeCnt += 1

            if(returnValue != 0):
                returnValue = 0
                if (largestPalindromeProduct < productNumber):
                    print(largestPalindromeProduct, productNumber)
                    largestPalindromeProduct = productNumber
                    findFirstNumber = firstNumber
                    findSecondNumber = secondNumber
                #break;

            secondNumber -= 1

        firstNumber -= 1

    print("\n", findFirstNumber, findSecondNumber)
    print("\n", largestPalindromeProduct)

if __name__ == "__main__":
    findLargestPalindromeProduct()




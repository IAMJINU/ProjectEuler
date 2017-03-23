#ex06_SumSquareDifference.py
#total execution time :  0.0010006427764892578
#value : 25164150

import time

def computeSumOfSquare():
    sumOfSquare = 1

    for i in range(2, 101):
        sumOfSquare = sumOfSquare + (i * i)

    return sumOfSquare

def computeSquareOfSum():
    squareOfSum = 0

    for i in range(1, 51):
        squareOfSum = squareOfSum + 101

    squareOfSum = squareOfSum * squareOfSum

    return squareOfSum

if __name__ == "__main__":
    measureTimeToSumOfSquare = time.time()
    result_Func_SumOfSquare = computeSumOfSquare()
    print("function sumOfSquare execution time : ", time.time() - measureTimeToSumOfSquare)
    print("sum of square(from 1 to 100) : ",result_Func_SumOfSquare)

    measureTimeToSquareOfSum = time.time()
    result_Func_SquareOfSum = computeSquareOfSum()
    print("function squareOfSum execution time : ", time.time() - measureTimeToSquareOfSum)
    print("total execution time : ", time.time() - measureTimeToSumOfSquare)
    print("square of sum(from 1 to 100) : ", result_Func_SquareOfSum)

    print("differnece between each sum : ", result_Func_SquareOfSum - result_Func_SumOfSquare)

#evenFibonacci_ex02.py

def find_sumOfEvenFibonacci():
    sumOfEvenFibonacci = 2   #default set 2. because 2 is even
    finobacci_param_one = 1
    finobacci_param_two = 2
    finobacci_next_param = 0

    while (finobacci_next_param <= 4000000):
        finobacci_next_param = finobacci_param_one + finobacci_param_two

        if (finobacci_next_param % 2 == 0):
            sumOfEvenFibonacci = sumOfEvenFibonacci + finobacci_next_param

        finobacci_param_one = finobacci_param_two
        finobacci_param_two = finobacci_next_param

    print(sumOfEvenFibonacci)


if __name__ == "__main__":
    find_sumOfEvenFibonacci()


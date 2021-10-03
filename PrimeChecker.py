n = int(input("Check this number: "))


def prime_checker(number):
    for i in range(2, 10):
        if number > 1 and number % i == 0:
            return 'Not Prime'
        else:
            return 'Prime'


print(prime_checker(number=n))

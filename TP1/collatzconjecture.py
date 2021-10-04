def collatz_conjecture_values_generator(number):
    i=0
    if number == 1:
        yield number
        return

    while number != 1:
        number = collatz_conjecture_fun(number)
        yield number

def collatz_conjecture_values(number):
    """ The collatz conjecture assumes that for any number, the collatz number values will converge towards 1

    >>> collatz_conjecture_values(5)
    16
    8
    4
    2
    1
    """

    for i in collatz_conjecture_values_generator(number):
        print(i)

def collatz_conjecture_fun(number):
    if number%2==0:
        return number//2
    else:
        return 3*number+1

if __name__ == "__main__":
    collatz_conjecture_values(5)
    number = 6
    collatz_conjecture_values_generator = collatz_conjecture_values_generator(number)
    print()
    print(next(collatz_conjecture_values_generator))
    print(next(collatz_conjecture_values_generator))
    print(next(collatz_conjecture_values_generator))
    print(next(collatz_conjecture_values_generator))
    print(next(collatz_conjecture_values_generator))
    print(next(collatz_conjecture_values_generator))
    print(next(collatz_conjecture_values_generator))
    print(next(collatz_conjecture_values_generator))
    # Should raise a StopIteration error
    print(next(collatz_conjecture_values_generator))



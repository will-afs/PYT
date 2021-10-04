from chrono_context_manager import time_exc_measure

@time_exc_measure
def fizzbuzz(start, end):
    """ This function prints the numbers from start to end (excluded).
    But for multiples of 3, print 'Fizz'
    For multiples of 5, print 'Buzz'
    And for multiples of 3 and 5, print 'FizzBuzz'

    >>> fizzbuzz(10,16)
    10 : Buzz
    11
    12 : Fizz
    13
    14
    15 : FizzBuzz
    """
    for i in fizzbuzz_generator(start, end):
        print(i)

def fizzbuzz_generator(start, end):
    for i in range(start,end):
        string = str(i) + ' : '
        if i%3==0 and i%5==0:
            string += 'FizzBuzz'
        elif i%3==0:
            string += 'Fizz'
        elif i%5==0:
            string += 'Buzz'
        else:
            string = i
        yield string

if __name__ == "__main__":
    fizzbuzz(10,16)
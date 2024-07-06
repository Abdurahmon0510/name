class PrimeNumbersIterator:
    def __init__(self, stop):
        self.stop = stop
        self.start = 2

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            num = self.start
            self.start += 1
            if self.is_prime(num):
                return num

    def is_prime(self, num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

def prime_numbers_generator(stop):
    start = 2
    while True:
        if is_prime(start):
            yield start
        start += 1

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_prime_numbers(stop):
    iterator = PrimeNumbersIterator(stop)
    for _ in range(stop):
        print(next(iterator), end=" ")
    print("\n")

    generator = prime_numbers_generator(stop)
    for _ in range(stop):
        print(next(generator), end=" ")

stop = 10
print_prime_numbers(stop)

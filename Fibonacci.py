class Fibonacci:
    def __init__(self, limit=None):
        self.a, self.b = 0, 1
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit and self.count >= self.limit:
            raise StopIteration

        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1

        return result

fibonacci = Fibonacci(limit=7)

for num in fibonacci:
    print(num)

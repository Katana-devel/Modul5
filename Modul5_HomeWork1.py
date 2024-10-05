import collections

def caching_fibonacci():
    cache = collections.defaultdict()

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            result = cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = result
        return result
    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(15))

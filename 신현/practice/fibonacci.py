f = int(input())


def fibonacci(f):
    if (f <= 1):
        return f
    return fibonacci(f-1) + fibonacci(f-2)

print(fibonacci(f))
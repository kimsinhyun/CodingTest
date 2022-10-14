

def solution(n, k):
    import math
    answer = [i for i in range(1, n + 1)]
    stack = []
    k = k-1
    while answer:
        print(f"n={n} ; k={k}")
        a = k // math.factorial(n - 1)
        stack.append(answer[a])
        del answer[a]
        k = k % math.factorial(n - 1)
        n -= 1

    return stack
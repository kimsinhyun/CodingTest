def is_prime(n):
    if (n <= 1):
        return False
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            return False
    return True
    
def solution(numbers):
    from itertools import permutations
    numbers = [n for n in numbers]
    tp = []
    for i in range(1,len(numbers)+1):
        tp.extend(list(permutations(numbers,i)))
    print(tp)
    p = list(set([int("".join(n)) for n in tp]))
    answer = []
    for n in p:
        answer.append(is_prime(n))
    return sum(answer)

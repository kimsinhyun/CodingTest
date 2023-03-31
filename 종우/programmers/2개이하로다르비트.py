# 0215
# https://school.programmers.co.kr/learn/courses/30/lessons/77885

# !! should've found a pattern
# brute force 하지말고 패턴  찾아보기

# 내 풀이 (시간초과)
def solution(numbers):
    answer = []
    for number in numbers:
        cmp = number + 1
        while True:
            if diff(tobin(number), tobin(cmp)):
                answer.append(cmp)
                break
            cmp += 1
    return answer

def tobin(number):
    binary = ""
    while number>0:
        binary = str(number%2) + binary
        number = number // 2
    return binary

def diff(n1, n2):
    zeros = len(n2) - len(n1)
    n1 = "0"*zeros + n1
    bitdiff = 0
    for i in range(len(n2)):
        if n1[i] != n2[i]:
            bitdiff+=1
    if bitdiff <= 2:
        return True
    return False


# slightly better
def solution(numbers):
    answer = []
    for n in numbers:
        a = n + 1
        while True:
            if cmp(n, a):
                answer.append(a)
                break
            a += 1
    return answer

def cmp(n1, n2):
    if str(bin(n1^n2))[2:].count("1") <= 2:
        return True
    return False
    
# final
def solution(numbers):
    answer = []
    for number in numbers:
        binary = str(bin(number))[2:]
        if number%2 == 0:
            binary = binary[:-1] + "1"
        else:
            binary = "0" + binary
            zero = binary.rfind("0")
            binary = binary[:zero] + "10" + binary[zero+2:]
        answer.append(int(binary, 2))
    return answer
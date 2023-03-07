# 0307
# https://school.programmers.co.kr/learn/courses/30/lessons/42895


# 내풀이 틀림
def solution(N, number):
    if N == number:
        return 1
    # for every 5 there can be (plus, minus, multiply, divide, concat)
    # multiple of N
    # for every length try all combinations -> memo combination results
    calculation = 0
    length = 2
    results = {N:1}
    
    while number not in results:
        calculations = []
        for result in results:
            calculations.append(result + N)
            calculations.append(result - N)
            calculation.append(result * N)
            calculations.append(result / N)
            calculations.append(result*10 + N)
            
        for c in calculations:
            if c not in results:
                results[c] = length
        length += 1
            
    return results[number]

solution(5, 12)

# 정답
def solution(N, number):
    if N == number:
        return 1
    
    calculations = [set() for x in range(8)]
    
    for i, c in enumerate(calculations, start=1):
        c.add(int(str(N)*i))
        
    for i in range(1, 8):
        for j in range(i):
            for op1 in calculations[j]:
                for op2 in calculations[i-j-1]:
                    calculations[i].add(op1+op2)
                    calculations[i].add(op1-op2)
                    calculations[i].add(op1*op2)
                    if op2 != 0:
                        calculations[i].add(op1//op2)             
        if number in calculations[i]:
            return i+1
                    
    
    return -1
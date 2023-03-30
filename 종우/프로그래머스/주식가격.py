# 0128
# https://school.programmers.co.kr/learn/courses/30/lessons/42584

# 내 풀이 효율성 x
def solution(prices):
    answer = [0]*len(prices)#[6,5,1,3,1,0,0,0]
    dropped = [0] #[0,1,4,5]
    for i in range(1,len(prices)):
        for j in dropped:
            if prices[i] >= prices[j]:
                answer[j] += 1
            else:
                answer[j] += 1
                dropped.remove(j)
        dropped.append(i)
    return answer

# 다른 풀이
def solution(prices):
    length = len(prices)
    answer = [ i for i in range (length - 1, -1, -1)]
    
    stack = [0]
    for i in range (1, length, 1):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
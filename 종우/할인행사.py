# 0131_1
# https://school.programmers.co.kr/learn/courses/30/lessons/131127

# 내 풀이
def solution(want, number, discount):
    answer = 0
    idic = {}
    for i in range(len(want)):
        idic[want[i]] = i
    
    for i in range(len(discount)-9):
        tmp = [0]*len(want)
        d2 = discount[i:i+11]
        for item in d2:
            try:
                tmp[idic[item]] += 1
            except:
                break
            if tmp == number: answer +=1
            
    return answer


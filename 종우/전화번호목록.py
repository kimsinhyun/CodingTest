# 0105_3
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# 내 풀이
def solution(phone_book):
    answer = True
    x = sorted(phone_book, key=len)
    for j in range(len(x)) :
        for i in range(j+1, len(x)):
            if len(x[j]) < len(x[i]):
                if x[i][:len(x[j])] == x[j]:
                    return False
    return answer

# 다른 풀이
# 그냥 sort 하면 앞에서부터 같은 문자연 순서대로 정렬됨
# 어차피 하나만 찾으면 해결됨
def solution(p):
    p.sort()
    for i in range(len(p)-1): 
        if p[i] == (p[i+1])[:len(p[i])] : 
            return False

    return True
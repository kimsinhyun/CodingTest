# 0317
# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    scores = [0,0,0]
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    for i, a in enumerate(answers):
        if a == s1[i%len(s1)]:
            scores[0] += 1
        if a == s2[i%len(s2)]:
            scores[1] += 1
        if a == s3[i%len(s3)]:
            scores[2] += 1
    
    for i in range(3):
        if scores[i] == max(scores):
            answer.append(i+1)
    return answer
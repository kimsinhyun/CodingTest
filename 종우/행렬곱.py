# 0103_1
# https://school.programmers.co.kr/learn/courses/30/lessons/12949

# 내 풀이
def solution(arr1, arr2):
    r = len(arr1)
    c = len(arr2[0])
    x = len(arr1[0])
    answer = []
    
    for i in range(r):
        answer.append([0]*c)
    
    for i in range(r):
        for j in range(c):
            for k in range(x):
                answer[i][j] += arr1[i][k]*arr2[k][j]
                    
                
    return answer

# 다른 풀이
def productMatrix(X, Y):
    answer = [[sum(a*b for a, b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return answer
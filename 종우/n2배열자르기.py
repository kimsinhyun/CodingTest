# 1005_1
# n^2 배열 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/87390

# 내가 짠 코드
# 시간 초과
def solution(n, left, right):
    arr = [0]*(n*n)
    for i in range(n):
        for j in range(n):
            arr[i*n+j] = max(i+1,j+1)
    answer = arr[left:right+1]
    return answer

# 풀이
def solution(n, left, right):
    return [ max(divmod(i,n))+1 for i in range(left,right+1)]
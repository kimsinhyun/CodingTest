# 1128_2
# https://school.programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    ans = 0
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    if n == 1:
        return 1
    
    while n != 2:
        if n%2 == 0:
            n = n/2
        else:
            n=n-1
            ans +=1
    ans+=1
    return ans

# 이진법 솔류션
def solution(n):
    return bin(n).count('1')
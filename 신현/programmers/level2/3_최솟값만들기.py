def solution(A,B):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    A.sort()
    B.sort(reverse=True)
    print(A)
    print(B)
    print([a*b for a,b in zip(A,B)])
    return sum([a*b for a,b in zip(A,B)])
    
    # print(sum(A*B))
    # for i in range(len(A)):
    #     min_A = min(A)
    #     max_B = max(B)
    #     answer += min_A * max_B
    #     A.remove(min_A)
    #     B.remove(max_B)
    return answer
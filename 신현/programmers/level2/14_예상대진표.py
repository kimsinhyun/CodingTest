def solution(arr):
    from math import gcd
    answer = arr[0]
    for i in arr:
        answer =  (answer * i)//gcd(i,answer)
        # print(answer)
    return answer
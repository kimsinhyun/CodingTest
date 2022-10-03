def solution(s):
    answer = ''
    temp = s.split(" ")
    temp = [int(i) for i in temp]
    max_val = str(max(temp))
    min_val = str(min(temp))
    print(max_val, min_val)
    answer = min_val + " " + max_val
    return answer
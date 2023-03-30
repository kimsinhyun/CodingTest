# 0106_1
# https://school.programmers.co.kr/learn/courses/30/lessons/17677


# 내 풀이
def solution(str1, str2):
    sp1 = []
    sp2 = []
    
    for i in range(len(str1)-1):
        if (str1[i] + str1[i+1]).isalpha():
            sp1.append((str1[i] + str1[i+1]).lower())
    for i in range(len(str2)-1):
        if (str2[i] + str2[i+1]).isalpha():
            sp2.append((str2[i] + str2[i+1]).lower())
    
    if len(sp1) == 0 and len(sp2) ==0:
        return 65536
    
    same = 0
    for i in sp1:
        if i in sp2:
            sp2.remove(i)
            same+=1
    
    return int(65536*(same/(len(sp1)+len(sp2))))
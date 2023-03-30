# 0319
# https://school.programmers.co.kr/learn/courses/30/lessons/42860

# 내 풀이
def solution(name):
    answer = 0
    # check for A
    # attempt faster route around A
    # rest should be normal track
    # case when to take left path instead of irght
    
    # keys to match letter
    
            
    # keys to move between letters
    cur = 0
    lr = 0
    ll = 0
    length = len(name)
    checked = [0] * len(name)
    while 0 in checked:
        checked[cur] = 1
        mv = 0
        while True:
            mv += 1
            # move right
            if lr + 1 > length-1:
                lr = 0
            else:
                lr +=1
            # check right
            if name[lr] == 'A':
                checked[lr] = 1
            elif checked[lr] == 0:
                answer += mv
                mv = 0
                cur = lr
            # check left
            if ll - 1 < 0 :
                ll = length-1
            else:
                ll -= 1
            if name[ll] == 'A':
                checked[ll] = 1
            elif checked[ll] == 0:
                answer += mv
                mv = 0
                cur = ll
            print(checked)
    return answer

#JOAAANAERIAA
solution("JOAAANAERIAA")

# 풀이 정답

def solution(name):
    answer = 0
    # check for A
    # attempt faster route around A
    # rest should be normal track
    # case when to take left path instead of irght
    minm = len(name)-1
    for i, n in enumerate(name):
        # moves to get letter
        answer += min(ord(n)-ord('A'), ord('Z')-ord(n)+1)
        
        # moves to get to spot
        j = i+1
        while j<len(name) and name[j]=="A":
            j+=1
            
        minm = min(minm, i + len(name) - j + min(i, len(name)-j))
    
    return answer + minm
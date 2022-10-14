# 1009_1
# 영어 끝말잇기
# https://school.programmers.co.kr/learn/courses/30/lessons/12981

# 내 풀이
def solution(n, words):
    person =0
    rot = 0
    swords = set()
    elidx = 0
    b4 = ""
    found = False
    # find which is the first repeated or wrong letter
    for i, word in enumerate(words):
        if i == 0: 
            b4 = word[-1]
            swords.add(word)
            continue
        if (word in swords) or (word[0] != b4):
            elidx = i
            found = True
            break
        b4 = word[-1]
        swords.add(word)
        
    # find which person
    # find which rotation
    rot, person = divmod(elidx, n)
    if found:
        return [person+1, rot+1]
    else:
        return [0,0]

# 다른 사람 풀이
# 한줄로 모든 케이스 해결
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
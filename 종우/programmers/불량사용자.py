# 0501
# https://school.programmers.co.kr/learn/courses/30/lessons/64064

# my sol
import re

combs = set()

def dfs(potential, pouch, level):
    global answer
    
    if level == len(potential):
        combs.add("".join(list(pouch)))
        return
    
    for p in potential[level]:
        if p in pouch:
            pouch.remove(p)
            level += 1
            dfs(potential, pouch, level)
            pouch.add(p)
            level -=1

def solution(user_id, banned_id):    
    potential = [[] for _ in range(len(banned_id))]
    
    for i, bi in enumerate(banned_id):
        pattern = ""
        for c in bi:
            if c == "*":
                pattern += "[a-z0-9]{1,1}"
            else:
                pattern += c
        for ui in user_id:
            if re.fullmatch(pattern, ui) and len(ui):
                potential[i].append(ui)
    
    pouch = set(user_id)
    
    level = 0
    dfs(potential, pouch, level)
    
    
    return len(combs)
def solution(k, dungeons):
    from itertools import permutations
    permutation = list(permutations(dungeons))
    
    answer=[]
    for i in permutation:
        have = k
        can=0
        for j in i:
            need, cost = j
            if(need > have):
                can = False
                break
            else:
                have -= cost
                can+=1
            answer.append(can)
    answer = max(answer)
    return answer
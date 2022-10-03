def solution(clothes):
    item = dict()
    answer = 1
    for _,y in clothes:
        if y in item.keys():
            item[y] += 1
        else:
            item[y] = 1
    item = list(item.values())
    for i in item:
        answer *= i + 1
    return answer -1
        
def compute(left):
    temp = [val for idx, val in left.items()]
    return sum(temp)

def solution(want, number, discount):
    from collections import Counter
    answer = 0
    want_dict = dict()
    for x,y in zip(want, number):
        want_dict[x] = y
        
    answer = []
    for i in range(len(discount)-9):
        left = Counter(want_dict) - Counter(discount[i:i+10])
        total_left = compute(left)
        answer.append(total_left)
    temp = list(filter(lambda x: x==0, answer))
    return len(temp)
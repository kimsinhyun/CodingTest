def solution(str1, str2):
    # answer = 0
    import math
    set_1 = []
    set_2 = []
    for i in range(0,len(str1)-1):
        temp=str1.lower()[i:i+2]
        if(temp.isalpha()):
            set_1.append(temp)
    for i in range(0,len(str2)-1):
        temp=str2.lower()[i:i+2]
        if(temp.isalpha()):
            set_2.append(temp)
    # print(f"set_1={set_1}")
    # print(f"set_2={set_2}")
#     교집합
    intersect =[]
    intersect_1 = set_1.copy()
    intersect_2 = set_2.copy()
    for i in intersect_1:
        if i in intersect_2:
            intersect_2.remove(i)
            intersect.append(i)
    
    union_1_a = set_1.copy()
    union_1_b = set_1.copy()
    union_2 = set_2.copy()
    for i in union_2:
        if i not in union_1_a:
            union_1_b.append(i)
        else:
            union_1_a.remove(i)
            
    # print(f"intersect = {intersect}")
    # print(f"union = {union_1_b}")
    if(len(union_1_b) == 0):
        answer = 1 * 65536
    else:
        answer = math.floor(len(intersect)/len(union_1_b) * 65536)
        
    return answer
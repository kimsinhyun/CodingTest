def get_sum(arr2D):
    return sum([sum(a) for a in arr2D])

def get_square(arr):
    global sum0, sum1
    half = int(len(arr)/2)
    if (len(arr) < 2):
        if (get_sum(arr) == 3):
            sum1 += 3
        elif (get_sum(arr) == 0):
            sum0 += 3
        return
    t1, t2, t3, t4 = [], [], [], []
    for i in range(len(arr[:half])):
        test1 = [arr[:half][i][t] for t in range(int(len(arr[:half][i])/2))]
        test2 = [arr[:half][i][t] for t in range(int(len(arr[:half][i])/2), len(arr[:half][i]))]
        test3 = [arr[half:][i][t] for t in range(int(len(arr[:half][i])/2))]
        test4 = [arr[half:][i][t] for t in range(int(len(arr[:half][i])/2), len(arr[:half][i]))]
        t1.append(test1)
        t2.append(test2)
        t3.append(test3)
        t4.append(test4)
    tttt = []
    tttt.append(t1)
    tttt.append(t2)
    tttt.append(t3)
    tttt.append(t4)
    # for i in tttt:
    #     for j in i:
    #         print(j)
    #     print()
    cal = [True] * 4
    for i in range(len(tttt)):
        if get_sum(tttt[i]) == 0:
            sum0 += half**2-1
            cal[i]= False
        if get_sum(tttt[i]) == half**2:
            sum1 += half**2-1
            cal[i]= False
    # print(f"sum0={sum0} ; sum1={sum1} ; half={half}")
    for i in range(len(tttt)):
        if(cal[i]):
            get_square(tttt[i])
            
        
        
def solution(arr):
    answer = []
    global sum0, sum1
    sum1 = 0
    sum0 = 0

    half = int(len(arr)/2)
    if get_sum(arr) == 0:
        return [1,0]
    elif get_sum(arr) == len(arr)**2:
        return [0,1]
    else:
        get_square(arr)
    
    total_1=get_sum(arr)
    total_0=len(arr)**2 - total_1
    z1 = total_1-sum1
    z0 = total_0-sum0
    answer = [z0,z1]
    return answer

# temp = solution([[0,0],[0,0],[0,0],[0,0]])
# print(temp)

# temp = solution([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
# # temp = solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]])
# print(temp)
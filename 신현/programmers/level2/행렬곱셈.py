def solution(arr1, arr2):
    print(len(arr1))
    print(len(arr2[0]))
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    # print(answer)
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    print(answer)
        
    return answer
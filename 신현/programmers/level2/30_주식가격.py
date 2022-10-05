def solution(prices):
    answer = []
    for i in range(len(prices)):
        temp = 0
        for j in range(i+1, len(prices)):
            if prices[j] >= prices[i]:
                if(j>=len(prices)-1):
                    answer.append(temp+1)
                temp+=1
            else:
                answer.append(temp+1)
                break
    answer.append(0)
    return answer
def solution(scoville, K):
    import heapq
    answer = 0
    heapq.heapify(scoville)
    # print(scoville)
    
    while scoville[0] < K:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville)+(heapq.heappop(scoville)*2))
        except:
            return -1
        answer+=1
        # print(scoville)
    
    return answer

# 0322
# https://school.programmers.co.kr/learn/courses/30/lessons/43238

# my initial (timeout)
def solution(n, times):
    answer = 0
    vacant = [1] * len(times)
    tte = [i for i in times]
    
    for i in range(n):
        fastest = tte.index(min(tte))
        
        if vacant[fastest]:
            vacant[fastest] = 0
            tte[fastest] += times[fastest]
        else:
            toend = tte[fastest] - times[fastest]
            answer += toend
            for j in range(len(tte)):
                tte[j] -= toend
                if tte[j] <= times[j]:
                    vacant[j] = 1
            vacant[fastest] = 0
            tte[fastest] += times[fastest]
               
    rest = [tte[i]-times[i] if not v else 0 for i, v in enumerate(vacant)]
    answer += max(rest)
    return answer

# 풀이
def solution(n, times):
    times.sort()
    answer = 0
    left = times[0]
    right = n*times[-1]
    
    while(right>=left):
        mid = int((right+left)/2)
        total = 0
        for i in times:
            total += int(mid/i)
    
        if total >= n:
            answer = mid
            right = mid-1
            
        elif total < n:
            left = mid+1
    
    return answer
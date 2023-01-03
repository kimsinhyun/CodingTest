# 0103_3
# https://school.programmers.co.kr/learn/courses/30/lessons/64065#

# 내 풀이
# 12-294.63
def solution(s):
    answer = []
    s2 = s[2:-2]
    order = s2.split("},{")
    
    order.sort(key=len)
    
    for i in order:
        nos = i.split(",")
        for j in nos:
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer

# 다른 풀이
# 12-43.13
def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter
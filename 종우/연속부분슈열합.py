# 0122_2
# https://school.programmers.co.kr/learn/courses/30/lessons/131701

# 내 풀이 3955
def solution(elements):
    unique = set()
    print(sum(elements[0:2]))

    for ln in range(1, len(elements)+1):
        for idx in range(len(elements)):
            if idx + ln > len(elements):
                shift = (idx + ln) % len(elements)
                sm = sum(elements[idx:len(elements)]) + sum(elements[0:shift])
                unique.add(sm)
            else:
                sm = sum(elements[idx:idx+ln])
                unique.add(sm)
    return len(unique)

# 1008_4
# 카펫
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

# 내 풀이, 2차 방정식으로 품
def solution(brown, yellow):
    x = (4+brown+((4+brown)**2-16*(yellow+brown))**0.5)/4
    y = (4+brown-((4+brown)**2-16*(yellow+brown))**0.5)/4
    return [x,y]


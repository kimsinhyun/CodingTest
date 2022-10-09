# 1006_1
# 곱셈 (백준)
# https://www.acmicpc.net/problem/1629

base, power, divisor = map(int, input().split())

# 지수법칙: a^(n+m) = a^n * a^m
# modulo 성질: (a*b)%c = (a%c * b%c)%c
# 2^11%3 = (2^5%3*2^5*2%3)%3 = 2
# 지수를 나누려면 각각 모듈로 적용해야함

def DaC(Base,Power):
    if Power == 1:
        return Base % divisor

    # 2^5 = 2^2*2^2*2
    recur_exp = DaC(Base, Power//2)

    # so depending on power(even, odd)
    # if even: return recur_exp * recur_exp % C
    # elif odd: return recur_exp * recur_exp * base  % C
    # this recursively divides power into 2 and gets their modulo until power reaches 1
    # recur_exp의 power가 1일때 이미 %divisor 해서 반환돼서 마지막에 %divisor 한번만 하면됨
    if Power%2 == 0:
        return recur_exp* recur_exp % divisor
    else:
        return recur_exp * recur_exp * Base % divisor

    
print(DaC(base, power))
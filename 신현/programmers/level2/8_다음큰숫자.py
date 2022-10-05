def solution(n):
    answer = 0
    num_one = str(bin(n))[2:].count('1')
    while True:
        n += 1
        bin_n = str(bin(n))[2:]
        # print(bin_n)
        if str(bin(n))[2:].count('1') == num_one:
            return n
        
    return answer
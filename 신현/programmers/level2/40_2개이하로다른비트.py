def solution(numbers):
    bins = []
    for n in numbers:
        temp = bin(n).replace("0b","")
        temp = temp.rjust(len(temp)+2, "0")
        bins.append(list(temp))              

    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            bins[i][-1] = "1"
        else:
            tb = "".join(bins[i])
            idx = tb.rindex("0")
            bins[i][idx] = "1"
            bins[i][idx+1] = "0"
    # print(bins)
    answer = []
    for b in bins:
        temp = int("".join(b),2)
        answer.append(temp)
    return answer
            
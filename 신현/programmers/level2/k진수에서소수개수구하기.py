def is_prim(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i ==0:
            return False
    return True
def solution(n, k):
    import string
    tmp = string.digits + string.ascii_lowercase
    def convert(num, base):
        q,r = divmod(num,base)
        if(q == 0):
            return tmp[r]
        else:
            return convert(q,base) + tmp[r]
    answer = 0
    k_n = convert(n,k)

    btwn_z = k_n.split("0")
    for b in btwn_z:
        if b.isdigit():
            if(is_prim(int(b))):
                answer+=1
    
    
    return answer
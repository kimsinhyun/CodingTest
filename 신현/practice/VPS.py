import sys
input = sys.stdin.readline

N = int(input().strip())
for i in range(N):
    left_p = 0
    temp_flag = False
    p_list = input().strip()
    for j in p_list:
        if(j == "("):
            left_p += 1
        elif(j == ")"):
            left_p -= 1
        if(left_p < 0):
            print("NO")
            temp_flag =True
            break
    if(left_p == 0):
        print("YES")
    elif(temp_flag == False):
        print("NO")
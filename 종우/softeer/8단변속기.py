# 0512
# https://softeer.ai/practice/info.do?idx=1&eid=408

import sys
gears = input().split(' ')
answer = ''

if gears[0] == '1':
    answer = 'ascending'
elif gears[0] == '8':
    answer = 'descending'
else:
    answer = 'mixed'

tmp = gears[0]
if answer == 'ascending':
    for i in range(1, 8):
        if int(gears[i]) - int(tmp) != 1:
            answer = 'mixed'
            break
        tmp = gears[i]
elif answer == 'descending':
    for i in range(1, 8):
        if int(tmp) - int(gears[i]) != 1:
            answer = 'mixed'
            break
        tmp = gears[i]
    
print(answer)
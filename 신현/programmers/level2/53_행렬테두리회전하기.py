def rotateMatrix(matrix, querie):
    from collections import deque
    transmaps = deque([])
    top = matrix[querie[0]-1][querie[1]-1:querie[3]]
    right = column(matrix[querie[0]:querie[2]-1], querie[3]-1)
    bottom = matrix[querie[2]-1][querie[1]-1:querie[3]]
    left = column(matrix[querie[0]:querie[2]-1], querie[1]-1)
    bottom.reverse()
    left.reverse()
    
    transmaps.extend(top)
    transmaps.extend(right)    
    transmaps.extend(bottom)    
    transmaps.extend(left)    
    transmaps.rotate(1)
    min_val = min(transmaps)
    idxs = []
    topidx = [[querie[0]-1, i] for i in range(querie[1]-1,querie[3])]
    rightidx = [[i, querie[3]-1] for i in range(querie[0],querie[2]-1)]
    bottomidx = [[querie[2]-1, i] for i in range(querie[1]-1,querie[3])]
    leftidx = [[i, querie[1]-1] for i in range(querie[0],querie[2]-1)]
    bottomidx.reverse()
    leftidx.reverse()
    idxs.extend(topidx)
    idxs.extend(rightidx)    
    idxs.extend(bottomidx)    
    idxs.extend(leftidx)    
    
    for x,y in idxs:
        matrix[x][y] = transmaps.popleft()
    # print()
    # for i in matrix:
    #     print(i)
    return matrix, min_val

def column(matrix, i):
    return [row[i] for row in matrix]

def solution(rows, columns, queries):
    matrix = [[j for j in range(i*columns+1, (i+1)*columns+1)] for i in range(0,rows)]
    
    min_vals = []
    for q in queries:
        matrix,min_val = rotateMatrix(matrix,q)
        min_vals.append(min_val)
    return min_vals
        
# def duplicate(arr):
#     dups = {}
#     answer = []

#     for a in arr:
#         if a not in dups:
#             dups[a] = 0
#         dups[a] += 1

#     for k in dups.keys():
#         if dups[k] > 1:
#             answer.append(dups[k])
    
#     if answer:
#         return answer
#     return [-1]

# print(duplicate([1,2,3,3,3,3,4,4]))
# print(duplicate([3,2,4,4,2,5,2,5,5]))
# print(duplicate([3,5,7,9,1]))

def assign(arr):
    # Assign Memory
    # read type and memery
    # depends on current type, 
    # previous assigned index,
    # if remaining 8 byte space is enough

    types = {"BOOL": ["#", 1], "SHORT" : ["##", 2], "FLOAT" : ["####", 4], "INT":["########", 8], "LONG":["########,########", 16]}
    memory = ""
    tmpUnit = ""
    
    for a in arr:
        length = len(tmpUnit)
        if a == "SHORT":
            if length%2 != 0:
                tmpUnit += "."
        elif a == "FLOAT":
            if length%4 != 0:
                tmpUnit += "."*(4-length%4)
        elif a == "INT" or a == "LONG":
            if length != 0:
                tmpUnit += "."*(8-length)
        if len(tmpUnit) == 8:
            memory += "," + tmpUnit
            tmpUnit = ""
        
        if a == "LONG" or a == "INT":
            memory += "," + types[a][0]
        else:
            tmpUnit += types[a][0]

        if len(memory) > 128:
            return "HALT"



    if len(tmpUnit) % 8 != 0:
            tmpUnit += "."*(8-length)
            memory += "," + tmpUnit
    return memory[1:]

print(assign(["INT", "INT", "BOOL", "SHORT", "LONG"]))
print(assign(["INT", "SHORT", "FLOAT", "INT","BOOL"]))
print(assign(["FLOAT", "SHORT", "BOOL", "BOOL", "BOOL", "INT"]))
print(assign(["BOOL", "LONG", "SHORT", "LONG", "BOOL", "LONG", "BOOL", "LONG", "SHORT", "LONG", "LONG"]))

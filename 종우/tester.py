def gra2coms(graph:dict[int,set[int]]) -> list[list[int]]:
    return [[int(k in j) for k in graph.keys()] for i, j in graph.items()]

print(gra2coms({i:{i, i - 5, i + 5} for i in range(10)}))
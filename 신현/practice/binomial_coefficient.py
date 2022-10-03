from codecs import BOM
from itertools import combinations

N, K = map(int,input().split(" "))
combs = list(combinations(range(N), K))
print(len(combs))
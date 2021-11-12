from itertools import combinations

N, M = map(int, input().split())
arr = [str(i+1) for i in range(N)]

for k in list(combinations(arr, M)):
    print(" ".join(k))

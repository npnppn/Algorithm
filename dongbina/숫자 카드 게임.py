#각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수 찾는게 핵심!

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data) #현재 줄에서 가장 작은 수 찾기
    result = max(result, min_value) # 작은 수 중에서 가장 큰거 찾기

print(result)

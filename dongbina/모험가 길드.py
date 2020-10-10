#현재 그룹에 포함된 모험가의 수가 현재 확인하고 있는 공포도보다 크거나 같으면, 그룹 결성

n = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = 0 #총 그룹 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data:
    count += 1
    print(count)
    if count >=i :
        result += 1
        count = 0

print(result)


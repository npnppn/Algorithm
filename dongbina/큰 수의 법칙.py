n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1] #가장 큰 수
second = data[n-2] #두번째 큰 수

#가장 큰 수가 더해지는 횟수 계산
count = int(m/ (k+1)) * k
count += m % (k+1)


result = 0
result += count * first
result += (m-count) * second
print(result)

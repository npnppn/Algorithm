#반복되는 수열에 대해서 파악하는것이 핵심!
#가장 큰 수와 두번째 큰 수만 저장하면 구현가능한 형태.

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

#최대한 많이 나누기

n, k = map(int, input().split())
result = 0

#n이 k이상이면 계속 나누기
while n >= k:
    while n % k != 0: #안나눠 떨어지면 n에서 1씩 빼기
        n -= 1
        result += 1

    n //= k
    result += 1

while n > 1: #마지막 남은 수 계산
    n -= 1
    result += 1

print(result)

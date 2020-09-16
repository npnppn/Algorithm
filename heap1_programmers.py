import heapq

def mix(first,second):
    return first+ second*2

def bfs(scoville,K):
    successFlag = False
    count = 0

    while len(scoville)>=1:
        first = heapq.heappop(scoville)
        if first > K:
            successFlag = True
            break
        if len(scoville)>=1:
            second = heapq.heappop(scoville)
            mixResult = mix(first,second)
            heapq.heappush(scoville, mixResult)
            count+=1

    if successFlag:
        return count
    else:
        return -1

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    answer = bfs(scoville,K)
    return answer
    
    """접근법
    1. 가장 작은 수가 K보다 작으면 계속 반복해주면 된다.

    2. 가장 작은 수를 바로 뽑을 수 있는 방법은 우선순위 큐를 사용해주었다. 우선순위 큐의 top()은 해당 큐에 있는 값 중에 가장 큰 수를 return 시켜준다.

    3. 우리는 가장 작은 값을 return 받고 싶기 때문에 원래 scoville값에 음수를 붙혀서 넣어준다. 왜냐하면

   [3,2,1]에서 우린 1을 뽑고 싶지만 우선순위 큐에서 top()의 return 값은 3이 나올 것이다.
   다만 음수를 곱하여 넣어준다면 [-3,-2,-1]의 형태로 들어갈 것이고 top()의 return값은 -1일 것이고 그것을 다시 음수를 곱해주면 최소값을 얻을 수 있다.
   
   """

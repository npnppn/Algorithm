import heapq

def solution(jobs):
    answer = 0
    jobs.sort()
    start = jobs[0][0]
    jobHeapq = []
    check = [False for i in range(len(jobs))]

    # 0초 기준으로 맞춤
    for i,value in enumerate(jobs):
        jobs[i][0] -= start


    answer += jobs[0][1]
    end = jobs[0][1]
    check[0] = True
    cnt = 1
    lastIndex = 0

    while cnt < len(jobs):
        for i,value in enumerate(jobs):
            #작업 중일때 요청들어온 디스크 작업 
            if value[0] <= end and check[i] == False:
                heapq.heappush(jobHeapq,[value[1],i])
                check[i] = True
            elif value[0] > end: 
                lastIndex = i 
                break

        if len(jobHeapq)==0: #디스크에 작업이 없을 경우
                answer += (jobs[lastIndex][1])
                end = jobs[lastIndex][1] +jobs[lastIndex][0]
                check[lastIndex]= True
                lastIndex+=1
                cnt+=1
        else:
            #minheaq[0] = 소요시간 , minheaq[1] = 디스크 인덱스
            minheaq = heapq.heappop(jobHeapq) 
            answer += (minheaq[0]+end-jobs[minheaq[1]][0])
            end += minheaq[0]
            cnt+=1

    answer = int(answer/len(jobs))
    return answer
    
"""접근법
<변수 및 기본 설명>

1. jobs를 오름차순으로 바꿔서 가장 일찍들어오는거 순으로 정렬은 시킨다.

2. 계산의 편의를 위해 시작디스크 작업을 0초로 맞춰춘다. -> jobs순회하며 jobs[0][0]을 빼준다.

3. end는 작업이 끝나는 시간이고, check는 해당 작업을 처리했는지 확인하는 리스트이다. cnt는 처리한 작업의 수이며, lastInde는 작업목록에 작업이 없고 아직 처리해야할 작업이 남았을 때, 다음 작업으로 가기위한 변수이다.

 

<핵심 풀이 부분>

4. 작업을 하는 중에 들어온 작업 목록에 대해서 다음 작업으로 어떤것을 선택해야지 걸리는 소요시간이 가장 작을지에 대해 생각을 해봐야한다.

-> 이미 제 시간에 시작을 못한 작업들은 빨리 들어온거나 늦게들어온거나 결국 대기되는 시간은 동일하다.

  그러므로 다음것을 선택할 때 고려해야할 것은 누가 먼저 들어왔냐, 누가 먼저 끝나냐가 아닌 그냥 순수한 작업 소요시간만 고려하면된다.  따라서 작업 소요시간을 c++에선 우선순위 큐, 파이썬에선 heap에 삽입하여 최소 소요시간이 걸리는 작업을 먼저 처리한다.

-> 이 경우 소요시간은 answer +=  (소요시간+ (end - 해당디스크의시작시간)) 으로 계산하면된다.
"""

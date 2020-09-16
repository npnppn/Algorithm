import heapq

def solution(operations):
    answer = []
    hq = []
    for command in operations:
        if command[0] == 'I': #삽입
            num = int(command[2:len(command)])
            heapq.heappush(hq,num)
        elif command[2] == '1': #최대값 삭제
            if len(hq)>0:
                hq.pop(hq.index(max(hq)))
        else: #최소값 삭제
            if len(hq)>0: 
                heapq.heappop(hq)
    if len(hq) >= 1:
        answer.append(max(hq))
        answer.append(heapq.heappop(hq))
    else:
        answer = [0,0]
    
    return answer
    
"""접근법
    
1. 최소값을 찾을 땐 파이썬의 heap를 사용하였으며, 최대값을 찾을 때는 리스트의 max와 index를 사용했다.

2. max(hq)는 hq 리스트 중에 최대값을 리턴해주고 hq.index(max(hq))는 hq리스트에서 max(hq)값의 위치를 반환해준다.

hq.pop(인덱스번호) 해당 인덱스를 pop시킨다.
"""

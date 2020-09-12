#프로그래머스 스택큐 4번문제

def solution(priorities, location):
    answer = 0

    sample = [0] * len(priorities)
    sample[location] = 1

    while max(sample) == 1:
        if priorities[0] == max(priorities):
            priorities.pop(0)
            sample.pop(0)
            answer += 1

        else:
            priorities.append(priorities.pop(0))
            sample.append(sample.pop(0))

    return answer

#우선순위 큐? 내용 완벽하게 이해 x

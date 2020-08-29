def solution(participant, completion):
    answer=''
    count_dictionary = {}

    # 우선 participant에서 동명이인 카운트
    for i in participant:
        if i in count_dictionary:
            count_dictionary[i]=count_dictionary[i]+1
        else: #기존에 존재하지않으면 key:value 쌍을 추가한다
            count_dictionary[i]=1
            
    for i in completion:
        if i in count_dictionary:
            count_dictionary[i]=count_dictionary[i]-1
        else: 
            print("완주하지 못한 사람이 있네요")

    for name, count in count_dictionary.items():
        if count==1:
            #print (name)
            answer=name

    return answer
    
    -----------------------
    
""" 더 간단한 풀이도 있음
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
"""

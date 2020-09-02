# 전화번호 목록 문제

def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(0,len(phone_book)) :
        for j in range(i+1,len(phone_book)) :
            if phone_book[i] in phone_book[j] :
                return False
            
    return answer
    
    
    
    ------------
    
"""밑에 방법이 해쉬 알고리즘 이용하여 제대로 푼 방법

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
"""

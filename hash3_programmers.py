#위장 문제

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
    
# reduce 함수? 흠.. 람다식도 한번 더 공부해보기
# 이건 수학문제... 휴우..
# counter 객체 다시한번 

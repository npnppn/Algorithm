def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    #x는 list(d.keys())의 원소를 의미
    #map 함수 안에 있는 lambda의 y는 d[x]의 원소를 의미
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer
    #따라서 x(genre)를 받아서 d[x] (dictionary d의 해당 장르에 속한 음악 고유번호와 play된 수 list)에서 play된 수만 추출
    #그 값들을 모두 합한 값을 key로 sorted를 하게 되는 것
    
    #lamda식 안에 lamda를 집어넣을수도 있구나!
    #lamda가 dictionary 방법보다 어렵게 느껴짐.. 람다식 좀더 공부해야봐야할듯!
    #해쉬 알고리즘 문제들 풀면서 느낀점 : 파이썬이 딕셔너리 덕분에 확실히 편한느낌.

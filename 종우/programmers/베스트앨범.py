# 0220
# https://school.programmers.co.kr/learn/courses/30/lessons/42579
# 해쉬

def solution(genres, plays):
    answer = []
    playno = {}
    gp = list(zip(genres, plays, (i for i in range(len(genres)))))
    for i, j, x in gp:
        if i not in playno:
            playno[i] = j
        else:
            playno[i] += j
            
    gp.sort(key=lambda x: x[1], reverse=True)
    gp.sort(key=lambda x: x[0], reverse=True)
    
    tmp = ''
    skip = False
    for k in gp:
        if not skip and tmp != k[0]:
            answer.append(k[2])
            tmp = k[0]
        elif not skip and tmp == k[0]:
            answer.append(k[2])
            skip = True
        elif tmp==k[0] and skip:
            continue
        elif tmp!=k[0] and skip:
            answer.append(k[2])
            skip = False
            tmp = k[0]
    
    return answer

# 풀이

def solution(genres, plays):
    answer = []
    #dic 딕셔너리에 입력 저장- { 장르1: [[노래1 재생 횟수 :노래1 고유 번호],[노래2 재생 횟수: 노래2 고유번호]...]} 형식으로
    dic={}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]].append([plays[i],i])
        else : 
            dic[genres[i]] = [[plays[i],i]]

    #genre_rank 딕셔너리에 각 장르의 모든 곡의 총 재생 횟수 저장- {장르 1 : 모든 장르 1곡의 총 재생 횟수 ,장르 2 : 모든 장르 2곡의 총 재생 횟수...}
    genre_rank ={}
    for genre in dic.keys():
        songs = dic[genre]
        plays_sum = 0
        for song in songs:
            plays_sum+=song[0]
        genre_rank[genre] = plays_sum
    #genre_rank를 재생 횟수가 큰 순으로 정렬 
    genre_rank = sorted(genre_rank.items(), key=lambda x: x[1],reverse=True)
    
    # genre_rank에 저장되어 있는 장르 순으로 dic에서 해당 장르를 key로 가진 value를 확인
    for genre in genre_rank:
        #2차원 배열인 value를 다중 조건으로 정렬 (첫번째 인자인 곡 재생 수를 기준으로 내림차순 정렬 후,
        #                                     두번째 인자인 곡 고유 번호를 기준으로 오름차순 정렬)
        song_rank=sorted(dic[genre[0]], key=lambda x:(-x[0],x[1]))
        best_two = 0
        # 정렬된 배열을 하니씩 확인하면서 answer에 고유 번호를 순서대로 저장 , 만약 한 장르의 곡이 두 곡 저장되면 해당 장르에서 반복 중지
        for song in song_rank:
            answer.append(song[1])
            best_two +=1
            if best_two == 2:
                break

    return answer
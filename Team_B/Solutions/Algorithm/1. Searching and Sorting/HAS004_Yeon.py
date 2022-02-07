# Draft 1
def gridlandMetro(n, m, k, track):
    # Write your code here
    total_track = 0
    tracks = {}
    for i in range(k):
        r = track[i][0]
        c1 = track[i][1]
        c2 = track[i][2]
        # 아래 조건문을 사용하면 같은 줄에 트랙이 띄엄띄엄 있을때 문제가 발생함
        if r in tracks:
            c1 = min(c1, tracks[r][0])
            c2 = max(c2, tracks[r][1])
        tracks[r] = [c1,c2]
        print(tracks)
    for j in tracks:
        a1 = tracks[j][0]
        a2 = tracks[j][1]   
        total_track += a2-a1+1
    zeros = n*m - total_track
    return zeros

# Draft 2 - 아래 로직으로 Hackerrank Testcase#5은 통과할수 있지만 만약 이미 같은줄에 두개의 별도의 트랙이 존재한다면 아래 코드는 에러가 발생함
def gridlandMetro(n, m, k, track):
    # Write your code here
    total_track = 0
    tracks ={}
    for i in range(k):
        r = track[i][0]
        c1 = track[i][1]
        c2 = track[i][2]
                   
        if r in tracks:
            # 해당 부분에서도 각 트랙마다 for loop을 돌려야하고 그 전 혹은 다음 트랙과 안겹치는지도 확인해야해서 우선 작성을 멈춤 
            if  c2 < tracks[r][0] or c1 > tracks[r][1]:
                tracks[r].append(c1)
                tracks[r].append(c2)
            else:
                c1 = min(c1, tracks[r][0])
                c2 = max(c2, tracks[r][1])
                tracks[r] = [c1,c2]
        else:
            tracks[r] = [c1,c2]
    print(tracks)
    
    #출력코드도 번거로워짐, 로직 자체는 어렵지 않으나 비효율적인 느낌인듯
    for j in tracks:
     
        if len(tracks[j]) > 2:
            
            a1, a2, start, end, small_sum= 0,0,0,1,0
            for q in range((len(tracks[j])//2)):
                #print(tracks[j][1])
                a1 = tracks[j][start]
                a2 = tracks[j][end]
                small_sum += a2-a1 +1
                start += 2
                end += 2

        else:
            small_sum = 0
            a1 = tracks[j][0]
            a2 = tracks[j][1]
            small_sum = a2-a1+1 
        total_track += small_sum
    zeros = n * m - total_track
    
    return zeros

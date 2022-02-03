import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        #만약에 width가 같으면 height를 역순으로 정렬
        envelopes = sorted(envelopes, key = lambda x: [x[0], -x[1]])
        
        max = []

        for dim in envelopes :
            h = dim[1]
            pos = bisect.bisect_left(max,h)
            if pos == len(max) :
                max.append(h)
            else :
                #현재 height가 이전 height보다 작거나 같은 경우 max의 length에는 변화가 없음
                max[pos] = h
        
        return len(max)
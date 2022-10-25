
import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while len(scoville) > 1:
        l1 = heapq.heappop(scoville)
        l2 = heapq.heappop(scoville)
        mixed = l1 + l2 * 2
        heapq.heappush(scoville, mixed)
        answer+=1

        if scoville[0] > K:
            return answer

    return -1

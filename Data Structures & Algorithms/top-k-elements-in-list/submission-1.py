from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = defaultdict(int)
        for num in nums:
            my_map[num] += 1
        
        heap = []

        for key,value in my_map.items():
            heapq.heappush(heap,(value,key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        for i in range(k):
            ans.append(heap[i][1])
        
        
        
        return ans
        
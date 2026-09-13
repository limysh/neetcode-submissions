from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = defaultdict(int)
        for num in nums:
            my_map[num] += 1
        
        top_k = sorted(my_map, key = lambda key: my_map[key], reverse = True)[:k]
        
        
        
        return top_k
        
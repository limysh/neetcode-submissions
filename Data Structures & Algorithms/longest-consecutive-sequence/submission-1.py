from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        my_set = set(nums)
        streak = 1
        for num in my_set:
            if (num-1) not in my_set:
                length = 1
                while (num + length ) in my_set:
                    length += 1
                    streak = max(length, streak)
        return streak




        
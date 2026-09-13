class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sorted_set = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and sorted_set[i] == sorted_set[i-1]:
                continue
            target = -(sorted_set[i])
            j = i + 1
            k = len(sorted_set) - 1
            while j < k:
                if j == i:
                    j += 1
                    continue
                if k == i:
                    k -= 1
                    continue
                if sorted_set[j] + sorted_set[k] < target:
                    j += 1
                    continue
                if sorted_set[j] + sorted_set[k] > target:
                    k -= 1
                    continue
                if sorted_set[j] + sorted_set[k] == target:
                    ans.append([sorted_set[i], sorted_set[j], sorted_set[k]])
                    j += 1
                    k -= 1
                    while j < k and sorted_set[j] == sorted_set[j - 1]:
                        j += 1

                    while j < k and sorted_set[k] == sorted_set[k + 1]:
                        k -= 1
        return ans

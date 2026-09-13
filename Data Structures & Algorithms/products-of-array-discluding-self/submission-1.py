class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0]* n
        suff = [0]* n

        pref[0] = 1
        suff[n-1] = 1

        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i-1]
        for i in range (n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]

        
        ans = []
        for i in range(len(nums)):
            ans_val = pref[i] * suff[i]
            ans.append(ans_val)
        





        return ans

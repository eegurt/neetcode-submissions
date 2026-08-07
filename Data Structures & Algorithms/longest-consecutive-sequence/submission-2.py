class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        res = 0

        for n in nums:
            if n-1 not in nset:
                streak = 1
                while n + streak in nset:
                    streak+=1
                res = max(res, streak)
        
        return res
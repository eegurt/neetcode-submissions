class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_ = set()
        for n in nums:
            if n not in set_:
                set_.add(n)
            else:
                return True
        return False
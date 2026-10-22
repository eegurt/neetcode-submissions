class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnums = []
        for ch in s:
            if ch.isalnum():
                alnums.append(ch)
        
        alnums = ''.join(alnums).lower()

        halflen = int(len(alnums) / 2)
        for i in range(halflen):
            if alnums[i] != alnums[len(alnums)-i-1]:
                return False
        return True
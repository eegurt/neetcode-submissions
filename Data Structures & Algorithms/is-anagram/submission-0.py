class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = dict.fromkeys(s,0)
        for ch in s:
            dic[ch] += 1
        
        for ch in t:
            if ch not in dic:
                return False
            
            dic[ch] -= 1
            if dic[ch] < 0:
                return False
        
        return sum(dic.values()) == 0

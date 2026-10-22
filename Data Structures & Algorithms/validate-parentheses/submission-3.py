class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')':'(',
            '}':'{',
            ']':'[',
        }
        stack = []

        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            else:
                if len(stack) >= 1:
                    if stack[len(stack)-1] == pairs[ch]:
                        stack.pop()
                    else:
                        return False
                elif len(stack) == 0 and ch in pairs.keys():
                    return False
        return len(stack) == 0

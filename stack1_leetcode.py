#20번 #valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')':'(',
            '}':'{',
            ']':'[',
        }
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0
        
  # 스택 가장 기본적인 문제.
  # 스택큐는 꼭 알아두자 

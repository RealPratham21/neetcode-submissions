class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ['(', '[', '{']
        closes = [')', ']', '}']

        for i in s:
            if i in opens:
                stack.append(i)
            
            else:
                if i == ')':
                    if stack and stack.pop() != '(':
                        return False
                
                elif i == '}':
                    if stack and stack.pop() != '{':
                        return False
                
                elif i == ']':
                    if stack and stack.pop() != '[':
                        return False
        
        return len(stack) == 0
class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for char in s:
            if char == ')':
                # Extract and reverse characters inside the innermost parentheses
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()  # Remove matching '('
                
                # Append reversed characters back to stack
                stack.extend(temp)
            else:
                stack.append(char)
                
        return "".join(stack)
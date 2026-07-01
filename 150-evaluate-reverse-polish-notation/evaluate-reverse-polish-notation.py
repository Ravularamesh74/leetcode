class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
      
        stack = []
        
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                # The first popped is the right operand, second is the left operand
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # int() division in Python 3 handles truncation towards zero automatically
                    stack.append(int(float(a) / b))
            else:
                stack.append(int(token))
                
        return stack[0]
class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        stack = []
        res = set()
        cur_set = {""}  # Current combined product group

        for char in expression:
            if char.isalpha():
                # Concatenate current letter with all elements in cur_set
                cur_set = {s + char for s in cur_set}

            elif char == '{':
                # Save previous evaluation state before entering sub-expression
                stack.append(res)
                stack.append(cur_set)
                res = set()
                cur_set = {""}

            elif char == ',':
                # End of current union branch within braces or expression
                res.update(cur_set)
                cur_set = {""}

            elif char == '}':
                # Complete the current inner union set
                res.update(cur_set)
                
                # Pop state prior to opening brace '{'
                prev_cur = stack.pop()
                prev_res = stack.pop()

                # Multiply popped product state with result of braced expression
                cur_set = {p + r for p in prev_cur for r in res}
                res = prev_res

        res.update(cur_set)
        return sorted(list(res))
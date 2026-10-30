class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        max_area = 0
        # Append a 0 at the end to flush out any remaining elements in the stack
        heights_extended = heights + [0]
        
        for i, h in enumerate(heights_extended):
            while stack and heights_extended[stack[-1]] > h:
                height = heights_extended[stack.pop()]
                # If stack is empty, width is i; otherwise, width is i - stack[-1] - 1
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
            
        return max_area
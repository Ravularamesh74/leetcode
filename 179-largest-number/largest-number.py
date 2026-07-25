from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Convert integers to strings
        nums = [str(x) for x in nums]
        
        # Custom comparator: returns negative if a+b > b+a (a comes before b)
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        
        # Sort using custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Join numbers into a single string
        res = "".join(nums)
        
        # Handle edge case with leading zeros (e.g., [0, 0] -> "0")
        return "0" if res[0] == "0" else res
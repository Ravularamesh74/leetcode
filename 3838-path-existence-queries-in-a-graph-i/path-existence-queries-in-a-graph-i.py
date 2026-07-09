class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # comp[i] will store the component ID for node i
        comp = [0] * n
        curr_id = 0
        
        # Determine the connected components in O(n)
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                curr_id += 1
            comp[i] = curr_id
            
        # Answer each query in O(1)
        ans = []
        for u, v in queries:
            ans.append(comp[u] == comp[v])
            
        return ans
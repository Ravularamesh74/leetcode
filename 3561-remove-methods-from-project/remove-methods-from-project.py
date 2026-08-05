from collections import defaultdict, deque

class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        # Build adjacency list
        adj = defaultdict(list)
        for u, v in invocations:
            adj[u].append(v)
            
        # 1. Traverse from k using BFS to find all suspicious methods
        suspicious = set([k])
        queue = deque([k])
        
        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        # 2. Check if any non-suspicious method calls a suspicious method
        for u, v in invocations:
            if v in suspicious and u not in suspicious:
                # Removal is blocked; return all nodes
                return list(range(n))
                
        # 3. Return remaining nodes
        return [i for i in range(n) if i not in suspicious]
from collections import defaultdict

class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list and track degrees
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        complete_components_count = 0
        
        # Step 2: Traverse all nodes to find components
        for i in range(n):
            if not visited[i]:
                # Start a BFS/DFS to explore the current component
                component_nodes = []
                queue = [i]
                visited[i] = True
                
                while queue:
                    curr = queue.pop(0)
                    component_nodes.append(curr)
                    
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                # Step 3: Verify if the component is complete
                # Each node in a complete component must have a degree equal to (total_nodes - 1)
                num_nodes = len(component_nodes)
                is_complete = True
                
                for node in component_nodes:
                    if len(adj[node]) != num_nodes - 1:
                        is_complete = False
                        break
                        
                if is_complete:
                    complete_components_count += 1
                    
        return complete_components_count
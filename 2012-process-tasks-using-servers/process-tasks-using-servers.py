import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        # Min-heap for available servers, stored as (weight, index)
        free_servers = []
        for i, weight in enumerate(servers):
            heapq.heappush(free_servers, (weight, i))
            
        # Min-heap for busy servers, stored as (free_time, weight, index)
        busy_servers = []
        
        ans = []
        current_time = 0
        
        for j, task_time in enumerate(tasks):
            # Time cannot be earlier than the task's arrival time `j`
            current_time = max(current_time, j)
            
            # If no servers are free, fast-forward time to when the earliest busy server becomes free
            if not free_servers:
                current_time = max(current_time, busy_servers[0][0])
                
            # Release all servers that finish their tasks by `current_time`
            while busy_servers and busy_servers[0][0] <= current_time:
                free_time, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, index))
                
            # Assign the current task to the optimal free server
            weight, index = heapq.heappop(free_servers)
            ans.append(index)
            
            # Push the server into the busy heap with its new release time
            heapq.heappush(busy_servers, (current_time + task_time, weight, index))
            
        return ans
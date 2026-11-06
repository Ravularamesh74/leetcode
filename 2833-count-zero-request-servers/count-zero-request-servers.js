/**
 * @param {number} n
 * @param {number[][]} logs
 * @param {number} x
 * @param {number[]} queries
 * @return {number[]}
 */
var countServers = function(n, logs, x, queries) {
    const m = queries.length;
    // Attach original indices to queries so we can restore order later
    const indexedQueries = queries.map((q, idx) => [q, idx]);
    
    // Sort queries by time ascending
    indexedQueries.sort((a, b) => a[0] - b[0]);
    // Sort logs by time ascending
    logs.sort((a, b) => a[1] - b[1]);
    
    const res = new Array(m);
    const serverCount = new Map();
    
    let left = 0;
    let right = 0;
    const totalLogs = logs.length;
    
    for (const [qTime, originalIdx] of indexedQueries) {
        const windowStart = qTime - x;
        const windowEnd = qTime;
        
        // Expand the right pointer to include logs <= windowEnd
        while (right < totalLogs && logs[right][1] <= windowEnd) {
            const serverId = logs[right][0];
            serverCount.set(serverId, (serverCount.get(serverId) || 0) + 1);
            right++;
        }
        
        // Shrink the left pointer to remove logs < windowStart
        while (left < totalLogs && logs[left][1] < windowStart) {
            const serverId = logs[left][0];
            const count = serverCount.get(serverId);
            if (count === 1) {
                serverCount.delete(serverId);
            } else {
                serverCount.set(serverId, count - 1);
            }
            left++;
        }
        
        // Servers with zero requests = total servers (n) - servers with >= 1 request
        res[originalIdx] = n - serverCount.size;
    }
    
    return res;
};
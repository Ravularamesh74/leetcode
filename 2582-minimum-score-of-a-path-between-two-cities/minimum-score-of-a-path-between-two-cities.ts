function minScore(n: number, roads: number[][]): number {
    // 1. Build the adjacency list
    // Each node will map to an array of [neighbor, distance]
    const adj: Map<number, [number, number][]> = new Map();
    for (let i = 1; i <= n; i++) {
        adj.set(i, []);
    }
    
    for (const [u, v, dist] of roads) {
        adj.get(u)!.push([v, dist]);
        adj.get(v)!.push([u, dist]);
    }
    
    // 2. BFS to traverse the component containing city 1
    let minScore = Infinity;
    const visited = new Set<number>();
    const queue: number[] = [1];
    visited.add(1);
    
    let head = 0;
    while (head < queue.length) {
        const curr = queue[head++];
        
        const neighbors = adj.get(curr) || [];
        for (const [neighbor, dist] of neighbors) {
            // Track the minimum road distance seen in this connected component
            minScore = Math.min(minScore, dist);
            
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push(neighbor);
            }
        }
    }
    
    return minScore;
}
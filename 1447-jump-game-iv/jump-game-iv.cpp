class Solution {
public:
    int minJumps(vector<int>& arr) {
        int n = arr.size();

        if (n == 1) return 0;

        unordered_map<int, vector<int>> mp;

        // Store all indices for each value
        for (int i = 0; i < n; i++) {
            mp[arr[i]].push_back(i);
        }

        queue<int> q;
        vector<bool> visited(n, false);

        q.push(0);
        visited[0] = true;

        int steps = 0;

        while (!q.empty()) {
            int size = q.size();

            while (size--) {
                int idx = q.front();
                q.pop();

                // Reached end
                if (idx == n - 1)
                    return steps;

                // Move right
                if (idx + 1 < n && !visited[idx + 1]) {
                    visited[idx + 1] = true;
                    q.push(idx + 1);
                }

                // Move left
                if (idx - 1 >= 0 && !visited[idx - 1]) {
                    visited[idx - 1] = true;
                    q.push(idx - 1);
                }

                // Same value jumps
                for (int next : mp[arr[idx]]) {
                    if (!visited[next]) {
                        visited[next] = true;
                        q.push(next);
                    }
                }

                // IMPORTANT OPTIMIZATION
                mp[arr[idx]].clear();
            }

            steps++;
        }

        return -1;
    }
};
import java.util.HashMap;
import java.util.Map;

class Solution {
    public long minSumSquareDiff(int[] nums1, int[] nums2, int k1, int k2) {
        int n = nums1.length;
        long totalK = (long) k1 + k2;
        
        // Step 1: Find max difference to size our frequency bucket
        int maxDiff = 0;
        int[] diffCounts = new int[100001];
        
        for (int i = 0; i < n; i++) {
            int diff = Math.abs(nums1[i] - nums2[i]);
            diffCounts[diff]++;
            if (diff > maxDiff) {
                maxDiff = diff;
            }
        }
        
        // Step 2: Greedily reduce the largest differences
        for (int d = maxDiff; d > 0 && totalK > 0; d--) {
            if (diffCounts[d] == 0) continue;
            
            // Number of operations needed to reduce all elements with difference `d` to `d - 1`
            long operationsToReduce = Math.min(totalK, (long) diffCounts[d]);
            
            diffCounts[d] -= operationsToReduce;
            diffCounts[d - 1] += operationsToReduce;
            totalK -= operationsToReduce;
        }
        
        // Step 3: Calculate the minimum sum of squared differences
        long minSum = 0;
        for (int d = 1; d <= maxDiff; d++) {
            if (diffCounts[d] > 0) {
                minSum += (long) diffCounts[d] * d * d;
            }
        }
        
        return minSum;
    }
}
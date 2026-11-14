class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int min_sum = -1;
        int n = nums.size();
        
        // Try every possible starting position
        for (int i = 0; i < n; ++i) {
            int current_sum = 0;
            // Extend the subarray up to length r
            for (int j = i; j < n; ++j) {
                current_sum += nums[j];
                int len = j - i + 1;
                
                // Check if length is within [l, r] and sum is positive
                if (len >= l && len <= r) {
                    if (current_sum > 0) {
                        if (min_sum == -1 || current_sum < min_sum) {
                            min_sum = current_sum;
                        }
                    }
                }
                
                // If length exceeds r, we can stop extending this subarray
                if (len > r) {
                    break;
                }
            }
        }
        
        return min_sum;
    }
};
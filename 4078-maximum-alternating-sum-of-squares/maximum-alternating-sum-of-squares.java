import java.util.Arrays;

class Solution {
    public long maxAlternatingSum(int[] nums) {
        int n = nums.length;
        long[] squares = new long[n];
        
        for (int i = 0; i < n; i++) {
            long val = (long) nums[i];
            squares[i] = val * val;
        }
        
        Arrays.sort(squares);
        
        long score = 0;
        // The first n / 2 elements are subtracted, and the remaining are added.
        // (Alternatively, we can assign them strictly according to odd/even positions)
        int mid = n / 2;
        for (int i = 0; i < n; i++) {
            if (i < mid) {
                score -= squares[i];
            } else {
                score += squares[i];
            }
        }
        
        return score;
    }
}
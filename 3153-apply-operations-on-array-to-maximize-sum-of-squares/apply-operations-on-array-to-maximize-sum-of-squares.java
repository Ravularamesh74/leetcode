import java.util.List;

class Solution {
    public int maxSum(List<Integer> nums, int k) {
        int[] bitCount = new int[32];
        
        // Step 1: Count the total frequency of set bits at each position
        for (int num : nums) {
            for (int i = 0; i < 30; i++) {
                if ((num & (1 << i)) != 0) {
                    bitCount[i]++;
                }
            }
        }
        
        long MOD = 1_000_000_007;
        long totalSum = 0;
        
        // Step 2: Greedily construct the k numbers
        for (int i = 0; i < k; i++) {
            long currentNum = 0;
            for (int bit = 29; bit >= 0; bit--) {
                if (bitCount[bit] > 0) {
                    currentNum |= (1L << bit);
                    bitCount[bit]--;
                }
            }
            totalSum = (totalSum + (currentNum * currentNum) % MOD) % MOD;
        }
        
        return (int) totalSum;
    }
}
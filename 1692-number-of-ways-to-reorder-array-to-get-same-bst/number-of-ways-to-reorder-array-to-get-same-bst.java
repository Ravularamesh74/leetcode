import java.util.*;

class Solution {
    private static final int MOD = 1000000007;
    private long[][] table;

    public int numOfWays(int[] nums) {
        int n = nums.length;
        table = new long[n + 1][n + 1];
        
        // Precompute Pascal's triangle for binomial coefficients C(n, k)
        for (int i = 0; i <= n; i++) {
            table[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                table[i][j] = (table[i - 1][j - 1] + table[i - 1][j]) % MOD;
            }
        }

        List<Integer> list = new ArrayList<>();
        for (int num : nums) {
            list.add(num);
        }

        return (int)((getWays(list) - 1 + MOD) % MOD);
    }

    private long getWays(List<Integer> nums) {
        if (nums.size() <= 2) {
            return 1;
        }

        int root = nums.get(0);
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();

        for (int i = 1; i < nums.size(); i++) {
            if (nums.get(i) < root) {
                left.add(nums.get(i));
            } else {
                right.add(nums.get(i));
            }
        }

        long leftWays = getWays(left) % MOD;
        long rightWays = getWays(right) % MOD;

        int lSize = left.size();
        int rSize = right.size();

        long combinations = table[lSize + rSize][lSize];

        return (((combinations * leftWays) % MOD) * rightWays) % MOD;
    }
}
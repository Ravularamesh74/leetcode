class Solution {
    public int minMoves(int[] nums, int limit) {
        int n = nums.length;

        int[] diff = new int[2 * limit + 2];

        for (int i = 0; i < n / 2; i++) {

            int a = nums[i];
            int b = nums[n - 1 - i];

            int low = Math.min(a, b);
            int high = Math.max(a, b);

            int sum = a + b;

            // Initially 2 moves
            diff[2] += 2;

            // 2 -> 1 moves
            diff[low + 1] -= 1;

            // 1 -> 0 moves
            diff[sum] -= 1;

            // 0 -> 1 moves
            diff[sum + 1] += 1;

            // 1 -> 2 moves
            diff[high + limit + 1] += 1;
        }

        int ans = Integer.MAX_VALUE;
        int moves = 0;

        for (int s = 2; s <= 2 * limit; s++) {
            moves += diff[s];
            ans = Math.min(ans, moves);
        }

        return ans;

    }
}
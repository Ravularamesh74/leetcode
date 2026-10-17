import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    // Helper function to calculate the digit sum of a number
    private int getDigitSum(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }

    public int minSwaps(int[] nums) {
        int n = nums.length;
        
        // Store pairs of (number, digit sum) or create wrapper objects/indices
        Integer[] indices = new Integer[n];
        int[][] elements = new int[n][2]; // [value, digit_sum]
        
        for (int i = 0; i < n; i++) {
            indices[i] = i;
            elements[i][0] = nums[i];
            elements[i][1] = getDigitSum(nums[i]);
        }

        // Sort indices based on the custom comparator: digit sum first, then value
        Arrays.sort(indices, (a, b) -> {
            if (elements[a][1] != elements[b][1]) {
                return Integer.compare(elements[a][1], elements[b][1]);
            }
            return Integer.compare(elements[a][0], elements[b][0]);
        });

        // Find minimum swaps using cycle detection
        boolean[] visited = new boolean[n];
        int swaps = 0;

        for (int i = 0; i < n; i++) {
            // If already visited or already in the correct position
            if (visited[i] || indices[i] == i) {
                continue;
            }

            // Traverse the cycle
            int cycleSize = 0;
            int curr = i;
            while (!visited[curr]) {
                visited[curr] = true;
                curr = indices[curr];
                cycleSize++;
            }

            // If a cycle of size k requires k - 1 swaps
            if (cycleSize > 1) {
                swaps += (cycleSize - 1);
            }
        }

        return swaps;
    }
}
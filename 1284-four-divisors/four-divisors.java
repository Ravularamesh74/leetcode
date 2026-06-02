class Solution {
    
    public int sumFourDivisors(int[] nums) {
        int ans = 0;

        for (int num : nums) {
            int count = 0;
            int sum = 0;

            for (int d = 1; d * d <= num; d++) {
                if (num % d == 0) {
                    int other = num / d;

                    if (d == other) {
                        count++;
                        sum += d;
                    } else {
                        count += 2;
                        sum += d + other;
                    }

                    if (count > 4) {
                        break;
                    }
                }
            }

            if (count == 4) {
                ans += sum;
            }
        }

        return ans;
    
    }
}
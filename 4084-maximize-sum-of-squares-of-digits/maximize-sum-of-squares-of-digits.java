class Solution {
    public String maxSumOfSquares(int num, int sum) {
        // If sum is out of the possible range, return empty string
        if (sum < 1 || sum > 9L * num) {
            return "";
        }
        
        StringBuilder sb = new StringBuilder();
        int remainingSum = sum;
        
        for (int i = 0; i < num; i++) {
            int remainingPositions = num - 1 - i;
            
            // Try digits from 9 down to 0 (or 1 if it's the very first digit and remainingSum is small)
            int startDigit = (i == 0) ? Math.max(1, remainingSum - 9 * remainingPositions) : 0;
            int endDigit = Math.min(9, remainingSum);
            
            // We want the maximum score, but since we go top-down from 9, 
            // we need to find the highest digit 'd' such that the remaining sum is achievable.
            for (int d = endDigit; d >= startDigit; d--) {
                int minPossibleSum = Math.max(0, remainingSum - d - 9 * remainingPositions);
                int maxPossibleSum = remainingSum - d;
                
                // Check if remainingSum - d can be formed by the rest of the positions
                if (maxPossibleSum >= 0 && maxPossibleSum <= 9 * remainingPositions) {
                    sb.append(d);
                    remainingSum -= d;
                    break;
                }
            }
        }
        
        return sb.toString();
    }
}
class Solution {
public:
    int rotatedDigits(int n) {
        int count = 0;
        
        for (int i = 1; i <= n; i++) {
            int num = i;
            bool isValid = true;
            bool isGood = false;
            
            while (num > 0) {
                int digit = num % 10;
                
                // invalid digits
                if (digit == 3 || digit == 4 || digit == 7) {
                    isValid = false;
                    break;
                }
                
                // changing digits
                if (digit == 2 || digit == 5 || digit == 6 || digit == 9) {
                    isGood = true;
                }
                
                num /= 10;
            }
            
            if (isValid && isGood) {
                count++;
            }
        }
        
        return count;
    }
};
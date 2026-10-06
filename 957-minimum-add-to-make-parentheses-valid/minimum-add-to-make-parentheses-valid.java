class Solution {
    public int minAddToMakeValid(String s) {
        int open = 0;
        int close = 0;

        for (char c : s.toCharArray()) {
            if (c == '(') {
                open++;
            } else { // c == ')'
                if (open > 0) {
                    open--; // Match with an existing '('
                } else {
                    close++; // Unmatched ')' needing a '(' before it
                }
            }
        }

        return open + close;
    }
}
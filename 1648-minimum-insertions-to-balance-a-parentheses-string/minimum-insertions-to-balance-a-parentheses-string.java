class Solution {
    public int minInsertions(String s) {
        int insertions = 0;
        int openNeeded = 0; // Tracks unmatched '(' count
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            
            if (c == '(') {
                openNeeded++;
            } else { // c == ')'
                // Check if the next character is also ')'
                if (i + 1 < s.length() && s.charAt(i + 1) == ')') {
                    i++; // Skip the second ')'
                } else {
                    insertions++; // Need to insert one ')' to make a consecutive "))"
                }
                
                // Now we have a complete "))"
                if (openNeeded > 0) {
                    openNeeded--; // Matched with an existing '('
                } else {
                    insertions++; // No '(' available, need to insert one '('
                }
            }
        }
        
        // Each remaining unmatched '(' needs two ')'
        insertions += openNeeded * 2;
        
        return insertions;
    }
}
class Solution {

    class TrieNode {
        TrieNode[] child = new TrieNode[10];
    }

    public int longestCommonPrefix(int[] arr1, int[] arr2) {

        TrieNode root = new TrieNode();

        // Insert all numbers from arr1
        for (int num : arr1) {
            TrieNode curr = root;
            String s = String.valueOf(num);

            for (char c : s.toCharArray()) {
                int idx = c - '0';

                if (curr.child[idx] == null) {
                    curr.child[idx] = new TrieNode();
                }

                curr = curr.child[idx];
            }
        }

        int ans = 0;

        // Find longest matching prefix for arr2 numbers
        for (int num : arr2) {
            TrieNode curr = root;
            String s = String.valueOf(num);

            int len = 0;

            for (char c : s.toCharArray()) {
                int idx = c - '0';

                if (curr.child[idx] == null) {
                    break;
                }

                len++;
                curr = curr.child[idx];
            }

            ans = Math.max(ans, len);
        }

        return ans;
    }
}
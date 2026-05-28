class Solution {
    class TrieNode {
        TrieNode[] children = new TrieNode[26];

        // best index for this suffix
        int idx = -1;
    }

    TrieNode root = new TrieNode();
    String[] words;

    private void updateBest(TrieNode node, int index) {
        if (node.idx == -1) {
            node.idx = index;
            return;
        }

        String curr = words[node.idx];
        String next = words[index];

        // smaller length preferred
        if (next.length() < curr.length()) {
            node.idx = index;
        }
        // if same length, earlier index preferred
        else if (next.length() == curr.length() && index < node.idx) {
            node.idx = index;
        }
    }

    private void insert(String word, int index) {
        TrieNode node = root;

        // update root for empty suffix ""
        updateBest(node, index);

        // insert reversed word
        for (int i = word.length() - 1; i >= 0; i--) {
            int ch = word.charAt(i) - 'a';

            if (node.children[ch] == null) {
                node.children[ch] = new TrieNode();
            }

            node = node.children[ch];

            updateBest(node, index);
        }
    }

    private int query(String word) {
        TrieNode node = root;

        for (int i = word.length() - 1; i >= 0; i--) {
            int ch = word.charAt(i) - 'a';

            if (node.children[ch] == null) {
                break;
            }

            node = node.children[ch];
        }

        return node.idx;
    }

    public int[] stringIndices(String[] wordsContainer, String[] wordsQuery) {

        words = wordsContainer;

        // build trie
        for (int i = 0; i < wordsContainer.length; i++) {
            insert(wordsContainer[i], i);
        }

        int[] ans = new int[wordsQuery.length];

        for (int i = 0; i < wordsQuery.length; i++) {
            ans[i] = query(wordsQuery[i]);
        }

        return ans;
    
    }
}
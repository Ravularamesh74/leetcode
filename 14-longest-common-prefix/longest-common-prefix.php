class Solution {

    /**
     * @param String[] $strs
     * @return String
     */
    function longestCommonPrefix($strs) {
        if (empty($strs)) return "";

        $first = $strs[0];

        for ($i = 0; $i < strlen($first); $i++) {
            $char = $first[$i];

            for ($j = 1; $j < count($strs); $j++) {
                // Check bounds + mismatch
                if ($i >= strlen($strs[$j]) || $strs[$j][$i] !== $char) {
                    return substr($first, 0, $i);
                }
            }
        }

        return $first;
    }
}
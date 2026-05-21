class Solution {

    List<List<Integer>> ans = new ArrayList<>();

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {

        Arrays.sort(candidates);

        backtrack(candidates, target, 0, new ArrayList<>());

        return ans;
    }

    private void backtrack(int[] nums, int target,
                           int start, List<Integer> curr) {

        if (target == 0) {
            ans.add(new ArrayList<>(curr));
            return;
        }

        for (int i = start; i < nums.length; i++) {

            // skip duplicates
            if (i > start && nums[i] == nums[i - 1]) {
                continue;
            }

            // pruning
            if (nums[i] > target) {
                break;
            }

            curr.add(nums[i]);

            // i + 1 because each number can be used once
            backtrack(nums, target - nums[i], i + 1, curr);

            curr.remove(curr.size() - 1);
        }
    }
}
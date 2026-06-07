class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(index, subset):
            if index == len(nums):
                result.append(subset[:])
                return

            # Include nums[index]
            subset.append(nums[index])
            backtrack(index + 1, subset)

            # Exclude nums[index]
            subset.pop()
            backtrack(index + 1, subset)

        backtrack(0, [])
        return result
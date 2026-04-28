class Solution {
    fun fourSum(nums: IntArray, target: Int): List<List<Int>> {
        nums.sort()
        val n = nums.size
        val res = mutableListOf<List<Int>>()

        for (i in 0 until n - 3) {
            // skip duplicates for i
            if (i > 0 && nums[i] == nums[i - 1]) continue

            // pruning
            if (nums[i].toLong() + nums[i + 1] + nums[i + 2] + nums[i + 3] > target) break
            if (nums[i].toLong() + nums[n - 1] + nums[n - 2] + nums[n - 3] < target) continue

            for (j in i + 1 until n - 2) {
                // skip duplicates for j
                if (j > i + 1 && nums[j] == nums[j - 1]) continue

                var left = j + 1
                var right = n - 1

                while (left < right) {
                    val sum = nums[i].toLong() +
                              nums[j].toLong() +
                              nums[left].toLong() +
                              nums[right].toLong()

                    when {
                        sum == target.toLong() -> {
                            res.add(listOf(nums[i], nums[j], nums[left], nums[right]))

                            // skip duplicates
                            while (left < right && nums[left] == nums[left + 1]) left++
                            while (left < right && nums[right] == nums[right - 1]) right--

                            left++
                            right--
                        }
                        sum < target -> left++
                        else -> right--
                    }
                }
            }
        }
        return res
    }
}
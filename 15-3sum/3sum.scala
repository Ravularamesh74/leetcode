object Solution {
    def threeSum(nums: Array[Int]): List[List[Int]] = {
        val result = scala.collection.mutable.ListBuffer[List[Int]]()
        val arr = nums.sorted

        for (i <- 0 until arr.length - 2) {
            // Skip duplicates
            if (i > 0 && arr(i) == arr(i - 1)) {
                // continue
            } else {
                var left = i + 1
                var right = arr.length - 1

                while (left < right) {
                    val sum = arr(i) + arr(left) + arr(right)

                    if (sum == 0) {
                        result += List(arr(i), arr(left), arr(right))

                        // Skip duplicates for left
                        while (left < right && arr(left) == arr(left + 1)) left += 1
                        // Skip duplicates for right
                        while (left < right && arr(right) == arr(right - 1)) right -= 1

                        left += 1
                        right -= 1
                    }
                    else if (sum < 0) {
                        left += 1
                    }
                    else {
                        right -= 1
                    }
                }
            }
        }

        result.toList
    }
}
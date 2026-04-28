package main

import "sort"

func fourSum(nums []int, target int) [][]int {
    sort.Ints(nums)
    n := len(nums)
    res := [][]int{}

    for i := 0; i < n-3; i++ {
        // skip duplicates for i
        if i > 0 && nums[i] == nums[i-1] {
            continue
        }

        // pruning
        if nums[i]+nums[i+1]+nums[i+2]+nums[i+3] > target {
            break
        }
        if nums[i]+nums[n-1]+nums[n-2]+nums[n-3] < target {
            continue
        }

        for j := i + 1; j < n-2; j++ {
            // skip duplicates for j
            if j > i+1 && nums[j] == nums[j-1] {
                continue
            }

            left, right := j+1, n-1

            for left < right {
                sum := nums[i] + nums[j] + nums[left] + nums[right]

                if sum == target {
                    res = append(res, []int{
                        nums[i], nums[j], nums[left], nums[right],
                    })

                    // skip duplicates
                    for left < right && nums[left] == nums[left+1] {
                        left++
                    }
                    for left < right && nums[right] == nums[right-1] {
                        right--
                    }

                    left++
                    right--
                } else if sum < target {
                    left++
                } else {
                    right--
                }
            }
        }
    }

    return res
}
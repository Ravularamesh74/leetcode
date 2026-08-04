#include <vector>
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    std::vector<int> findMissingElements(std::vector<int>& nums) {
        std::unordered_set<int> num_set(nums.begin(), nums.end());
        int min_val = *std::min_element(nums.begin(), nums.end());
        int max_val = *std::max_element(nums.begin(), nums.end());
        
        std::vector<int> missing;
        for (int i = min_val; i <= max_val; ++i) {
            if (num_set.find(i) == num_set.end()) {
                missing.push_back(i);
            }
        }
        return missing;
    }
};
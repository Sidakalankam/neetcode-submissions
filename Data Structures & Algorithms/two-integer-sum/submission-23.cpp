#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numHash;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            if (numHash.count(complement)) {
                return {numHash[complement], i};
            }

            numHash[nums[i]] = i;
        }

        return {}; // problem guarantees a solution
    }
};

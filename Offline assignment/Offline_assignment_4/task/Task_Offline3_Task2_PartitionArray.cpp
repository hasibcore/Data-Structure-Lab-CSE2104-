// LeetCode 2161. Partition Array According to Given Pivot
// Problem Link: https://leetcode.com/problems/partition-array-according-to-given-pivot/
// Related Assignment: Offline 3 - Task 2

#include <vector>
using namespace std;

class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> ans(nums.size());
        int left = 0, right = nums.size() - 1;
        
        for (int i = 0, j = nums.size() - 1; i < nums.size(); i++, j--) {
            if (nums[i] < pivot) {
                ans[left++] = nums[i];
            }
            if (nums[j] > pivot) {
                ans[right--] = nums[j];
            }
        }
        
        while (left <= right) {
            ans[left++] = pivot;
        }
        
        return ans;
    }
};

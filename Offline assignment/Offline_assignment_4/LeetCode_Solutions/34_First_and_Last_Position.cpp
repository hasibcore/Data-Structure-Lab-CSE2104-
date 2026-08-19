// LeetCode 34. Find First and Last Position of Element in Sorted Array
// Problem Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
// Matching Assignment: Offline 1 (Lower Bound & Upper Bound)

#include <vector>
using namespace std;

class Solution {
private:
    int lowerBound(const vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1;
        int ans = nums.size();
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] >= target) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

    int upperBound(const vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1;
        int ans = nums.size();
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] > target) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int lb = lowerBound(nums, target);
        int ub = upperBound(nums, target);
        
        if (lb == nums.size() || nums[lb] != target) {
            return {-1, -1};
        }
        
        return {lb, ub - 1};
    }
};

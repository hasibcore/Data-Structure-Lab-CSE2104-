// LeetCode 4. Median of Two Sorted Arrays
// Problem Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
// Related Assignment: Offline 3 - Task 7

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

        vector<int> nums;
        int i = 0, j = 0;

        while (i < nums1.size() && j < nums2.size()) {
            if (nums1[i] <= nums2[j])
                nums.push_back(nums1[i++]);
            else
                nums.push_back(nums2[j++]);
        }

        while (i < nums1.size())
            nums.push_back(nums1[i++]);

        while (j < nums2.size())
            nums.push_back(nums2[j++]);

        int n = nums.size();

        if (n % 2 == 1)
            return nums[n / 2];

        return (nums[n / 2 - 1] + nums[n / 2]) / 2.0;
    }
};

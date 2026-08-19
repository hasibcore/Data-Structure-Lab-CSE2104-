// LeetCode 19. Remove Nth Node From End of List
// Problem Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
// Matching Assignment: Offline 4 (Deleting previous of last node / node from end)

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* first = dummy;
        ListNode* second = dummy;
        
        for (int i = 0; i <= n; i++) {
            first = first->next;
        }
        
        while (first != nullptr) {
            first = first->next;
            second = second->next;
        }
        
        ListNode* toDelete = second->next;
        second->next = second->next->next;
        delete toDelete;
        
        ListNode* result = dummy->next;
        delete dummy;
        return result;
    }
};

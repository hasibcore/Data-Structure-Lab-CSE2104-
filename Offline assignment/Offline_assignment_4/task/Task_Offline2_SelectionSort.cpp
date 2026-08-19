// LeetCode 912. Sort an Array
// Problem Link: https://leetcode.com/problems/sort-an-array/
// Related Assignment: Offline 2 (Selection Sort / Custom Sort)

#include <vector>
#include <string>
#include <algorithm>
using namespace std;

struct Book {
    string bName;
    string author;
    int y;
};

class Solution {
public:
    void selectionSort(vector<Book>& b) {
        int n = b.size();
        for (int i = 0; i < n - 1; i++) {
            int maxIdx = i;
            for (int j = i + 1; j < n; j++) {
                if (b[j].y > b[maxIdx].y) {
                    maxIdx = j;
                } else if (b[j].y == b[maxIdx].y) {
                    if (b[j].author < b[maxIdx].author) {
                        maxIdx = j;
                    } else if (b[j].author == b[maxIdx].author) {
                        if (b[j].bName < b[maxIdx].bName) {
                            maxIdx = j;
                        }
                    }
                }
            }
            swap(b[i], b[maxIdx]);
        }
    }
};

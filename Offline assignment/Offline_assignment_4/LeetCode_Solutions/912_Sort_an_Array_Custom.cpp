// LeetCode practice for Selection Sort / Custom Sorting Logic
// Problem Link: https://leetcode.com/problems/sort-an-array/
// Matching Assignment: Offline 2 (Custom Sorting with Selection Sort logic)

#include <vector>
#include <string>
#include <algorithm>
using namespace std;

// Struct definition matching Offline 2
struct Book {
    string bName;
    string author;
    int y;
};

class Solution {
public:
    // Selection sort algorithm tailored for Book struct (Offline 2 logic)
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

#include<bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    vector<int> v(n);
    cout << "Enter elements: ";
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    // Selection Sort
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (v[j] < v[minIdx]) {
                minIdx = j;
            }
        }
        // Swap the found minimum with the first unsorted element
        if (minIdx != i) {
            swap(v[i], v[minIdx]);
        }
    }

    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) {
        cout << v[i] << " ";
    }
    cout << endl;

    return 0;
}

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

    // Bubble Sort
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (v[j] > v[j + 1]) {
                swap(v[j], v[j + 1]);
                swapped = true;
            }
        }
        // If no swap occurred in this pass, array is sorted
        if (!swapped) break;
    }

    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) {
        cout << v[i] << " ";
    }
    cout << endl;

    return 0;
}

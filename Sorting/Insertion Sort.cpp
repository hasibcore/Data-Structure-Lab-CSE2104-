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

    // Insertion Sort
    for (int i = 1; i < n; i++) {
        int key = v[i];
        int j = i - 1;
        // Shift elements greater than key one position ahead
        while (j >= 0 && v[j] > key) {
            v[j + 1] = v[j];
            j--;
        }
        v[j + 1] = key;
    }

    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) {
        cout << v[i] << " ";
    }
    cout << endl;

    return 0;
}

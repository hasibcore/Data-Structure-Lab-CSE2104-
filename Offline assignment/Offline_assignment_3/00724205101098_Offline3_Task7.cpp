/* 7. Given two sorted arrays, find the median of the combined sorted array using merge sort.
Also print the merged array.*/

#include<bits/stdc++.h>
using namespace std;

void Merge(vector<double> &v, int low, int mid, int high)
{
    int i = low;
    int j = mid + 1;
    int k = low;

    vector<double> temp(v.size());

    while(i <= mid && j <= high)
    {
        if(v[i] <= v[j])
        {
            temp[k] = v[i];
            i++;
        }
        else
        {
            temp[k] = v[j];
            j++;
        }
        k++;
    }

    while(i <= mid)
    {
        temp[k] = v[i];
        i++;
        k++;
    }

    while(j <= high)
    {
        temp[k] = v[j];
        j++;
        k++;
    }

    for(int x = low; x <= high; x++)
        v[x] = temp[x];
}

void merge_sort(vector<double> &v, int low, int mid, int high)
{
    Merge(v, low, mid, high);
}

int main()
{
    int n1, n2;
    cin >> n1 >> n2;

    vector<double> a(n1), b(n2);

    for(auto &x : a)
        cin >> x;

    for(auto &x : b)
        cin >> x;

    vector<double> v;

    for(auto &x : a)
        v.push_back(x);

    for(auto &x : b)
        v.push_back(x);

    merge_sort(v, 0, n1 - 1, n1 + n2 - 1);

    cout << "Merged Array: ";
    for(auto x : v)
        cout << x << " ";

    double med;

    int n = n1 + n2;

    if(n % 2 == 1)
    {
        med = v[n / 2];
    }
    else
        med = (v[n / 2 - 1] + v[n / 2]) / 2.0;

    cout << "\nMedian: " << med;

    return 0;
}


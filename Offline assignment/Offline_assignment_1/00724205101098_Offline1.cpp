#include <bits/stdc++.h>
using namespace std;
void binarySearch( vector<int> v, int key)
{
    int flag = 0;

    int high = v.size() - 1;
    int low = 0;
    int mid;

    sort(v.begin(), v.end());

    while(low <= high)
    {
        mid = (low + high) / 2;

        if(key == v[mid])
        {
            flag = 1;
            break;
        }
        else if(key > v[mid])
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }

    if(flag == 1)
    {
        cout << "Book Found";
    }
    else 
    {
        cout << "Book Not Found";
    }
}

int lowerBound(vector<int> a, int key)
{
    int low = 0, high = a.size() - 1;
    int ans = a.size();

    while (low <= high)
    {
        int mid = (low + high) / 2;

        if (a[mid] >= key)
        {
            ans = mid;
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }

    return ans;
}

int upperBound(vector<int> a, int key)
{
    int low = 0, high = a.size() - 1;
    int ans = a.size();

    while (low <= high)
    {
        int mid = (low + high) / 2;

        if (a[mid] > key)
        {
            ans = mid;
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }

    return ans;
}

int main() {
   
    int n, x, key;
    vector<int> vec;

    cin >> n;

    for(int i = 0; i < n; i++)
    {
        cin >> x;
        vec.push_back(x);
    }

    cin >> key;

    binarySearch(vec, key);
    cout << endl;

    int lb = lowerBound(vec,key);
    cout << "Lower Bound Index: " << lb << endl;

    
    int ub = upperBound(vec,key);
    cout << "Upper Bound Index: " << ub << endl;

    return 0;
}

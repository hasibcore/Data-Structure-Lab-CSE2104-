#include<iostream>
#include<vector>
using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> arr(n);

    for(int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int key;
    cout << "Enter the element to search: ";
    cin >> key;

    bool flag = false;

    for(int i = 0; i < n; i++)
    {
        if(arr[i] == key)
        {
            cout << "Found at index: " << i << endl;
            flag = true;
            break;
        }
    }

    if(flag == false)
    {
        cout << "Not Found";
    }

    return 0;
}
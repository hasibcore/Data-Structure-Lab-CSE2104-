#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];

    }
    for(int i=0;i<n;i++)
    {


        for(int j=i+1;j<n;j++)
        {


            if(arr[j]>arr[i])
            {
               swap(arr[j],arr[i]);
            }

        }
    }
    cout<<arr[1];
}

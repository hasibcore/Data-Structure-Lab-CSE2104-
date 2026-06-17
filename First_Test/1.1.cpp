#include<iostream>
using namespace std;
int main()
{
    int a;
    cin>>a;
    int arr[a];
if(1<=a && a<=100){
    for(int i=0;i<a;i++)
    {
        cin>>arr[i];
    }
    int max=arr[0];
    for(int i=0;i<a;i++)
    {
        if(arr[i]>max)
        {
            max=arr[i];
        }

    }
    cout<<max;
}
}

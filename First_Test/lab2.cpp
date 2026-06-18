#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    if(n>=1 && n<=100)
    {
        int arr[n];
        for (int i=0;i<n;i++)
        {
            cin>>arr[i];
        }
        int temp;
      for(int i=0;i<n/2;i++)
      {
          temp=arr[n-1-i];
          arr[n-1-i]=arr[i];
          arr[i]=temp;

      }
      for (int i=0;i<n;i++)
        {
            cout<<arr[i]<<" ";
        }
    }

}

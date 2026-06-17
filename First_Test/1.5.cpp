#include<iostream>
using namespace std;
int main()
{
   int n;
   cin>>n;
   int arr[n],t1[n],t2[n],m=0,p=0;
   for(int i=0;i<n;i++)
   {
       cin>>arr[i];
   }
    for(int i=0;i<n;i++)
    {
        if(arr[i]%2==0)
        {
            t1[m]=arr[i];
            m++;
        }
        else
        {
            t2[p]=arr[i];
            p++;
        }

    }
    int j=0;
    for(int i=0;i<n;i++)
    {
        if(i<m)
        {
            arr[i]=t1[i];
        }
        else{

            arr[i]=t2[j];
            j++;
        }
        cout<<arr[i]<<" ";
    }


}

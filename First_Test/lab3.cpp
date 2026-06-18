#include<bits/stdc++.h>

using namespace std;
int main()
{
    int n,z,in=0,i;
    cin>>n;
    int arr[100];

   while(n!=0){
    z=n%10;
    arr[in]=z;
    in++;
    n=n/10;

   }

   sort(arr,arr+in);
     cout<<arr[1];

}

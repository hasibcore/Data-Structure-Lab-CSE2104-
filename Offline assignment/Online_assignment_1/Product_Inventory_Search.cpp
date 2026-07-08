#include<bits/stdc++.h>
using namespace std;
int binarySearch(vector<int>v,int key)
{
 int low=0;
 int high=v.size()-1;
 while(low<=high)
 {
     int mid=(low+high)/2;
     if(key==v[mid])
     {
         return 1;
     }
     else if(key>v[mid])
     {
         low=mid+1;
     }
     else{
        high=mid-1;
     }

 }
 return -1;
}
 int upperBound(vector<int>v,int key)
 {
     int high=v.size()-1,low=0;
     while(high>=low)
     {
       int mid=(high+low)/2;
         if(key>v[mid])
         {
             low=mid+1;
         }
         else{
            high=mid-1;
         }
     }
     return low;
 }
 int lowerbound(vector<int>v,int key)
 {
     int high=v.size()-1,low=0;
     while(high>=low)
     {
       int mid=(high+low)/2;
         if(key>=v[mid])
         {
             low=mid+1;
         }
         else{
            high=mid-1;
         }
     }
     return low;
 }
int main()
{
    int n;
    cin>>n;
    vector<int>v;
    for(int i=0;i<n;i++)
{
    int x;
    cin>>x;
    v.push_back(x);

}
 int key;
 cin>>key;

 sort(v.begin(),v.end());
 int q=binarySearch(v,key);
 if(q==1)
 {
    cout<<"Found"<<endl;
 }
    else {
    cout<<"Not found"<<endl;
    }
    cout<<"Upper Bound Index : "<<upperBound(v,key)<<endl;
    cout<<"Lower Bound Index : "<<lowerbound(v,key)<<endl;
}

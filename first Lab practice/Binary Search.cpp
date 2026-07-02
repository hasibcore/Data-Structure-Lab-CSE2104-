#include<bits/stdc++.h>
using namespace std;
int searchBinary(vector<int>v,int target)
{
    int high=v.size()-1;
    int low=0;

    while(high>=low){
            int mid=(high+low)/2;
        if(target==v[mid]){
            return mid;
            break;
        }
        else if(target>v[mid])
        {
            low=mid+1;
        }
    else{
        high=mid-1;
    }

    }
    return -1;
}
int main ()
{
  int n,target;
  cin>>n;
  vector<int>v;
  for(int i=0;i<n;i++){
    int x;
    cin>>x;
    v.push_back(x);
  }

#include<bits/stdc++.h>
using namespace std;
void binarySearch(vector<int>v1,vector<int>v2)
{
  for(int i=0;i<v2.size();i++){
    int high=v1.size()-1;
    int low =0;
    int ans=v1.size();
    while(high>=low)
    {
      int mid=(high+low)/2;
      if(v2[i]==v1[mid])
      {
        ans=mid;
        break;

      }
      else if(v2[i]<v1[mid])
      {
        ans=mid;
        high=mid-1;
      }
      else{
        low=mid+1;
      }

    }
    if(ans==v1.size()){
      cout<<"-1"<<endl;
    }
    else{
      cout<<ans+1<<endl;
    }
  }

}
int main()
{
  int n,m;
  cin>>n>>m;
  vector <int> v1;
  vector <int> v2;
  for(int i=0;i<n;i++)
  {
    int x;
    cin>>x;
    v1.push_back(x);
  }
  for(int i=0;i<m;i++)
  {
    int x;
    cin>>x;
    v2.push_back(x);
  }
  sort(v1.begin(),v1.end());
  binarySearch(v1,v2);
}

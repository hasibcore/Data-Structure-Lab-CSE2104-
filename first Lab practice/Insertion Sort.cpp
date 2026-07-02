#include<bits/stdc++.h>
using namespace std;
int main()
    {
    int n;
    cin>>n;
    vector<int>v;
    int x;
for(int i=0;i<n;i++)
    {

        cin>>x;
        v.push_back(x);

    }
    for(int i=1;i<n;i++)
    {
     int key=v[i];
     int j=i-1;
      while(j>=0 && v[j]>key)
      {

      v[j+1]=v[j];
        j--;
        }
        v[j+1]=key;
    }
    for(int i=0;i<n;i++)
    {
        cout<<v[i]<<" ";
    }


}

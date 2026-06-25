#include<bits/stdc++.h>
using namespace std;

void search(int a,vector<int> v,int m)

{

    int flag=0;

int high=v.size()-1;
    int low=0;
    int l;
    //if(v[i]==m)
    sort(v.begin(),v.end());
    while(low<=high)
    {
         l=(high+low)/2;
        if(m==v[l])
        {
            flag=1;
            break;
        }
     else if(m>v[l])
      {

         low=l+1;
      }
       else {
        high=l-1;

       }

        }
if(flag==1){
    cout<<"found";
}
else{
    cout<<"not found";
}


}



int main()
{
    int n,x,m;
    vector<int> v;
    cin>>n;

    for(int i=0;i<n;i++)
    {
        cin>>x;
        v.push_back(x);
    }
     cout<<"enter searched elements :";

    cin>>m;
  search(n,v,m);
      return 0;
}

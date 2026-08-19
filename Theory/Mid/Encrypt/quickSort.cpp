#include<bits/stdc++.h>
using namespace std;
int part(vector<int> &v,int h,int l,int id)
{
    int pv;
  if(id<50)
  {
       pv=v[h];
  }
 else{
     pv=v[l];
 }
 int i=l,j=h;
 while(i<j)
 {
     while(v[i]<=pv && i<=j)
     {
         i++;
     }
     while(v[j]>pv && i<=j)
     {
         j--;
     }
     if(i<j)
     {
    swap(v[i],v[j]);

     i++;
     j--;
     }
 }
 if(id<50){
   swap(v[h],v[i]);
   return i;
 }
 else{
     swap(v[l],v[j]);
   return j;

 }
}
void sortQ(vector<int>&v,int h,int l,int id)
{
    if(l<h)
    {
        int p=part(v,h,l,id);
        sortQ(v,p-1,l,id);
        sortQ(v,h,p+1,id);

    }
}
int main()
{
    int n,id;
    cin>>n;
    cin>>id;
    vector<int>v(n);
    for(auto &x:v)
    {
        cin>>x;

    }

    sortQ(v,v.size()-1,0,id);
    for(auto x:v)
    {
        cout<<x<<" ";
    }

}

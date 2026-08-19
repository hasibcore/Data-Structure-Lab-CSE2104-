// 2.During each partition of Quick Sort, print the pivot value, the array after partitioning, and the pivot's final index.
#include<bits/stdc++.h>
using namespace std;
int c=0;
int part(vector<int>&v,int l,int h)
{
    int i=l,j=h,pv=v[l];
    cout<<"Pivot index : "<<l<<" and Pivot no. "<< c<<" : "<<pv<<endl;
    while(i<j)
    {
        while(v[i]<=pv && i<h)
        {
            i++;
        }
        while(v[j]>pv && j>l)
        {
            j--;
        }
        if(i<j){
            swap(v[i],v[j]);
        }
    }
    swap(v[l],v[j]);
    return j;
}
void QuickSort(vector<int>&v,int l,int h)
{
    if(l<h)
    {
        int pt=part(v,l,h);
        QuickSort(v,l,pt-1);
        QuickSort(v,pt+1,h);

    }
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
   QuickSort(v,0,v.size()-1);
   for(int i=0;i<v.size();i++)
   {
    cout<<v[i]<<" ";
   }


}

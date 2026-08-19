// 1.Implement Quick Sort using the last element as the pivot and sort the given array in ascending order.
#include <bits/stdc++.h>
using namespace std;
 int partition(vector<int>&v,int low,int high)
 {
    int pv=v[high];
    int i=low,j=high;
    while(i<j)
    {
        while(pv>v[i] && i<high)
        {
            i++;
        }
        while(pv<=v[j] && j>low)
        {
            j--;
        }
        if(i<j)
        {
            swap(v[i],v[j]);
            //i++;
           // j--;
        }
    }
    swap(v[i],v[high]);
    return i;
 }
  void Sort(vector<int>&v,int low,int high)
  {
        if(low<high)
        {
            int pt=partition(v,low,high);
            Sort(v,low,pt-1);
            Sort(v,pt+1,high);
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
   Sort(v,0,v.size()-1);
   for(int i=0;i<v.size();i++)
   {
    cout<<v[i]<<" ";
   }
}

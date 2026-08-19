//3.Count the total number of comparisons and swaps performed by Quick Sort while sorting the array.
#include <bits/stdc++.h>
using namespace std;
int com=0,sw=0;
 int partition(vector<int>&v,int low,int high)
 {
    int pv=v[high];
    int i=low,j=high;
    while(i<j)
    {
        com++;
        while(pv>v[i] && i<high)
        {
            i++;
            com++;
        }
        com++;
        while(pv<=v[j] && j>low)
        {
            j--;
            com++;
        }
        com++;
        if(i<j)
        {
            swap(v[i],v[j]);
            sw++;
            com++;

        }
        com++;
    }
    swap(v[i],v[high]);
    com++;
    sw++;
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
   cout<<"Compare : "<<com<<endl;
   cout<<"Swap : "<<sw<<endl;
   for(int i=0;i<v.size();i++)
   {
    cout<<v[i]<<" ";
   }
}

/* 1. Given an array of N integers, simulate Quick Sort using the last element as pivot and
count the number of comparisons performed during the sorting process. */

#include<bits/stdc++.h>
using namespace std;
int comp=0;
int Sort(vector<int>&v,int high,int low)
{
    int pv=v[high];
    int i=low;
    int j=high;

    while(i<j){
      while(i<high && pv>v[i])
      {
        i++;
        comp++;
      }
    comp++;
       while(j>low && pv<=v[j])
       {
        j--;
        comp++;
        }
    comp++;
    if(i<j)
    {
       swap(v[i],v[j]);
    }


    }

    swap(v[i],v[high]);
    return i;
}
void quickSort(vector<int>&v,int high,int low)
{

    if(high>low)
    {
        int pt=Sort(v,high,low);
        quickSort(v,pt-1,low);
        quickSort(v,high,pt+1);
    }
}

int main()
{
    int n;
  vector<int>v;
  cin>>n;
  for(int i=0;i<n;i++)
  {
      int x;
      cin>>x;
      v.push_back(x);

  }

  quickSort(v,n-1,0);
  for(auto x:v)
  {
      cout<<x<<" ";
  }
  cout<<endl<<comp;

}

/* 2. Given an array and a pivot, rearrange the array such that elements less than pivot come
before it and greater come after.*/
#include<bits/stdc++.h>
using namespace std;

void Sort(vector<int>&v,int high,int low,int pv)
{

    int i=low;
    int j=high;
    int k;
  for(k=low;k<=high;k++)
  {
    if(v[k]==pv)
    {
        break;
    }
  }
  swap(v[k],v[high]);
    while(i<j){
      while(i<high && pv>v[i])
      {
        i++;

      }

       while(j>low && pv<=v[j])
       {
        j--;

        }

    if(i<j)
    {
       swap(v[i],v[j]);
    }


    }

    swap(v[i],v[high]);

}
void quickSort(vector<int>&v,int high,int low,int pv)
{

    if(high>low)
    {
        Sort(v,high,low,pv);

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
 int pv;
 cin>>pv;
  quickSort(v,n-1,0,pv);
  for(auto x:v)
  {
      cout<<x<<" ";
  }


}

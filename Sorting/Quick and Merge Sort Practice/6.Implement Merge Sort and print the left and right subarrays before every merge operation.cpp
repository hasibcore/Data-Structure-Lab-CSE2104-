//6.Implement Merge Sort and print the left and right subarrays before every merge operation.
#include <bits/stdc++.h>
using namespace std;
void Merge(vector<int>&v,int l,int h,int mid)
{
    int i=l,j=mid+1,k=l;
    vector<int>temp;
    while(i<=mid && j<=h)
    {
        if(v[i]<v[j])
        {
            temp.push_back(v[i]);
            k++;
            i++;
        }
        else{

            temp.push_back(v[j]);
            k++;
            j++;
        }
    }
    if(i<=mid)
    {
        while(i<=mid)
        {
            temp.push_back(v[i]);
            k++;
            i++;
        }
    }
    else{

        temp.push_back(v[j]);
            k++;
            j++;
    }
    for(int i=0;i<temp.size();i++)
    {
        v[l+i]=temp[i];
    }

}

void Sort(vector<int>&v,int low,int high)
  {
        if(low<high)
        {
            int mid=(high+low)/2;
            Sort(v,low,mid);

            Sort(v,mid+1,high);
            Merge(v,low,high,mid);

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
  // cout<<"Compare : "<<com<<endl;
  // cout<<"Swap : "<<sw<<endl;
   for(int i=0;i<v.size();i++)
   {
    cout<<v[i]<<" ";
   }
}


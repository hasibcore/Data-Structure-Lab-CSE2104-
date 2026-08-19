#include<bits/stdc++.h>
using namespace std;
void selectionSort(vector<int>&v)
{
    int l=0,h=v.size()-1;
    while(h!=l)
    {
        int i=l,j=h,mi=l,mx=h;
        while(i<=h)
        {
            if(v[i]<v[mi])
            {
                mi=i;
            }
            i++;
        }
        swap(v[mi],v[l]);


        while(j>=l)
        {
            if(v[j]>v[mx])
            {
                mx=j;
            }
            j--;
        }
        swap(v[mx],v[h]);
        l++;
        h--;

    }
}
int main()
{
    vector<int>v;
    int n,x;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>x;
        v.push_back(x);
    }
    selectionSort(v);
     for(int i=0;i<n;i++)
    {
        cout<<v[i]<<" ";
    }

}

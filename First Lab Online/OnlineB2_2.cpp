#include<bits/stdc++.h>
using namespace std;
void sorted(vector <int> &v)
{
    for(int i=0;i<v.size()-1;i++)
    {
        int min=i;
        for(int j=i+1;j<v.size();j++)
        {
            if(v[min]>v[j] && v[j]%2==0 && v[min]%2==0)
                min=j;

        }
        swap(v[min],v[i]);
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
    sorted(v);
    for(int i=0;i<n;i++)
    {
        cout<<v[i]<<" ";
    }
}

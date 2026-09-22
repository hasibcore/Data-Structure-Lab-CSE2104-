#include<bits/stdc++.h>
using namespace std;
bool DFS(vector<int>g[],int start,vector<int>&color)
{
    color[start]=0;
    for(int i=0;i<g[start].size();i++)
    {
        int ngh=g[start][i];
        if(color[ngh]==-1)
        {

            DFS(g,ngh,color);
            color[ngh]=1-color[start];
        }
        else if(color[ngh]==color[start])
        {
            return false;
        }
    }
    return true;
}
 int main()
 {
     int n,e;
     cin>>n>>e;
     vector<int>g[n+1];
     vector<int>color(n,-1);
     for(int i=0;i<e;i++)
     {
         int a,b;
         cin>>a>>b;
         g[a].push_back(b);
         g[b].push_back(a);
     }

     for(int i=0;i<n;i++)
     {
         if(color[i]==-1)
         {
             bool m=DFS(g,i,color);
               if(m==false)
         {
             cout<<"Biparthite not possible ";
             return 0;
         }
         }

     }
     cout<<"group 1 : ";
     for(int i=0;i<color.size();i++)
     {
         if(color[i]==0)
         {
             cout<<i<<" ";
         }
     }
    cout<<endl;
     cout<<"group 2 : ";
     for(int i=0;i<color.size();i++)
     {
         if(color[i]==1)
         {
             cout<<i<<" ";
         }
     }
 }

#include<bits/stdc++.h>
using namespace std;

void DFS(vector<int>g[],int st,int n,vector<bool>&marked)
{
    cout<<st<<" ";
    marked[st]=true;

    for(int i=0;i<g[st].size();i++)
    {
        int ng=g[st][i];
        if(!marked[ng])
        {
            DFS(g,ng,n,marked);
        }
    }
}

int main()
{
    int n,e;
    cin>>n>>e;
    vector<int>graph[n+1];
    vector<bool>marked(n+1,false);
    for(int i=0;i<e;i++)
    {
        int a,b;
        cin>>a>>b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    for(int i=0;i<n;i++)
    {
     if(!marked[i])
     {
      DFS(graph,i,n,marked);
     }
    }
}

#include<bits/stdc++.h>
using namespace std;

void DFS(vector<int>g[],int start,vector<bool>&visited)
{
    visited[start]=true;
    cout<<start<<" ";
    for(int i=0;i<g[start].size();i++)
    {
        int neigh=g[start][i];
        if(visited[neigh]==false)
        {
            DFS(g,neigh,visited);
        }
    }
}

int main()
{
    cout<<"Node and edge : ";
    int n,e,m;
    cin>>n>>e;
    vector<int>graph[n+1];
    for(int i=0;i<e;i++)
    {
        int a,b;
        cin>>a>>b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    cout<<"Start node : ";
    cin>>m;
    vector<bool>visited(n+1,false);
    DFS(graph,m,visited);
}

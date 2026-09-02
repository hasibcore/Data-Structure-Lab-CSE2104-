#include<bits/stdc++.h>
using namespace std;
void DFS(vector<int>v[],int start,vector<bool>&visited)
{
    cout<<start<<" ";
    visited[start]=true;
    for(int i=0;i<v[start].size();i++)
    {
        int neigh=v[start][i];
        if(visited[neigh]==false)
        {
            DFS(v,neigh,visited);
        }
    }
}
int main()
{
    cout<<"Enter node and edge : ";
    int n,e,m;
    cin>>n>>e;
    vector<int>g[n+1];
    for(int i=0;i<e;i++)
    {
        int a,b;
        cin>>a>>b;
        g[a].push_back(b);
        g[b].push_back(a);
    }
    vector<bool>visited(n+1,false);
    cout<<"Enter start node : ";
    cin>>m;
    DFS(g,m,visited);

}

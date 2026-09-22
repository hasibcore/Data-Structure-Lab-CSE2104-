#include<bits/stdc++.h>
using namespace std;

void DFS(vector<int>graph[],int start,int n)
{
    stack<int>s;
    vector<bool>marked(n+1,false);
    s.push(start);
    marked[start]=true;
    while(!s.empty())
    {
        int e=s.top();
        s.pop();
        cout<<e<<" ";
        for(int i=0;i<graph[e].size();i++)
        {
         int ngh=graph[e][i];
         if(marked[ngh]==false)
         {

             marked[ngh]=true;
             s.push(ngh);
         }
        }
    }
}

int main()
{
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
    cin>>m;
    DFS(g,m,n);
}

#include<bits/stdc++.h>
using namespace std;

void DFS(vector<int>g[],int st,vector<bool>&marked)
{
    stack<int>s;

    marked[st]=true;
    s.push(st);
    while(!s.empty())
    {
        int e=s.top();
        cout<<e<<" ";
        s.pop();
       for(int i=0;i<g[e].size();i++)
      {
         int ng=g[e][i];
         if(marked[ng]==false)
         {
            s.push(ng);
            marked[ng]=true;

         }
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
     if(marked[i]==false)
     {
      DFS(graph,i,marked);
     }
    }
}

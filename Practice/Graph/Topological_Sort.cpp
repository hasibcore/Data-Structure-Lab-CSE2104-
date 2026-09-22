#include<bits/stdc++.h>
using namespace std;
stack<int>s;
void DFS(vector<int>g[],int st,vector<bool>&marked)
{


    //cout<<st<<" ";
    marked[st]=true;

    for(int i=0;i<g[st].size();i++)
    {
        int ng=g[st][i];
        if(marked[ng]==false)
        {
            DFS(g,ng,marked);
        }

    }

    s.push(st);
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
       // graph[b].push_back(a);

    }
    for(int i=0;i<n;i++)
    {
     if(marked[i]==false)
     {
      DFS(graph,i,marked);
     }
    }
    while(!s.empty())
    {
       cout<<s.top()<<" ";
       s.pop();
    }

}

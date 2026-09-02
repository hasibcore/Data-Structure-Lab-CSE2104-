#include<bits/stdc++.h>
using namespace std;
void BFS(vector<int>g[],int start,int n)
{
    queue<int>q;
    vector<bool>visit(n+1,false);
    q.push(start);
    visit[start]=true;
     while(!q.empty())
     {
         int e=q.front();

            cout<<q.front()<<" ";
         q.pop();



         for(int i=0;i<g[e].size();i++)
         {

             int v=g[e][i];
             if(visit[v]==false)
             {
                 visit[v]=true;
                 q.push(v);
             }
         }
     }
}
int main()
{
    int n,e,m;
    cout<<"node and edge : ";
    cin>>n>>e;

    vector<int>v[n+1];
    for(int i=0;i<e;i++)
    {
        int a,b;
        cin>>a>>b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    int s;
    cout<<"start : ";
    cin>>s;
    BFS(v,s,n);
}

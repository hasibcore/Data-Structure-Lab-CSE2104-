#include<bits/stdc++.h>
using namespace std;
queue<int>q;
int cycle;
bool DFS(vector<int>g[],int start,int parent,vector<bool>&visited)
{

    visited[start]=true;
    for(int i=0;i<g[start].size();i++)
    {
        int ngh=g[start][i];
        if(visited[ngh]==false)
        {

            if(DFS(g,ngh,start,visited)==true )
            {

                q.push(start);
                return true;
            }
        }
        else if(visited[ngh]==true && parent!=ngh)
        {
            cycle=ngh;
            q.push(start);
            return true;
        }
    }
    return false;
}
 int main()
 {
     int n,e;
     bool l=false;
     cin>>n>>e;
     vector<int>g[n+1];
     vector<bool>visited(n+1,false);

     for(int i=0;i<e;i++)
     {
         int a,b;
         cin>>a>>b;
         g[a].push_back(b);
         g[b].push_back(a);
     }
     for(int i=0;i<n;i++)
     {
         if(visited[i]==false)
         {
            bool m= DFS(g,i,-1,visited);

            if(m==true){
                cout<<"cycle detected ";
                l=true;
                break; //optional
            }
         }
     }
     cout<<endl;
     if(l==true){
     do
     {
         int f=q.front();
         q.pop();
         cout<<f<<" ";

     }
     while(!q.empty() && q.front()!=cycle);
     return 0;
     }
     else
     {
    cout<<"Cycle not detected";
     }
 }

#include<bits/stdc++.h>
using namespace std;

// Cycle detection using Floyd's Tortoise and Hare approach
void HT(vector<int>g[], int n)
{
    int fast = -1, slow = -1;
    // Implementation placeholder for functional graph / single successor graph
    if(n >= 1 && !g[1].empty())
    {
        slow = 1;
        fast = 1;
    }
}

int main()
{
    int n, e;
    cin >> n >> e;
    vector<int> g[n+1];
    for(int i = 0; i < e; i++)
    {
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }
    HT(g, n);
    return 0;
}

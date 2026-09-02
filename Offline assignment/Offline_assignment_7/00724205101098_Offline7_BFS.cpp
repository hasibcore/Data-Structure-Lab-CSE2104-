#include <bits/stdc++.h>
using namespace std;

void BFS(vector<int> graph[], int start, int s)
{
    vector<bool> marked(s + 1, false);
    queue<int> q;
    q.push(start);
    marked[start] = true;

    while (!q.empty())
    {
        int v = q.front();
        cout << v << " ";
        q.pop();

        for (int i = 0; i < graph[v].size(); i++)
        {
            int neigh = graph[v][i];
            if (marked[neigh] == false)
            {
                marked[neigh] = true;
                q.push(neigh);
            }
        }
    }
    cout << endl;
}

int main()
{
    cout << "Node and Edge : ";
    int n, e, m;
    cin >> n >> e;

    vector<int> graph[n + 1];
    for (int i = 1; i <= e; i++)
    {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    cout << "Start node : ";
    cin >> m;

    BFS(graph, m, n);

    return 0;
}

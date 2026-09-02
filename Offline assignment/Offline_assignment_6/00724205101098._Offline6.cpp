#include<bits/stdc++.h>
using namespace std;

stack<char> st;
stack<int> it;

int piority(char c)
{
    if(c == '^') return 3;
    else if(c == '*' || c == '/') return 2;
    else if(c == '+' || c == '-') return 1;
    else return -1;
}

string infixToPostfix(string s)
{
    string postfix = "";

    for(int i = 0; i < s.length(); i++)
    {
        if(s[i] >= '0' && s[i] <= '9')
        {
            while(i < s.length() && s[i] >= '0' && s[i] <= '9')
            {
                postfix += s[i];
                i++;
            }

            postfix += ' ';
            i--;
        }

        else if(s[i] == '(')
        {
            st.push(s[i]);
        }

        else if(s[i] == ')')
        {
            while(!st.empty() && st.top() != '(')
            {
                postfix += st.top();
                postfix += ' ';
                st.pop();
            }

            if(!st.empty())
                st.pop();
        }

        else
        {
            while(!st.empty() &&
                  st.top() != '(' &&
                  piority(s[i]) <= piority(st.top()))
            {
                postfix += st.top();
                postfix += ' ';
                st.pop();
            }

            st.push(s[i]);
        }
    }

    while(!st.empty())
    {
        postfix += st.top();
        postfix += ' ';
        st.pop();
    }

    return postfix;
}

int evaluation(string post)
{
    for(int i = 0; i < post.size(); i++)
    {
        if(post[i] >= '0' && post[i] <= '9')
        {
            int n = 0;

            while(i < post.size() &&
                  post[i] >= '0' && post[i] <= '9')
            {
                n = n * 10 + (post[i] - '0');
                i++;
            }

            it.push(n);
            i--;
        }

        else if(post[i] == '+')
        {
            int a = it.top();
            it.pop();

            int b = it.top();
            it.pop();

            it.push(b + a);
        }

        else if(post[i] == '-')
        {
            int a = it.top();
            it.pop();

            int b = it.top();
            it.pop();

            it.push(b - a);
        }

        else if(post[i] == '*')
        {
            int a = it.top();
            it.pop();

            int b = it.top();
            it.pop();

            it.push(b * a);
        }

        else if(post[i] == '/')
        {
            int a = it.top();
            it.pop();

            int b = it.top();
            it.pop();

            it.push(b / a);
        }
    }

    return it.top();
}

int main()
{
    cout << "Enter the infix expression: ";

    string s;
    cin >> s;

    string postfix = infixToPostfix(s);

    cout << "Postfix expression: " << postfix << endl;

    int ev = evaluation(postfix);

    cout << "Evaluation result : " << ev;

    return 0;
}

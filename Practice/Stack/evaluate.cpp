#include<bits/stdc++.h>
using namespace std;
stack<int>st;
void ev(string s)
{
    for(int i=0;i<s.length();i++)
    {
        char c=s[i];
        if(s[i]>='0' && s[i]<='9')
        {

            st.push(c-'0');
        }
        else if(c=='+')
        {
            int a=st.top();
            st.pop();
            int b=st.top();
            st.pop();
            st.push(b+a);
        }
        else if(c=='-')
        {
            int a=st.top();
            st.pop();
            int b=st.top();
            st.pop();
            st.push(b-a);
        }
         else if(c=='*')
        {
            int a=st.top();
            st.pop();
            int b=st.top();
            st.pop();
            st.push(b*a);
        }
         else
        {
            int a=st.top();
            st.pop();
            int b=st.top();
            st.pop();
            st.push(b/a);
        }
    }
    cout<<endl;
    cout<<st.top();
}
int main()
{
    string s="234*+";
    ev(s);
}

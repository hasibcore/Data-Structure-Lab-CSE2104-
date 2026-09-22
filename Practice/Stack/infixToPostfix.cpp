#include<bits/stdc++.h>
using namespace std;
stack<char>st;
int pri(char x)
{
    if(x=='+' || x=='-') return 1;
    if(x=='*' || x=='/') return 2;
    if(x=='^') return 3;
  //  if(x=='(') return 4;

  return 0;
}
  void infixToPostfix(string s)
  {
      cout<<endl;

      for(int i=0;i<s.length();i++){
        if(s[i]>='0' && s[i]<='9')
           {

            while(s.length()>i && s[i]>='0' && s[i]<='9')
           {
            cout<<s[i];
            i++;
           }
           cout<<" ";
           i--;
        }
        else if(s[i]=='(')
            {
                st.push(s[i]);
            }
          else if(s[i]==')')
          {
              while(!st.empty() && st.top()!='(')
              {
                  cout<<st.top()<<" ";
                  st.pop();
              }
              st.pop();
          }
        else{

            int p=pri(s[i]);



                while(!st.empty() && st.top()!='(' && p<=pri(st.top()))
                {
                    cout<<st.top()<<" ";
                    st.pop();

                }
                st.push(s[i]);

             }


        }

        while(!st.empty())
         {
           cout<<st.top()<<" ";
           st.pop();
         }

      }

 int main()
 {
     string s;
      getline(cin,s);
     infixToPostfix(s);

 }
//    (1+2)-(3*1)

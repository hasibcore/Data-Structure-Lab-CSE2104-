#include<iostream>
using namespace std;
int main()
{
  int n,z,m=0;
  cin>>n;
  while(n!=0)
  {
       z=n%10;
      n=n/10;
      if(z%2==0)
      {
          m++;
      }
  }
  cout<<m;
}

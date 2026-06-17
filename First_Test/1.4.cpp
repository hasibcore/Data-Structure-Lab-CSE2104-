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
      z=m*10+z;
      m=z;
  }
  cout<<m;

 }

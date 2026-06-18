#include<iostream>
using namespace std;
void calculated(int n)
{

   int mul=1,z;
   while(n!=0){
    z=n%10;

    mul=mul*z;
    n=n/10;

   }
    cout<<mul;
}
int main()
{
    int n;
    cin>>n;
   calculated(n);

}

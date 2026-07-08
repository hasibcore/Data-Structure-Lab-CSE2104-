#include<bits/stdc++.h>
using namespace std;
struct Book
{
    string bName;
    string author;
    int y;
};

void selectionSort(vector<Book> &b, int n)
{
    for(int i=0;i<n-1;i++)
{
    int max=i;
    for(int j=i+1;j<n;j++)
    {
        if(b[j].y==b[max].y)
        {
            if(b[j].author<b[max].author)
            {
                max=j;
            }
            else if(b[j].author==b[max].author)
           {
             if(b[j].bName<b[max].bName)
            {
                max=j;
            }
           }
            
        }
       else if(b[j].y>b[max].y)
        {
            max=j;
         }
      
    }
    swap(b[i],b[max]);
}
}
int main()
{
 int n;
 cin>>n;
 cin.ignore();
 vector<Book> b(n);
 for(int i=0;i<n;i++)
 {
    string line;
getline(cin, line);

stringstream ss(line);

getline(ss, b[i].bName, ',');
getline(ss, b[i].author, ',');

if (b[i].author[0] == ' '){
    b[i].author.erase(0, 1);
 }
ss >> b[i].y;
    
 }
 selectionSort(b,n);
  for(int i=0;i<n;i++)
  {
    cout << b[i].bName << ", "
     << b[i].author << ", "
     << b[i].y << endl;
  
  }
}

#include<bits/stdc++.h>
using namespace std;
struct Node
{
    int data;
    Node* next;
};
Node* head=NULL;
void addLast(int data)
{
    Node *k=head;
    Node *newn=new Node();
 if(head==NULL)
 {
   head=newn;
   newn->data=data;
   newn->next=NULL;
   return;
 }
newn->data=data;
newn->next=NULL;
while(k->next!=NULL)
{
    k=k->next;
}
k->next=newn;

}
void print()
{
    Node *k=head;
    while(k!=NULL)
    {
        cout<<k->data<<" ";
        k=k->next;
    }
}
void Sort()
{
    Node *i=head;
    Node* tmp=head;
    while(i!=NULL)
    {
        Node *j=i->next;
        tmp=i;
        while(j!=NULL)
        {
            if(tmp->data>j->data)
            {
             tmp=j;
            }
        j=j->next;
        }
       swap(tmp->data,i->data);
        i=i->next;
    }

}
int main()
{
int n;
cin>>n;
for(int i=0;i<n;i++)
{
    int x;
    cin>>x;
    addLast(x);

}
Sort();
print();
}

#include<bits/stdc++.h>
using namespace std;
 struct node
 {
   int data;
   node* next;
 };
 node *head=NULL;
 void lastInsert(int x)
 {
     node *newnode,*t=head;
     newnode=(node*)malloc(sizeof(node));
     newnode->data=x;
     newnode->next=NULL;
     if(head==NULL){
        head=newnode;
        return;
     }

     while(t->next!=NULL)
     {
         t=t->next;
     }
     newnode->next=NULL;
     t->next=newnode;
 }
 void display()
{

     node *ghost;
    ghost=head;
    while(ghost!=NULL)
    {
        cout<<ghost->data<<endl;
        ghost=ghost->next;
    }

}
 void reverselist()
 {
    node* prev=NULL;
    node* current=head;
    node* next=NULL;
    while(current!=NULL)
    {
        next=current->next;
        current->next=prev;
        prev=current;
        current=next;

    }
    head=prev;
 }
int main()
{
    int i,x,n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>x;
        lastInsert(x);

    }
    reverselist();
    display();
}

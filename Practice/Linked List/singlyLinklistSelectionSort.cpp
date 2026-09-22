#include<bits/stdc++.h>
using namespace std;

struct node{
int data;
node* next;
};
node* head=NULL;
void last(int d)
{
    node* newn=(node*)malloc(sizeof(node));
    newn->data=d;
    newn->next=NULL;
    if(head==NULL)
    {
       head=newn;
       return ;
    }
    node* k=head;
    while(k->next!=NULL)
    {
        k=k->next;
    }
    k=k->next;
}
void print()
{
    node* k=head;
    while(k!=NULL)
    {
        cout<<k->data<<" ";
        k=k->next;
    }
}
void selection()
{

    node* k1=head,*tmp=head;
    while(k1->next!=NULL)
    {

        node *k2=k1->next;
       node* in=k1;
        while(k2!=NULL)
        {
            if(k2->data<in->data)
            {
               in=k2;
            }
            k2=k2->next;
        }
         swap(k1->data,in->data);
        k1=k1->next;
    }

}
int main()
{

    last(4);
    last(2);
    last(9);
    last(3);
    last(5);
    cout<<"before : ";
    print();
    cout<<endl;
    cout<<"after : ";
    selection();
    print();
}

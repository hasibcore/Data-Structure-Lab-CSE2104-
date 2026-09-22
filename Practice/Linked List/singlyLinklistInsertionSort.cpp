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
       return;
    }
    node* k=head;
    while(k->next!=NULL)
    {
        k=k->next;
    }
    k->next=newn;
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

void insertionSort()
{
    if(head == NULL || head->next == NULL) return;

    node* sorted = NULL;
    node* curr = head;

    while(curr != NULL)
    {
        node* nextNode = curr->next;
        if(sorted == NULL || sorted->data >= curr->data)
        {
            curr->next = sorted;
            sorted = curr;
        }
        else
        {
            node* temp = sorted;
            while(temp->next != NULL && temp->next->data < curr->data)
            {
                temp = temp->next;
            }
            curr->next = temp->next;
            temp->next = curr;
        }
        curr = nextNode;
    }
    head = sorted;
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
    insertionSort();
    print();
    return 0;
}

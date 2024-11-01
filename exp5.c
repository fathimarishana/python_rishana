#include <stdio.h>
#include <stdlib.h>
struct node{
     int data;
     struct node*next;
};
void insert_at_first(struct node**head,int new_data){
     struct node*new_node=malloc(sizeof(struct node));
     new_node->next=NULL;
     new_node->data=new_data;
     if(head==NULL){
          *head=new_node;
         return;
    }
     else{
        new_node->next=*head;
        *head=new_node;
       return;
     }
}
void insert_at_end(struct node**head,int new_data){
     struct node*new_node=malloc(sizeof(struct node));
     new_node->next=NULL;
     new_node->data=new_data;
     struct node*last=*head;
     while(last->next!=NULL){
          last=last->next;
     }
     last->next=new_node;
     return;
     }
void insert_at_pos(struct node**head,int pos,int new_data){
     struct node*new_node=malloc(sizeof(struct node));
     new_node->next=NULL;
     new_node->data=new_data;
     struct node*last=*head;
     int i=1;
     while(i<pos-1){
         last=last->next;
         i++;
     }
     new_node->next=last->next;
     last->next=new_node;
     return;
     }
void delete_begin(struct node**head){
    struct node*temp=*head;
    *head=(*head)->next;
    free(temp);
}
void delete_last(struct node**head){
    struct node*last=*head;
    struct node*temp=*head;
    while(last->next->next!=NULL){
          last=last->next;
   }
free(last->next);
    last->next=NULL;
}
void delete_pos(struct node**head,int pos){
    int i=1;
    struct node*last=*head;
    while(i<pos-1){
       last=last->next;
       i++;
}
    struct node*del=last->next;
    last->next=last->next->next;
    free(del);
}
void search(struct node**head,int search){
    int i=1;
    struct node*last=*head;
    while(last->next!=NULL){
                                       if(last->data==search)
           {
            printf("elements found %d at %d position\n",search,i);
            break;
           }
         last=last->next;
         i++;
    }
    if(last->next==NULL&&last->data!=search){
       printf("element not found\n");}
}
void printlist(struct node*nod)
{
 while(nod!=NULL)
 {
  printf("%d",nod->data);
  nod=nod->next;
 }
printf("\n");
}
void main(){
struct node*head=NULL;
int new_data,choice;
while(choice!=-1){
printf("1.insert at beggining\n2.insert at last\n3.insert at position\n4.delete at beggining\n5.delele at last\n6.delete at position\n7.search\n-1.exit\n enter the choice:");
scanf("%d",&choice);
switch(choice){
case 1:printf("enter the data to insert:");
scanf("%d",&new_data);
insert_at_first(&head,new_data);
printf("the updated linked list is:\n");
printlist(head);
break;
case 2:printf("enter the data to insert:");
scanf("%d",&new_data);
insert_at_end(&head,new_data);
printf("the updated linked list is:\n");
printlist(head);
break;
case 3:printf("enter the data to insert:");
scanf("%d",&new_data);
int pos;
printf("enter the position");
scanf("%d",&pos);
insert_at_pos(&head,pos,new_data);
printf("the updated linked list is:\n");
printlist(head);
break;
case 4:delete_begin(&head);
printf("the updated linked list is:\n");
printlist(head);
break;
case 5:delete_last(&head);
printf("the updated linked list is:\n");
printlist(head);
break;
case 6:printf("enter the position:");
scanf("%d",&pos);
if(pos==1)
{
delete_begin(&head);
}
else
delete_pos(&head,pos);
printf("the updated linked list is:\n");
printlist(head);
break;
case 7:printf("enter the number to search:");
int s;
scanf("%d",&s);
search(&head,s);
break;
default:printf("exiting\n");
break;
}}}


/*PROBLEM STATEMENT: Department of Computer Engineering has student's club named 
'pinnacle club’. Students of second, third and final year of department can be granted 
membership on request. Similarly on may cancel the membership of club .First node is reserved 
for the president of the club and last node is reserved for the secretary of club .write C++ 
program to maintain club members information using singly linked list .store student PRN and 
Name .Write function to:
a) Add and Delete the members as well as the president or even secretary.
b) Compute total numbers of members of club.
c) Display members.
d) Display list in reverse order using recursion.
e) Two linked lists exists for two divisions .Concatenate two lists.

Name: Diya Rade
Class: SE Comp 2
Batch: R
Clg PRN: F24122005
Seat no: */
#include<iostream>
#include<string>
using namespace std;
struct node{
	int prn;
	string name;
	node *next;
};
class list{
	node *temp,*head;
	public:
		list(){
			head=NULL;
		}
		node *create(int val,string n);
		void insertbeg();
		void insertend();
		void insertat(int);
		void deleteat(int);
		void display();
		void reverse();
		int count();
		void rev(node *);
		void concatenate(list,list);
		void op();
};
node* list::create(int val,string n){
	temp=new (struct node);
	temp->prn=val;
	temp->name=n;
	temp->next=NULL;
	return temp;
}
void list::insertend(){
	int val;
	string n;
	node* t=head;
	cout<<"\nEnter prn: ";
	cin>>val;
	cout<<"\nEnter name: ";
	cin>>n;
	temp=create(val,n);
	if(head==NULL){
		head=temp;
		head->next=NULL;
	}
	else{
		while(t->next!=NULL){
			t=t->next;
		}
		t->next=temp;
		temp->next=NULL;
		cout<<"\nSceretary inserted";
	}
}
void list::insertat(int i){
	int val,pos=i-1,c=1;
	string n;
	node *ptr;
	node* t=head;
	while(t->next!=NULL){
		t=t->next;
		c++;
	}
	if(i==1){
		insertbeg();
	}
	else if(pos>c||i<=0){
		cout<<"\nInvalid position";
	}
	else{
		cout<<"\nEnter prn: ";
		cin>>val;
		cout<<"\nEnter name: ";
		cin>>n;
		temp=create(val,n);
		while(pos--){
			ptr=t;
			t=t->next;
		}
		temp->next=t;
		ptr->next=temp;
		cout<<"\nMember inserted";
	}
}
void list::insertbeg(){
	int val;
	string n;
	cout<<"\nEnter prn: ";
	cin>>val;
	cout<<"\nEnter name: ";
	cin>>n;
	temp=create(val,n);
	if(head==NULL){
		head=temp;
		head->next=NULL;
		return;
	}
	else{
		temp->next=head;
		head=temp;
	}
	cout<<"\nPresident inserted";
}
void list::deleteat(int i){
		int val,pos=i-1,c=1;
	string n;
	node *ptr1,*ptrr;
	node* t=head;
	while(t->next!=NULL){
		t=t->next;
		c++;
	}
	if(i==1){
		ptr1=head;
		head=head->next;
		delete ptr1;
	}
	else if(pos>c||i<=0){
		cout<<"\nInvalid position";
	}
	else{
		while(pos--){
			ptr1=t;
			t=t->next;
			ptrr=t->next;
		}
		ptr1->next=ptrr;
		delete t;
		cout<<"\n member deleted at position: "<<i;
	}
}
void list::display(){
	temp=head;
	cout<<"\nPresident:";
	cout<<temp->prn<<"-->"<<temp->name;
	if(temp->next!=NULL){
		temp=temp->next;
	}
	while(temp->next!=NULL){
		cout<<temp->prn<<"-->"<<temp->name;
		temp=temp->next;
	}
	cout<<"\nSecretary:";
	cout<<temp->prn<<"-->"<<temp->name<<"->";
	cout<<"null";	
}
int list::count(){
	node *t=head;
	int c=0;
	while(t!=NULL){
		c++;
		t=t->next;
	}
	return c;
}
void list::concatenate(list a, list b){
	node *last,*last1;
	node *t=a.head;
	while(t!=NULL){
		int val=t->prn;
		string n=t->name;
		temp=create(val,n);
		if(head==NULL){
			head=temp;
			head->next=NULL;
			last=head;
		}
		else{
			last->next=t;
			last=t;
		}
		t=t->next;
	}
	last->next=b.head;
	t=b.head;
	while(t!=NULL){
		int val=t->prn;
		string n=t->name;
		temp=create(val,n);
		last->next=temp;
		last=temp;
		t=t->next;
	}
	last->next=NULL;
}
void list::rev(node *t){
	if(t->next!=NULL){
		rev(t->next);
	}
	if(t==head){
		cout<<"\nSecretary:"<<t->prn<<"-->"<<t->name;
	}
	else if(t->next==NULL){
		cout<<"\nPresident:"<<t->prn<<"-->"<<t->name;
	}
	else{
		cout<<"\nMember"<<t->prn<<"-->"<<t->name;
	}
}
void list::reverse(){
	rev(head);
}
void list::op(){
	int ch;
	while(true){
		cout<<"\n1.Add \n2.Delete \n3.Member count \n4.Display \n5.Reverse \n0.prev menu";
		cout<<"\nEnter choice: ";
		cin>>ch;
		switch(ch){
			case 1:{
				int c;
				cout<<"\n1Add president \n2.Add member \n3.Add secretary";
				cout<<"\nEnter choice: ";
				cin>>c;
				switch(c){
					case 1:{
						insertbeg();
						break;
					}
					case 2:{
						insertat(2);
						break;
					}
					case 3:{
						insertend();
						break;
					}
				}
				break;
			}
			case 2:{
				cout<<"\n1Delete president \n2.Delete member \n3.Delete secretary";
				cout<<"\nEnter choice: ";
				int c;
				cin>>c;
				switch(c){
					case 1:{
						deleteat(1);
						break;
					}
					case 2:{
						cout<<"\nEnter position: ";
						int j;
						deleteat(j);
						break;
					}
					case 3:{
						deleteat(count());
						break;
					}
				}
				break;
			}
			case 3:{
				cout<<"\nMember count: "<<count();
				break;
			}
			case 4:{
				if(head==NULL){
					cout<<"\nEmpty";
					return;
				}
				else{
					display();
					break;
				}
			}
			case 5:{
				reverse();
				break;
			}
			case 0:{
				
				return;
			}
		}
	}
}
int main(){
	list l,x,y;
	int ch;
	while(true){
		cout<<"\n1.List A \n2.List B \n3.Concatenate \n4.Exit";
		cout<<"\nEnter choice: ";
		cin>>ch;
		switch(ch){
			case 1:{
				x.op();
				break;
			}
			case 2:{
				y.op();
				break;
			}
			case 3:{
				l.concatenate(x,y);
				l.display();
				break;
			}
			case 4:{
				cout<<"\nExiting...";
				return 0;
				break;
			}
		}
	}
}

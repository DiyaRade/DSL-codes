/*PROBLEM STATEMENT: Second year Computer Engineering class, set A of students like 
Vanilla ice-cream and set B of students like Butterscotch ice-cream. Write C++ program to 
store two sets using Linked List. Compute and displayi. Set of students who like both vanilla and butterscotch
ii. Set of students who like either vanilla or butterscotch or not both
iii. Number of students who like neither vanilla nor butterscotch

Name: Diya Rade
Class: SE Comp 2
Batch: R
Clg PRN: F24122005
Seat no: */
#include<iostream>
using namespace std;
struct node{
	int data;
	node *next;
};

class link{
	node *head;
	public:
		link(){
			head=nullptr;
		}
		node insert(int val){
			node *newnode=new node();
			newnode->data=val;
			newnode->next=head;
			head=newnode;
		}
		bool contains(int val){
			node *temp=head;
			while(temp!=nullptr){
				if(temp->data==val) return true;
				temp=temp->next;
			}
			return false;
		}
		void display(){
			node *temp=head;
			while(temp!=nullptr){
				cout<<temp->data<<"\t";
				temp=temp->next;
			}
			cout<<endl;
		}
		link intersection(link &other){
			link res;
			node *temp=head;
			while(temp!=nullptr){
				if(other.contains(temp->data)){
					res.insert(temp->data);
				}
				temp=temp->next;
			}
			return res;
		}
		link uni(link &other){
			link res;
			node *temp=head;
			while(temp!=nullptr){
				res.insert(temp->data);
				temp=temp->next;
			}
			temp=other.head;
			while(temp!=nullptr){
				if(!contains(temp->data)){
					res.insert(temp->data);
				}
				temp=temp->next;	
			}
			return res;
		}
		link diff(link &other){
			link res;
			node *temp=head;
			while(temp!=nullptr){
				if(!other.contains(temp->data)){
					res.insert(temp->data);
				}
				temp=temp->next;
			}
			temp=other.head;
			while(temp!=nullptr){
				if(!contains(temp->data)){
					res.insert(temp->data);
				}
				temp=temp->next;
			}
			return res;
		}
		int count(){
			node *temp=head;
			int c=0;
			while(temp!=nullptr){
				c++;
				temp=temp->next;
			}
			return c;
		}
};

int main(){
	link v,b;
	int total,id,ch;
	
	cout<<"\nEnter total number of students: ";
	cin>>total;
	
	cout<<"\nEnter number of student who like vanilla: ";
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		cout<<"\nEnter student id: ";
		cin>>id;
		v.insert(id);
	}
	
		cout<<"\nEnter number of student who like butterscotch: ";
	int m;
	cin>>m;
	for(int i=0;i<m;i++){
		cout<<"\nEnter student id: ";
		cin>>id;
		b.insert(id);
	}
	
	while(true){
		cout<<"\n1. student who like both vanilla and butterscotch \n2. student who like either vanilla or butterscotch but not both \n3. number of student who neither like vanilaa nor butterscotch \n4. exit \n";
		cout<<"\nEnter choice";
		cin>>ch;
		switch(ch){
			case 1:{
				link l3=v.intersection(b);
				cout<<"\nstudent who like both vanilla and butterscotch ";
				l3.display();
				break;
			}
			case 2:{
				link l3=v.diff(b);
				cout<<"\nstudent who like either vanilla or butterscotch but not both ";
				l3.display();
				break;
		    }
		    case 3:{
		    	link uni=v.uni(b);
		    	int nn=total-uni.count();
		    	cout<<"\nnumber of student who neither like vanilaa nor butterscotch "<<nn;
				break;
			}
			case 4:{
				cout<<"exiting....";
				break;
			}
				
		}
	}
}

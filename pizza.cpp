/*PROBLEM STATEMENT: Pizza parlor accepting maximum M orders. Orders are 
served in first come first served basis. Order once placed cannot be cancelled. Write C++ 
program to simulate the system using circular queue using array.

Name: Diya Rade
Class: SE Comp 2
Batch: R
Clg PRN: F24122005
Seat no: */
#include<iostream>
using namespace std;
#define size 5
class Pizza{
	int porder[size];
	int front,rear;
	
	public:
		Pizza(){
			front=rear=-1;
		}
		bool qfull(){
			return front==(rear+1)%size;
		}
		bool qempty(){
			return front==-1;
		}
		void accept(int item){
			if(qfull()){
				cout<<"\nSorrry! no more orders";
				return;				
			}
			else{
				if(front==-1){
					front=rear=0;
				}
				else{
					rear=(rear+1)%size;
				}
			porder[rear]=item;
			cout<<"\nOrder placed successfully";
			}
		}
		void payment(int n){
			int item;
			if(qempty()){
				cout<<"No pending order";
				return;
			}
			else{
				cout<<"\nDelivered orders as follows";
				for(int i=0;i<n;i++){
					item=porder[front];
					if(front==rear){
						front=rear=-1;
					}
					else{
						front=(front+1)%size;
					}
					cout<<"\t"<<item;
				}
	
			cout<<"\n Total amount to be paid: "<<n*100;
			cout<<"\nThanks visit again";
		    }
		}
		void display(){
			if(qempty()){
				cout<<"\n No pending orders";
				return;
			}
			int i=front;
			while(i!=rear){
				cout<<porder[i]<<"\t";
				i=(i+1)%size;
			}
			cout<<porder[rear]<<"\n";
		}
};
int main(){
	Pizza p;
	int ch,n,k;
	while(true){
		cout<<"\n1. Accept \n2. Payment \n3. Pending orders \n4. Exit ";
		cout<<"\nEnter choice";
		cin>>ch;
		switch(ch){
			case 1:{
				cout<<"\nWhich pizza would you like to order?";
				cout<<"\n1. Veg soya pizza \n2. Veg butter pizza \n3. egg pizza";
				cout<<"\nEnter order";
				cin>>k;
				p.accept(k);
				break;
			}
			case 2:{
				cout<<"\nhow many pizza?";
				cin>>n;
				p.payment(n);
				break;
			}
			case 3:{
				cout<<"\nPending orders: ";
				p.display();
				break;
			}
			case 4:{
				cout<<"Exiting.... ";
				return 0;
			}
		}
	}
}

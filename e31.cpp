/*PROBLEM STATEMENT: A double-ended queue (deque) is a linear list in which 
additions and deletions may be made at either end. Obtain a data representation mapping a 
deque into a one- dimensional array. Write C++ program to simulate deque with functions to 
add and delete elements from either end of the deque.

Name: Diya Rade
Class: SE Comp 2
Batch: R
Clg PRN: F24122005
Seat no: */
#include<iostream>
using namespace std;
class Dque{
	int *arr;
	int front;
	int rear;
	int capacity;
	int size;
	public:
		Dque(int cap){
			capacity=cap;
			arr=new int[cap];
			front=-1;
			rear=-1;
			size=0;
		}
		bool qfull(){
			return size==capacity;
		}
		bool qempty(){
			return size==0;
		}
		void addfront(int val){
			if(qfull()){
				cout<<"\nNo more elements ";
				return;
			}
			if(qempty()){
				front=rear=0;
			}
			else{
				front=(front-1+capacity)%capacity;
			}
			arr[front]=val;
			size++;
			cout<<"\nValue added successfully";
		}
		void addrear(int val){
			if(qfull()){
				cout<<"\n No more elements";
				return;
			}
			if(qempty()){
				front=rear=0;
			}
			else{
				rear=(rear+1)%capacity;
			}
			arr[rear]=val;
			size++;
		}
		void deletefront(){
			if(qempty()){
				cout<<"\n No elements to delete";
				return;
			}
			cout<<"\nElement deleted from front: "<<arr[front];
			if(qempty()){
				front=rear=-1;
			}
			else{
				front=(front+1)%capacity;
			}
			size--;
		}
		void deleterear(){
			if(qempty()){
				cout<<"\nNo elements to delete";
				return;
			}
			cout<<"\nElement deleted from rear: "<<arr[rear];
			if(qempty()){
				front=rear=-1;
			}
			else{
				rear=(rear-1+capacity)%capacity;
			}
			size--;
		}
		void display(){
			if(qempty()){
				cout<<"\n No elements to display";
				return;
			}
			int i=front;
			while(i!=rear){
				cout<<arr[i]<<"\t";
				i=(i+1)%capacity;
			}
			cout<<arr[rear]<<"\n";
		}
};
int main(){
	Dque d(5);
	int ch,val;
	while(true){
		cout<<"\n1. Add front \n2. Add rear \n3. Delete front \n4. Delete rear \n5. Display \n6. Exit";
		cout<<"\nEnter choice: ";
		cin>>ch;
		switch(ch){
			case 1:{
				cout<<"\nEnter value: ";
				cin>>val;
				d.addfront(val);
				break;
			}
			case 2:{
				cout<<"\nEnter value: ";
				cin>>val;
				d.addrear(val);
				break;
			}
			case 3:{
				d.deletefront();
				break;
			}
			case 4:{
				d.deleterear();
				break;
			}
			case 5:{
				d.display();
				break;
			}
			case 6:{
				cout<<"Exiting....";
				break;
			}
		}
	}
}

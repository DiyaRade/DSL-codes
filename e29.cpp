/*PROBLEM STATEMENT: Queues are frequently used in computer programming, and 
a typical example is the creation of a job queue by an operating system. If the operating system 
does not use priorities, then the jobs are processed in the order they enter the system. Write C++ 
program for simulating job queue. Write functions to add job and delete job from queue.

Name: Diya Rade
Class: SE Comp 2
Batch: R
Clg PRN: F24122005
Seat no: */
#include<iostream>
#include<string>
using namespace std;
struct job{
	int id;
	string name;
	job *next;
};
class Jobqueue{
	job *front;
	job *rear;
	public:
		Jobqueue(){
			front=rear=nullptr;
		}
		void add(int id, string name){
			job *newjob=new job;
			newjob->id=id;
			newjob->name=name;
			newjob->next=nullptr;
			if(rear==nullptr){
				front=rear=newjob;
			}
			else{
				rear->next=newjob;
				rear=newjob;
			}
			cout<<"\nJob added successfully";
		
		}
		void delete1(){
			if(front==nullptr){
				cout<<"\nNo jobs to delete";
				return;
			}
			job *temp=front;
			front=front->next;
			if(front==nullptr){
				rear=nullptr;
			}
			cout<<"job deleted successfully";
			delete temp;
		}
		void display(){
			if(front==nullptr){
				cout<<"\nNo jobs to display";
				return;
			}
			job *temp=front;
			while(temp!=nullptr){
				cout<<"\nId: "<<temp->id<<"Name: "<<temp->name;
				temp=temp->next;
			}
		}
		~Jobqueue(){
			while(front!=nullptr){
				delete1();
			}
		}
};
int main(){
	Jobqueue j;
	int id,ch;
	string name;
	while(true){
		cout<<"\n1. Add job \n2. Delete job \n3display job \n4Exit";
		cout<<"\nEnter choice";
		cin>>ch;
		switch(ch){
			case 1:{
				cout<<"\nEnter id and name";
				cin>>id>>name;
				j.add(id,name);
				break;
			}
			case 2:{
				j.delete1();
				break;
			}
			case 3:{
				j.display();
				break;
			}
			case 4:{
				cout<<"Exiting";
				break;
			}
		}
	}
	

}


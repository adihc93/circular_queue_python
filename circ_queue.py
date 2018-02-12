# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 07:41:28 2018
Implementing Circular Queue with class
Queue size allocation can be done at runtime
@author: HP
"""

max_queue=0

class my_queue:
    queue=[]
    front=-1
    rear=-1
    def insert_queue(self):
        if (self.front==0 and self.rear==max_queue-1) or (self.front==self.rear+1):
            print("Overflow")
            return
        else:
            ele=input("Enter element to INSERT: ")
            if self.front==-1 and self.rear==-1:
                self.front=0
                self.rear=0
            elif self.rear==max_queue-1:
                self.rear=0
            else:
                self.rear+=1
            self.queue[self.rear]=ele      
            print("Element ",ele," INSERTED successfully")
            return
    
    def delete_queue(self):
        if self.front==-1:
            print("Underflow")
            return
        else:
            temp=self.queue[self.front]
            if self.front==self.rear:
                self.front=-1
                self.rear=-1
            elif self.front==max_queue-1:
                self.front=0
            else:
                self.front+=1
            print("Element ",temp," DELETED successfully")
            return
    
    def print_queue(self):
        if self.front==-1 and self.rear==-1:
            return "Queue is empty"
        elif self.front<=self.rear:
            que="FRONT->|"
            for x in range(self.front, self.rear+1):
                que+=self.queue[x]+"|"
            que+="<-REAR"
            return que
        else:
            que="FRONT->|"
            for x in range(self.front, max_queue):
                que+=self.queue[x]+"|"
            for x in range(0, self.rear+1):
                que+=self.queue[x]+"|"
            que+="<-REAR"
            return que

qu=my_queue()
print("Welcome to Queue")
size=int(input("Enter size of queue: "))
max_queue=size
for i in range(0, max_queue):
    qu.queue.append(0)
while(True):
    print("0. Exit")
    print("1. INSERT")
    print("2. DELETE")
    print("3. Print Queue")
    choice=input("Enter your Choice: ")
    if choice=='0':
        print("Exiting program...")
        break
    elif choice=='1':
        print("INSERTING element...")
        qu.insert_queue()
        print()
    elif choice=='2':
        print("DELETING element...")
        qu.delete_queue()
        print()
    elif choice=='3':
        print("Printing queue entries...")
        queuing=qu.print_queue()
        print(queuing)
        #print(qu.queue)
        print()
    else:
        print("Invalid entry")
        print()
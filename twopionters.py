class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class linkedlist:
    def __init__(self):                       #constructor
        self.head=None                        #....
    def createLL(self,n):
        i=0
        while i<n:
            val=int(input("enter LL value"))
            new_node=Node(val)
            if self.head==None:
                self.head=new_node
            else:
                t=self.head
                while t.next != None:
                    t=t.next
                t.next=new_node
            i=i+1

    def split(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        second=slow
        prev.next=None

        print("first part")
        show(self.head)
        print("second part")
        show(second)

            
    
    def show(self,head):
        t=head
        sum=0
        t=self.head
        while t:
            print(t.val,end="->")
            sum+=t.val
            t=t.next
        print("\n total sum=",sum)
            

obj=linkedlist()
n=int(input())
obj.createLL(n)
obj.show(obj.head)
obj.split()

            
'''def show(self):
        while head:
            print(head.val)
            head=head.next
'''

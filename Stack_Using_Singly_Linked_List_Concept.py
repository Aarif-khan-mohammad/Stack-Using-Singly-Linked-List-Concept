class Node:
    def __init__(self ,item= None , next=None):
        self.item = item
        self.next = next

class Stack: #LIFO method

    def __init__(self):
        self.start = None
        self.item_count = 0
    
    def is_empty(self):
        return self.start==None
    
    def push(self , data):
        n= Node(data,self.start)
        self.start = n
        self.item_count+=1

    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.start = self.start.next
            self.item_count-=1
            return data
        else:
            raise IndexError("Stack is empty")
        
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is empty")
        
    def size(self):
        return self.item_count
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("top value = " , s1.peek())#top value =  30
print("size of stack = " , s1.size())#size of stack =  3
print("poped value = " , s1.pop())#poped value =  30
print("top value = " , s1.peek())#top value =  20
print("size of stack = " , s1.size())#size of stack =  2


    

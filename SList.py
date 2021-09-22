from SLNode import SLNode

class SList:
    def __init__(self):
        self.head= None
    def add_to_front(self, val):
        new_node = SLNode(val,self.head)
        self.head=new_node
        return self
    def add_to_back(self,val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        while runner.next!= None:
            runner = runner.next
        runner.next = new_node
        return self
    def print_values(self):
        runner = self.head
        while runner!=None:
            print (runner.val)
            runner = runner.next
        return self
    def remove_from_front(self):
        firstNode = self.head
        self.head= firstNode.next
        value = firstNode.val
        del firstNode
        return value
    def remove_from_back(self):
        runner = self.head
        while runner.next!=None:
            prev_node = runner
            runner = runner.next
        value = runner.val
        prev_node.next = None
        del runner
        return value
    def remove_val(self,value):
        prev_node = None
        runner = self.head
        while runner!=None:
            if runner.val == value:
                if prev_node!=None:
                    prev_node.next=runner.next
                else:
                    self.head=runner.next
                del runner
                break
            prev_node = runner 
            runner = runner.next
        return self
    def insert_at(self,value,n):
        if n==0:
            self.add_to_front(value)
            return self
        counter = 1
        newNode = SLNode(value)
        runner = self.head
        while counter < n:
            runner = runner.next
            counter +=1
        newNode.next= runner.next
        runner.next=newNode
        return self

        
        



        
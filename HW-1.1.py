class Node(object):
    def __init__(self,elem):
        self.elem = elem
        self.next = None
class SingleLinkList(object):
    def __init__(self,node=None):
        self.__head = node
        
    def Judge_Empty(self):
        return self.__head == None
        
    def LengthLinkList(self):
        Now = self.__head
        count=0
        while Now != None:
            count = count+1
            Now = Now.next
        return count
        
    def PrintLinkList(self):
        Now = self.__head
        while Now != None:
            print(Now.elem,end=" ")
            Now=Now.next
    def insert(self,position,item):
        if position <= 0:#adding elem at the start of linklist
            node = Node(item)
            node.next = self.__head
            self.__head = node
        elif position > (self.LengthLinkList()-1):
            node = Node(item)
            if self.Judge_Empty():
                self.__head=node
            else:
                Now = self.__head
                while Now.next != None:
                    Now = Now.next
                Now.next = node
        else:
            pre = self.__head
            count = 0
            while count < (position-1):
                count=count+1
                pre=pre.next
                #after leaving from recycle pre points to the position-1
            node = Node(item)
            node.next = pre.next
            pre.next = node
    def Remove(self,item):
        Now = self.__head
        pre = None
        while Now != None:
            if Now.elem == item:
                if Now == self.__head:
                    self.__head = Now.next
                else:
                    pre.next=Now.next
                break
            else:
                pre = Now
                Now = Now.next
    def Adding(self,item):
        node = Node(item)
        a=type(item)
        if self.Judge_Empty():
            self.__head=node
        else:
            Now = self.__head
            while Now.next != None:
                Now = Now.next
            Now.next = node
        print(a)


if __name__== "__main__":
    LinkList1=SingleLinkList()
    
    LinkList1.Adding(1.32)
    LinkList1.Adding(312)
    LinkList1.Adding('sda')
    LinkList1.Adding('dsadsadad')
    LinkList1.Adding(2.6456)
    LinkList1.Adding(445.549)
    LinkList1.Adding('dasda')
    LinkList1.Adding('dada')
    LinkList1.PrintLinkList()
    

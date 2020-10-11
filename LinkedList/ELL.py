#ELL.py
#Created October 10, 2020

class IndexOutOfBoundsError(Exception):
    pass

class llNode:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, iterable=[]):
        dummy = llNode(None, None)
        self.head = dummy
        self.cardinality = 0
        
        traverse = self.head
        
        for element in iterable:
            tempNode = llNode(element)
            
            traverse.link = tempNode
            traverse = traverse.link 
            self.cardinality = self.cardinality + 1
        
    def __str__(self):
        string = ""
        
        traverse = self.head.link
        while traverse != None:
            string = string + str(traverse.data) + ", "
            traverse = traverse.link
        
        return string
    
    def __repr__(self):
        return self.__str__()
    
    def __iter__(self):
        return IterableLinkedList(self.head)
    
    def __len__(self):
        return self.cardinality
    
    def append(self, data):
        tempNode = llNode(data)
        
        traverse = self.head
        
        while traverse.link != None:
            traverse = traverse.link
        
        traverse.link = tempNode
        self.cardinality = self.cardinality + 1
    
    def insertAt(self, index, data):
        if index < 0 or index > (self.cardinality - 1):
            raise IndexOutOfBoundsError
        
        tempNode = llNode(data)
        traverse = self.head
        
        while index > 0:
            traverse = traverse.link
            index = index - 1
        
        tempNode.link = traverse.link
        traverse.link = tempNode
        self.cardinality = self.cardinality + 1
    
    def delete(self, data):
        traverse = self.head 
        
        while traverse.link != None:
            if traverse.link.data == data:
                traverse.link = traverse.link.link
                self.cardinality = self.cardinality - 1
                break
            traverse = traverse.link
    
    def deleteAt(self, index):
        if index < 0 or index > (self.cardinality - 1):
            raise IndexOutOfBoundsError
        
        traverse = self.head
        
        while index > 0:
            traverse = traverse.link
            index = index - 1
        
        datum = traverse.link.data
        traverse.link = traverse.link.link
        self.cardinality = self.cardinality - 1
        return datum

    def merge(self, iterable):
        traverse = self.head
        
        while traverse.link != None:
            traverse = traverse.link
        
        for element in iterable:
            tempNode = llNode(element)
            traverse.link = tempNode
            self.cardinality = self.cardinality + 1
            traverse = traverse.link
    

class IterableLinkedList:
    def __init__(self, head):
        self.head = head
        self.traverse = self.head
    
    def __next__(self):
        self.traverse = self.traverse.link
        if self.traverse == None:
            raise StopIteration
        else:
            return self.traverse.data
    
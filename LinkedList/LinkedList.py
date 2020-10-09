# LinkedList.py
# Created Thursday, October 8, 2020

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
        self.head = None
        traverse = self.head
        
        for element in iterable:
            tempNode = llNode(element)
            if (traverse) == None:
                self.head = tempNode
                traverse = tempNode
            else:
                traverse.link = tempNode
                traverse = traverse.link
                
    def __str__(self):
        returnString = ""
        
        traverse = self.head
        
        while traverse != None:
            returnString = returnString + str(traverse) + ", "
            traverse = traverse.link
            
        return returnString
    
    def append(self, data):
        tempNode = llNode(data)
        traverse = self.head 
        
        if traverse == None:
            self.head = tempNode
            return
        
        while traverse.link != None:
            traverse = traverse.link
        
        traverse.link = tempNode
    
    def insertAt(self, index, data):
        if index < 0:
            raise IndexOutOfBoundsError
        
        tempNode = llNode(data)
        
        if index == 0:
            postChain = self.head
            self.head = tempNode
            self.head.link = postChain
        
        preChain = self.head
        postChain = self.head.link
        while index > 1 and postChain != None:
            preChain = preChain.link
            postChain = postChain.link
            index = index - 1
        
        if index > 1:
            raise IndexOutOfBoundsError
        
        preChain.link = tempNode
        tempNode.link = postChain
    
    def delete(self, data):
        preChain = self.head
        if preChain == None:
            return
        
        postChain = self.head.link 
        
        if preChain.data == data:
            self.head = postChain
            return
        
        while postChain != None:
            if postChain.data == data:
                preChain.link = postChain.link
                return
            else:
                preChain = preChain.link
                postChain = postChain.link
    
    def deleteAt(self, index):
        if index < 0:
            raise IndexOutOfBoundsError
        
        preChain = self.head 
        if preChain == None:
            return 
        
        postChain = self.head.link 
        
        if index == 0:
            self.head = postChain
            return
        
        while index > 1 and postChain != None:
            preChain = preChain.link
            postChain = postChain.link
            index = index - 1
        
        if index >= 1:
            raise IndexOutOfBoundsError
        
        if postChain == None:
            preChain.link = None
        else:
            preChain.link = postChain.link
        
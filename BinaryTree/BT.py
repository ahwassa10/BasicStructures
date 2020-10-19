# BT.py
# A simple class for exploring binary trees
# Sunday, October 18, 2020

class NotNodeComparisonError(Exception):
    """
    This exception is raised when the user tried to compared a BTNode instance to something that is not a BTNode.
    """
    pass

class DuplicatesFoundError(Exception):
    """
    This exception is raised when a duplicate element is inserted into the binary tree.
    """
    pass

class BTNode:
    """
    An instance of BTNode is a node in a binary tree. 
    
    Fields:
        data:   Holds the data stored in a BTNode instance
        left:   A reference to the left child node
        right:  A reference to the right child node
    
    Methods:
        __init__(self, data=None, left=None, right=None):   Initializes the BTNode with the specified data. 
        __str__(self):                                      returns the string representation of the data.
        setLeft(self, leftChild):                           Sets the left field to the specified BTNode instance.
        setRight(self, rightChild):                         Sets the right field to the specified BTNode instance.  
    """
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = left
    
    def __lt__(self, other):
        if not (isinstance(other, BTNode)):
            raise NotNodeComparisonError
        if (self.data < other.data):
            return True
        else:
            return False
    
    def __gt__(self, other):
        if not (isinstance(other, BTNode)):
            raise NotNodeComparisonError
        if (self.data > other.data):
            return True
        else:
            return False
    
    def __str__(self):
        return str(self.data)
    
    def setLeft(self, leftChild):
        self.left = leftChild
    
    def setRight(self, rightChild):
        self.right = rightChild
    

class BT:
    def insert(self, item):
        tempNode = BTNode(item)
        
        traverse = self.root
        if traverse == None:
            self.root = tempNode
        else:
            while (traverse.left != None and traverse.right != None):
                if tempNode < traverse:
                    traverse = traverse.left
                elif tempNode > traverse:
                    traverse = traverse.right
            if tempNode < traverse:
                traverse.left = tempNode
            elif tempNode > traverse:
                traverse.right = tempNode

    def __init__(self, iterable):
        self.root = None
        for element in iterable:
            self.insert(element)
    
    def __str__(self):
        
        def recursiveStringBuilder(root, depth, stringRep):
            if root == None:
                return stringRep
                
            tempString =  (stringRep + "\t" * depth + str(root) + "\n")
            tempString = recursiveStringBuilder(root.left, depth+1, stringRep)
            tempString = recursiveStringBuilder(root.right, depth+1, stringRep)
            return tempString
        
        return recursiveStringBuilder(self.root, 0, "")
        
        
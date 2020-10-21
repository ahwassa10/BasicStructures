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
        """
        Inserts the specified item into the binary tree.
        
        Duplicates are not stored in the binary tree. However, no error is raised if a duplicate is detected. 
        """
        tempNode = BTNode(item)
        
        forward = self.root
        previous = self.root
        
        while forward != None:
            if tempNode < forward:
                previous = forward
                forward = forward.left 
            elif tempNode > forward:
                previous = forward
                forward = forward.right
        
        if previous == None:
            self.root = tempNode
        elif tempNode < previous:
            previous.left = tempNode
        elif tempNode > previous:
            previous.right = tempNode

    def __init__(self, iterable=[]):
        self.root = None
        for element in iterable:
            if element == 3:
                pass
                #breakpoint()
            self.insert(element)
    
    def inorder(self):
        """
        Performs an inorder traversal of the binary tree. (Left child, root, right child)
        
        Returns a list containing the object stored in the data field of each BTNode in inorder. 
        """
        items = []
        def rinorder(root):
            if root == None:
                return
            else:
                rinorder(root.left)
                items.append(root.data)
                rinorder(root.right)
        rinorder(self.root)
        return items
    
    def preorder(self):
        """
        Performs a preorder traversal of the binary tree (root, left child, right child)
        
        Return a list containing the object stored in the data field of each BTNode in preorder
        """
        items = []
        def rpreorder(root):
            if root == None:
                return
            else:
                items.append(root.data)
                rpreorder(root.left)
                rpreorder(root.right)
        rpreorder(self.root)
        return items
    
    def postorder(self):
        """
        Performs a postorder traversal of the binary tree (left child, right child, root)
        
        Returns a list containing the object stored in the data field of each BTNode in postporder
        """
        items = []
        def rpostorder(root):
            if root == None:
                return
            else:
                rpostorder(root.left)
                rpostorder(root.right)
                items.append(root.data)
        rpostorder(self.root)
        return items
    
    def levelorder(self):
        """
        Performs a level order traversal of the binary tree. In other words, it prints each level of the binary tree in order
        
        Returns a list containing the object stored in the data field of each BTNode in levelorder
        """
        
        items = []
        if self.root == None:
            return items 
        else:
            items.append(self.root)
        
        traverse = 0
        while True:
            if traverse == len(items):
                break
            else:
                possibleChild1 = items[traverse].left
                possibleChild2 = items[traverse].right
                if possibleChild1 != None:
                    items.append(possibleChild1)
                if possibleChild2 != None:
                    items.append(possibleChild2)
                traverse = traverse + 1
        
        for i in range(len(items)):
            items[i] = items[i].data
        
        return items
    
    def __str__(self):
        
        def recursiveStringBuilder(root, depth, stringRep):
            if root == None:
                return stringRep
            
            tempString = stringRep
            tempString = recursiveStringBuilder(root.right, depth+1, tempString)
            tempString =  (tempString + "\t" * depth + str(root) + "\n")
            tempString = recursiveStringBuilder(root.left, depth+1, tempString)
            return tempString
        
        return recursiveStringBuilder(self.root, 0, "")
        
b = BT([5, 4, 10, 11])
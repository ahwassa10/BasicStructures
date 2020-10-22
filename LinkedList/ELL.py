#ELL.py
#Created October 10, 2020

class IndexOutOfBoundsError(Exception):
    """
    Objects of this class are raised when an index is out of bounds.
    """
    pass

class llNode:
    """
    An instance object of this class represents a single node in a linked list. 
    
    Fields:
        data: The data stored by the node. This data can be of any arbitrary type.
        link: Stores a reference to the next node in the linked list. 
    
    Methods:
        __init__: Constructor method that creates instance object of the llNode class.
        __str__ : Returns a string representation of the data stored in the node.
    
    """
    def __init__(self, data, link=None):
        self.data = data
        self.link = link
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    """
    Instance objects of this class are linked lists composed of instances of the llNode class.
    
    This type of linked list is not cyclical and not doubly linked. 
    
    The LinkedList class makes use of a dummy initial node and a field called cardinality to simplify the algorithms for inserting and deleting 
    nodes in the linked list. The dummy node has a None data field and initially points to None. The dummy node is not counted as part of the
    cardinality field. 
    
    Fields:
        head: Stores a reference to the dummy node at the beginning of the linked list. 
        cardinality: Stores an integer that represents the length of the linked list (number of nodes, excluding the dummy node, in the linked 
        list)
    
    methods:
        __init__    :Default constructor. Note that an interable can be optionally passed. Each element in the iterable becomes a node.
        __str__     :Returns a string representation of the linked list.
        __repr__    :Calls __str__ so these methods are functionally the same.
        __iter__    :Returns an instance of the IterableLinkedList class. This object supports Python's standard iteration protocol.
        __len__     :Returns the length (cardinality) of the linked list.
        append      :Given a datum as input, creates a new node using this data and appends it to the end of the linked list.
        insertAt    :Given a datum as input, creates a new node using this data and inserts it at the index specified.
        delete      :Given a datum as input, deletes the first node in the linked list that has this datum as its data field.
        deleteAt    :Given a index, deletes the node at that index and returns the data field of the deleted node.
        merge       :Appends an iterable object to the end of a linked list. Each element in the iterable becomes a node. 
    
    """
    def __init__(self, iterable=[]):
        """
        Creates a linked list from the elements in the passed in iterable. 
        
        If no iterable is specified, or the iterable is empty, then a linked list of cardinality=0 is created. Note that this list still
        contains the dummy node.
        """
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
        """
        Returns a string representation of the linked list.
        
        Every node is suffixed with a ", " including the last node.
        """
        string = ""
        
        traverse = self.head.link
        while traverse != None:
            string = string + str(traverse.data) + ", "
            traverse = traverse.link
        
        return string
    
    def __repr__(self):
        """
        Functionally the same as __str__.
        """
        return self.__str__()
    
    def __iter__(self):
        """
        Returns an instance object of the class IterableLinkedList.
        
        This iterable object fully supports Python's iterable protocol. This means that linked list object can be used in for loops and any other
        iteration context.
        """
        return IterableLinkedList(self.head)
    
    def __len__(self):
        """
        Returns the cardinality of the linked list. 
        """
        return self.cardinality
    
    def append(self, data):
        """
        Creates a new node using the datum in the data field and then appends the node to the end of the linked list. 
        
        Returns a reference to the last node in the linked list (the node that was appended to the end of the list by this method).
        """
        tempNode = llNode(data)
        
        traverse = self.head
        
        while traverse.link != None:
            traverse = traverse.link
        
        traverse.link = tempNode
        self.cardinality = self.cardinality + 1
        return tempNode
    
    def insertAt(self, index, data):
        """
        Creates a new node using the datum in the data field and then inserts this new node at the index specified in the index field.
        
        If the index is out of bounds, an IndexOutOfBoundsError exception is raised.
        """
    
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
        """
        Deletes the first node whose data field matches the datum passed in as the argument.
        
        Does not return anything.
        """
        traverse = self.head 
        
        while traverse.link != None:
            if traverse.link.data == data:
                traverse.link = traverse.link.link
                self.cardinality = self.cardinality - 1
                break
            traverse = traverse.link
    
    def deleteAt(self, index):
        """
        Deletes the node at the specified index and returns the data field of the deleted node.
        
        If the specified index is out of bounds, an IndexOutOfBoundsError exception is raised.
        """
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
        """
        Takes every element in iterable, converts that element into an llNode instance, and appends that instance to the end of the linked list. 
        
        Elements in the iterable are appended in the same order in which they appear in the iterable.
        """
        traverse = self.head
        
        while traverse.link != None:
            traverse = traverse.link
        
        for element in iterable:
            tempNode = llNode(element)
            traverse.link = tempNode
            self.cardinality = self.cardinality + 1
            traverse = traverse.link
    

class IterableLinkedList:
    """
    A helper class that allows instances of the linked list class to support the Python iteration protocol.
    
    Field:
        head:       Stores a reference to the dummy node at the beginning of the linked list.
        traverse:   Stores a reference to the current node in the traversal of the linked list.
    
    Methods:
        __init__:   Constructs an instance of the IterableLinkedList class. Initializes the head and traverse fields.
        __next__:   Returns the value of the data field of the node referenced by the traverse pointer. If the traverse pointer equals None, the
        StopIteration exception is raised since that signifies the end of the traversal. 
    """
    def __init__(self, head):
        self.head = head
        self.traverse = self.head
    
    def __next__(self):
        self.traverse = self.traverse.link
        if self.traverse == None:
            raise StopIteration
        else:
            return self.traverse.data
    
# testing.py
# Code for making sure that BT.py works correctly
# Monday, October 19, 2020

import BT

def test1():
    b = BT.BT()
    if b.root == None:
        return "Passed"

def test2():
    b = BT.BT([1, 2])
    if str(b.root) != "1":
        return "Incorrect insert root node"
    elif str(b.root.left) != "None":
        return "Incorrectly inserted node on left"
    elif str(b.root.right) != "2":
        return "Incorrect right insert"
    elif str(b.root.right.left) != "None":
        return "Inserted third node on left of 2"
    elif str(b.root.right.right) != "None":
        return "Inserted third node on right of 2"
    else:
        return "Passed"

def test3():
    b = BT.BT([1, 2, 3])
    if str(b.root) != "1":
        return "Incorrect insert root node"
    elif str(b.root.left) != "None":
        return "Incorrectly inserted node on left"
    elif str(b.root.right) != "2":
        return "Incorrect right insert"
    elif str(b.root.right.left) != "None":
        return "Inserted third node on left of 2"
    elif str(b.root.right.right) != "None":
        return "Inserted third node on right of 2"
    else:
        return "Passed"
        

#print("Test1: " + test1())
#print("Test2: " + test2())
#breakpoint()
b = BT.BT([1, 2, 3])
print(b)
"""
    A way of storing Newick Strings as a tree and nodes...

    two classes:

    node class
        a node in the tree (each node can have a left and a right 'child', as well as a 'parent' node)
        nodes can only have one 'parent', and two 'children'

    tree class
        
"""

import os

class node:
    """
        a node in the tree
    """

    def __init__(self, nodeId = None, distToParent = None, size = None, left = None, right = None):
        self.nodeId = nodeId
        self.isRoot = True
        if distToParent != None:
            self.distToParent = distToParent
            self.isRoot = False
        self.size = 1

    
    def __str__(self):
        s = ""
        s += str(self.nodeId) + "|"
        if not self.isRoot:
            s += str(self.distToParent)
        else:
            s += "root"
        return s

class tree:
    """
        a tree consisting of nodes
    """
    def __init__(self):
        self.numNodes = 0
        self.root = None
    
    def __add__(nodeId, distToParent):
        self.root = self.__add__(self.root, nodeId, distToParent)

x = node("stinky")

print(x)


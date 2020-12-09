class node:
    """
        ident: identity, contains the genus and species with the distance to the last common ancestor afterwords
        parent: most recent ancestor in the tree, None if ancestor is the 'root' of the tree, as this tree is unrooted
        distToParent: not used currently
        children[]: a list of all the children of that node (can be more than 2, but it is not in this case)
    """
    def __init__(self, ident, parent = None, distToParent = None):
        """
            initializes
        """
        self.parent = parent
        self.distToParent = distToParent
        self.ident = ident
        self.children = []

    def __str__(self):
        """
            overloaded string casting method
        """
        retstr = ""
        retstr += "id: " + str(self.ident) + " | external/internal (T/F): " + str(self.isExternal()) +  " | ancestor: " + str(self.parent) + "\n"
        return retstr
    
    def isRoot(self):
        """
            returns true if it doesn't have parents, not really used
        """
        if self.parent != None:
            return False
        else:
            return True

    def update(self, n):
        """
            adds children
        """
        self.children.append(n)

    def isExternal(self):
        """
            if there are children, return false
        """
        if len(self.children) == 0:
            return True
        else:
            return False

class tree:
    """
        tree class that is made of nodes
        
        size: each node added increases size
        root: if there is a root to the tree
        nodes[]: a list of all the nodes in the tree
        treeLength: the length of the tree (currently unused)
    """
    def __init__(self):
        """
            initialize
        """
        self.size = 0
        self.root = None
        self.nodes = []
        self.treeLength = 0


    def addNewNodeBetter(self, nodeString):
        """
            shouldn't be called outside of class

            adds each node
        """
        nodes = self.findNodes(nodeString)
        for nod in nodes:
            numnodes = len(self.nodes)
            for i in range(len(self.nodes)):
                i = len(self.nodes)-1-i
                if self.contains(self.nodes[i].ident, nod):
                    self.nodes.append(node(nod, self.nodes[i].ident, None))
                    self.nodes[i].update(nod)
                    break
            if numnodes == len(self.nodes):
                self.nodes.append(node(nod))
            self.size += 1
            

    def findNodes(self, st):
        """
            finds the nodes from a newick string after taking it in
        """
        oop = -1
        tempstr = ""
        externalNodes = []
        for i in range(len(st)):
            if oop == 0 and st[i] == ',' or i == len(st)-1:
                if tempstr != "" and tempstr[0] != ')':
                    externalNodes.append(tempstr)
                tempstr = ""
            elif oop == 0:
                tempstr += st[i]
            elif oop > 0:
                tempstr += st[i]
            if st[i] == '(':
                oop += 1
            elif st[i] == ')':
                oop -= 1
        return externalNodes

    def contains(self, comparing, looking):
        """
            checks to see if the string looking is in comparing
            returns true if it is
        """
        if len(comparing) < len(looking):
            return False
        for i in range(len(comparing)):
            for j in range(len(looking)):
                if j == len(looking)-1:
                    return True
                if comparing[i+j] == looking[j]:
                    continue
                else:
                    break
        return False

    def takeInNewick(self, fileName):
        """
            reads in a newick file
        """
        fileThing = open(fileName, 'r').readline().strip()
        fileThing = fileThing[:fileThing.rfind(';')]
        #intialize nodestringlist and nodelabelist
        #nodelabellist holds a numerical label for each internal node
        nodestringlist = [fileThing]
        nextnodelabel = 0
        nodelabellist = [nextnodelabel]
        # i indexes the nodes
        # this outer loop, loops over the nodestrings
        # the inner loop adds new nodestring to the end of the list
        i = 0
        while True:
            if i >= len(nodelabellist):
                break
            nodestring = nodestringlist[i]
        #    print(nodestring+"\n")  # just for checking
            # make a new string from the nodestring but without opening and closing parentheses
            nodestring_strip_parens = nodestring[nodestring.find('(')+1:nodestring.rfind(')')]

            # counters and markers for positions in noestring_strip_parens
            p = 0
            numopenparens = 0
            numcloseparens = 0
            pstart = -1
            while True:
                numopenparens += nodestring_strip_parens[p] == '('
                numcloseparens += nodestring_strip_parens[p] == ')'
                if numopenparens == 1  and numcloseparens == 0 and pstart == -1:   # set marker for beginning of a nodestring
                    pstart = p
                if numcloseparens == numopenparens and numcloseparens != 0:  # reached the end of a nodestring
                    newnodestring = nodestring_strip_parens[pstart:p+1]
                    nodestringlist.append(newnodestring)   # add the newlly found nodestring to the end of the list
                    nextnodelabel += 1  # set the label for the newly found nodestring
                    nodelabellist.append(nextnodelabel) # put the label in the list
                    # reset counters and marker so we are ready to handle the next nodestring we find
                    numopenparens = 0
                    numcloseparens = 0
                    pstart = -1
                p += 1
                if p == len(nodestring_strip_parens): # readed the end
                    i += 1
                    break
        for i in range(len(nodestringlist)):
            self.addNewNodeBetter(nodestringlist[i])



    def hasParent(self, parent):
        """
            returns a tuple (boolean, i)
            if it has a parent, and where the parent is in self.nodes
        """
        i = -1
        for i in range(len(self.nodes)):
            if self.nodes[i].parent == parent:
                return True, i
        return False, i

    def printExternalNodes(self):
        """
            prints the number of external nodes
        """
        retstr = ""
        for node in self.nodes:
            if node.isExternal():
                retstr += str(node) + "\n"
        print(retstr)

    def numExternal(self):
        """
            returns the number of external nodes
        """
        retval = 0
        for node in self.nodes:
            if node.isExternal():
                retval += 1
        return retval

    def numInternal(self):
        """
            returns the number of internal nodes
        """
        retval = 0
        for node in self.nodes:
            if not node.isExternal():
                retval += 1
        return retval

    def __str__(self):
        """
            overloaded string method, prints each node out with a blank line between them
        """
        temp = ""
        for node in self.nodes:
            temp += str(node) +"\n"
        return temp

t = tree()
t.takeInNewick("p53_homologous.out_phyml_tree.txt")
print(t)

with open("tree_output.txt", 'w') as fileThing:
    fileThing.writelines(str(t))
    fileThing.write("External Nodes: " + str(t.numExternal()) + "\n")
    fileThing.write("Internal Nodes: " + str(t.numInternal()) + "\n")
    fileThing.write("Total Nodes: " + str(t.size) + "\n")
    fileThing.close()


"""
    Implements a bifurcating ultrametric rooted tree

    two main classes:

    edge class
        an edge on a tree

    tree class
        a subclass of dictionary
        tree is always ultrametric (all external edges come up to the same time point)
        tree is always rooted

        growrandom(self,addtime):
            add time to all external edges, and then split one random external edge into two

        getedgetotaltime(self,e):
            return the time at the bottom of edge e
            have to sum all the descendant edges

        newick(self):
            return a newick string for self

        sumbranchlengths(self):
            return a simple sum of branch lengths

        checktree(self):
            does several checks of integrity
            kind of slow

        gettreestats(self):
            print length and edge count summaries

"""
import os
import sys
import random
import math


class edge:
    """
        an edge on the tree
    """

    def __init__(self,id=-1, up = None, dn = -1, t = 0.0):
        """
            nup is the # descendants (fix at 2)
            up is a list of the descendant ids
            dn is the id of the down ancestor
            t is the length of the edge  (not the time at the bottom)
            use the position in nodelist as the id #
        """
        self.id = id
        self.nup = 2
        if up != None:
            self.up = list(up)
        else:
            self.up = []
        self.dn = dn
        self.t = max(0.0,t)

    def update(self,id = None, upedge = None, up = None, dn = None, t = None):
        """
            for updating any of the basic variables belonging to an edge
        """
        if id != None:
            self.id = id
        if upedge != None: ## add the upedge to the list up
            assert upedge not in self.up
            self.up.append(upedge)
            self.nup += 1
        if up != None:
            self.up = up
        if dn != None:
            self.dn = dn
        if t != None:
            self.t = max(0.0,t)

    def isexternal(self):
        """
            True if no daughter edges
        """
        return self.up == []

    def __str__(self):
        """
            create a string with information for using print()
        """
        s =  "id %d nup %d "%(self.id,self.nup)
        if self.up == []:
            s += "[]"
        else:
            s += '['
            for i in range(self.nup):
                if i < self.nup-1:
                    s += "%d,"%self.up[i]
                else:
                    s += "%d"%self.up[i]
            s += ']'
        s += " dn %d"%self.dn
        s += " time %.3f"%self.t
        return s

class tree(dict):
    """
        a tree class, is a subclass (inherits from) the dictionary type,
        contains a phylogenetic tree
        positive integers are used as labels
    """

    def __init__(self):
        """
            initialize the dictionary with a single root edge
        """
        self.tlen = 0.0
        self.tmrca = 0.0
        label = 0
        self[label] = edge(id = label,up = [],dn = -1,t = 0.0)
        self.nextlabel = label + 1
        self.rootid = label
        self.numexternal = 1 # number of external edges


    def __add__(self, addtime):

        #overload addition +=  add addtime to all extern edges
        for key in self.keys():
            if self[key].isexternal():
                self[key].t += addtime
        self.tlen += self.numexternal * addtime ## increment the length of the tree
        self.tmrca += addtime
        return self



    def growrandom(self,addtime):
        """
            if tree has more than one edge
            add time to all external edge lengths and then

            if only one edge,  this is the root and do not add time
            randomly pick an edge to split into two daughter edges
        """
        def add_daughters ():
            """
                pick an external edge at random and make two daughters
            """
##            print(self)
            while True:
                x = random.choice(list(self.keys()))
                if  self[x].isexternal():
                    break
            self[self.nextlabel] = edge(id = self.nextlabel,up = [], dn = x,t = 0.0)

            tempup = [self.nextlabel]
            self.nextlabel += 1
            self[self.nextlabel] = edge(id = self.nextlabel,up = [], dn = x,t = 0.0)
            tempup.append(self.nextlabel)
            self.nextlabel += 1
            self[x].update(up = tempup)
            self.numexternal += 1
            return

        if len(self) > 1:
            self += addtime
        add_daughters()
        return

    def getedgetotaltime(self,e):
        """
            return the time at the bottom of edge e
            have to sum all the descendant edges
        """
        tempt = self[e].t
        while self[e].up != []:
            e = self[e].up[0]
            tempt += self[e].t
        return tempt

    def newick(self):
        """
            return a newick string for self

        """

        def innernewick(self,tempedge):
            """
                recursive
            """
            if self[tempedge].isexternal():
                return str(tempedge)
            else:
                tempnodeinfolist = []
                for i in range(2):
                    tempupid  = self[tempedge].up[i]
                    tempnodestr = innernewick(self,tempupid)
                    temptime = self[self[tempedge].up[i]].t
                    tempnodeinfolist.append(tempnodestr + ":%.5f"%(temptime))
                tempbuildnode = "(" + tempnodeinfolist[0] + ',' + tempnodeinfolist[1] + ')' + str(tempedge)
                return tempbuildnode
            return

        newickstr = innernewick(self,self.rootid) + ";"
        return newickstr

    def sumbranchlengths(self):
        """
            return a simple sum of branch lengths

        """
        sumt = 0.0
        for e in self:
            sumt += self[e].t
        return sumt

    def checktree(self):
        """
            does several checks of integrity
            kind of slow
        """
        sumt = 0.0
        countexternal = 0

        for e in self:
            if e != self.rootid:
                if (e == self[self[e].dn].up[0] or e == self[self[e].dn].up[1]) is False: # check that an up edge and its dn ege identify each other
                    print (self[e])
                    raise Exception(" up dn failure in checktree:  edge %d"%(e))
                if self[e].up != [] and self[e].up[0] == self[e].up[1]:  # check that both up edges are different
                    raise Exception (" up failure for edge %d:  up[0] %d up[1] %d"%(e,self[e].up[0],self[e].up[1]))
            else:  # its the root and should not have a dn edge or a time
                if self[e].dn != -1:
                    raise Exception (" rootid: %d  has a down edge"%(self.rootid))
                if self[e].t != 0.0:
                    raise Exception (" rootid: %d  has a t value"%(self.rootid))
        for e in self:   # loop over all edges,  sum length, and check that each edge's path to the root has length = tmrca
            sumt += self[e].t
            if self[e].isexternal():
                countexternal += 1
                d = e
                tmrcacheck = 0.0
                while self[d].dn != -1:
                    tmrcacheck += self[d].t
                    d = self[d].dn
                if math.isclose(tmrcacheck,self.tmrca) is False:
                    raise Exception("tmrca check failed: tmrcacheck %.4f  self.tmrca %.4f"%(tmrcacheck,self.tmrca))
        if math.isclose(sumt,self.tlen) is False:
            raise Exception("tlen check failed: sumt %.4f  self.tlen %.4f"%(sumt,self.tlen))
        if countexternal != self.numexternal:
            raise Exception("external count failed: count %d  self.numexternal %d"%(countexternal,self.numexternal))

    def gettreestats(self):
        """
            print length and edge count summaries
        """
        sumexlen = 0.0
        sumintlen = 0.0
        exc = intc = 0
        for e in self:
            if self[e].isexternal():
                exc += 1
                sumexlen += self[e].t
            else:
                intc += 1
                sumintlen += self[e].t
        try:
            if intc > 0:
                info = "Length : %.3f  TMRCA: %.3f #edges: %d  #internal: %d (mean length: %.4f)  #external: %d (mean length: %.4f)"%(self.tlen,self.tmrca,len(self),intc,sumintlen/intc,exc,sumexlen/exc)
            else:
                assert exc == 1
                info = "Length : %.3f  TMRCA: %.3f #edges: %d  #internal: %d #external: %d (mean length: %.4f)"%(self.tlen,self.tmrca,len(self),intc,exc,sumexlen/exc)
        except Exception:
            info = "problem getting stats"
        return info

    def __str__(self):
        s =  self.gettreestats() + "\n"
        s += self.newick() + "\n"
        return s

##a = edge(id=5,t=3.4)
random.seed(11)

t = tree()
print(t)
numnew = 5
for i in range(numnew):
    time = 1.0
    t.growrandom(time)
    print(t)

"""
def getNodesFromNewick():
"""
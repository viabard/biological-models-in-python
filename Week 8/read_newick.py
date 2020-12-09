import os

os.chdir("D:\\SCHOOL\\fall 2020\\Biological Models in Python\\Week 8")

# build a list of all the internal nodes of a newick string, i.e. all substrings with bracketing parentheses
# this does not do anything with the external nodes

nws = open("p53_homologous.out_phyml_tree.txt",'r').readline().strip()

# remove semicolon
nws = nws[:nws.rfind(';')]

#intialize nodestringlist and nodelabelist
#nodelabellist holds a numerical label for each internal node
nodestringlist = [nws]
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
    print(nodestring+"\n")  # just for checking
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

print(len(nodestringlist))
print(len(nodelabellist))

print(nodestringlist)
print(nodelabellist)


def findNodes(st):
    oop = -1
    tempstr = ""
    nodes = []
    for i in range(len(st)):
        if oop == 0 and st[i] == ',' or i == len(st)-1:
            if tempstr != "" and tempstr[0] != ')':
                nodes.append(tempstr)
            tempstr = ""
        elif oop == 0:
            tempstr += st[i]
        elif oop > 0:
            tempstr += st[i]
        if st[i] == '(':
            oop += 1
        elif st[i] == ')':
            oop -= 1
    return nodes

def contains(comparing, looking):
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

for i in range(len(nodestringlist)):
    print(findNodes(nodestringlist[i]))

print(contains("((Marsupenaeus_japonicus:2.13937634,(Drosophila_melanogaster:1.50486951,Bombyx_mori:1.21941407)0.533000:0.17840451)0.928000:0.36496209,(Mouse_p53:0.19658049,((Cricetulus_griseus:0.10016937,Microtus_ochrogaster:0.07571016)0.999000:0.11975202,(Canis_lupus:0.13043219,((Homo_sapiens:0.03963178,(Macaca_mulatta:0.00000012,Macaca_fascicularis:0.00304606)0.985000:0.02428087)1.000000:0.18106018,(Delphinapterus_leucas:0.02961825,Bubalus_bubalis:0.10883105)0.981000:0.03566226)0.887000:0.05289516)1.000000:0.18216924)0.041000:0.05880152)0.996000:0.41153571)0.968000:0.32073821)1.000000:0.53332303 (Marsupenaeus_japonicus:2.13937634,(Drosophila_melanogaster:1.50486951,Bombyx_mori:1.21941407)0.533000:0.17840451)0.928000:0.36496209", "(Marsupenaeus_japonicus:2.13937634,(Drosophila_melanogaster:1.50486951,Bombyx_mori:1.21941407)0.533000:0.17840451)0.928000:0.36496209"))
print(contains("Macaca_mulatta:0.00000012asdfasdf", "Macaca_mulatta:0.00000012"))

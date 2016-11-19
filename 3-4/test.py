from scipy.io import loadmat as load
from numpy import argsort, reshape, transpose, array, log2, zeros, transpose, delete

class Node(object):
    def __init__(self, index):
        self.index = index
        self.children = []
        self.label = "noleaf"

    def add_child(self, obj):
        self.children.append(obj)


global wang
def script4():
    data = load('restaurant.mat')
    c = array(data['c']).astype(int).tolist()  # final result for m sample
    nc = array(data['nc']).astype(int)[0].tolist()  # number of class, in restaurant data set, it is 2
    x = array(data['x']).astype(int).tolist() # main data
    nx = array(data['nx']).astype(int)  # range of each attribute
    nx = reshape(nx, [1, nx.size]).tolist()
    nx = nx[0]
    global wang
    wang = nc;

    y = array(data['y']).astype(int).tolist()
    d = array(data['d']).astype(int)
    nc = nc[0]

    tempC = list()
    for myc in c:
        tempC.append(myc[0])

    tr = tree_train(tempC,nc,x,nx)
    b = tree_classify(y, tr)
    print(b)
    print(d)

    #your_output = b
    #correct_output = d


def tree_train(c, nc, x, nx):

    tr = constructTree(c, nc, x,nx)

    return tr

def tree_classify(y, tr):

    b = list()
    for myY in y:
        b.append(lala(tr,myY))

    return b

def lala(tr, myY ):
    if(tr.index == -1):
        return tr.label
    value = myY[tr.index]
    myY.pop(tr.index)
    hey = lala(tr.children[value - 1],myY)
    return hey


def constructTree(c, nc, x,nx):

    myset = set()
    for item in c:
        myset.add(item)

    if len(myset) == 1:
        leaf = Node(-1)
        leaf.label = myset.pop()
        return leaf

    if (len(x) == 0):
        leaf = Node(-1)
        leaf.label = 1
        return leaf

    if (len(nx) == 0):
        leaf = Node(-1)
        leaf.label = 1
        return leaf

    node = constructNode(nc, c, x,nx)
    index = node.index

    for i in range(1,nx[index] + 1):
        myX = list()
        for a in x:
            temp = list()
            for b in a:
                temp.append(b)
            myX.append(temp)
        newX = list()
        newC = list()
        for j in myX:
            if j[index] == i:
                newX.append(j)
                newC.append(c[myX.index(j)])

        for hey in newX:
            hey.pop(index)

        newNX = list(nx);
        del newNX[index]

        node.children.append(constructTree(newC,nc,newX,newNX))

    return node


def constructNode(nc , c ,data,nx):

    list1 = list()
    for i in range(0, len(data[0])):
        list1.append(calculateInformationGain(i, nc, c, data,nx))
    best = max(list1)
    index = list1.index(best)
    node = Node(index)
    return node


def calculateInformationGain(index, nc, c, data,nx):
    weight = getWeight(index, data, nx)
    answer = 0
    entropyList = dict()
    for i in range(1, nc + 1):
        entropyList[i] = 0

    for j in range(1, nx[index] + 1):
        entropyList[j] = calculateEntropy(index, j, data, c, nc,weight)

    for e in entropyList:
        answer = answer - (weight[e] / len(data)) * entropyList[e]
    return answer


def getWeight(index, x, nx):

    dict1 = dict()
    for n in range(1, nx[index] + 1):
        dict1[n] = 0

    for i in x:
        a = i[index]
        dict1[a] = dict1[a] + 1
    return dict1


def calculateEntropy(index, value, x, c, nc,weight):

    dict1 = dict()
    for n in range(1, nc + 1):
        dict1[n] = 0

    for i in x:
        if i[index] == value:
            dict1[c[x.index(i)]] = dict1[c[x.index(i)]] + 1

    answer = 0;
    for a in dict1:
        if dict1[a] != 0:
            answer = answer - (dict1[a] / weight[value]) * (log2(dict1[a] / weight[value]))

    return answer

script4()
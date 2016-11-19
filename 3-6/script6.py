#script6   Complete the exercise only using the core Python language and the
#following imported functions as needed:

from scipy.io import loadmat as load
from numpy import reshape, array, zeros, log, argmax,min,max,asarray,prod,delete,trace
from matplotlib.pyplot import figure, plot, legend,show

def script6():

    data = load('seed_data.mat')
    c = array(data['c']).astype(float).tolist()
    nc = array(data['nc']).astype(float).tolist()
    x = array(data['x']).astype(float)
    nc = int(nc[0][0])
    tempC = list()
    for i in c:
        tempC.append(i[0])

    validate(x,nc,tempC,6)
    plotGraph(x,6,tempC,nc)


    return

def plotGraph(x, nk, c, nc):
    X = x.tolist()
    a = transformX(x, X, nk)
    b = a[1] + (a[2] / 2)
    b1 = list()
    b2 = list()
    b1.append(b[0])
    b2.append(b[1])
    for i in range(1, 6):
        b1.append(b1[i - 1] + a[2][0])
        b2.append(b2[i - 1] + a[2][1])
    miao = list()
    miao.append(b1)
    miao.append(b2)
    counts = getTP(c,nc)
    pc = list()
    for count in counts:
        pc.append(count/len(x.tolist()))

    bb = getCountTable(nk, a[0], c, nc)
    pr = (getPTable(bb, counts, len(x[0]), nk, nc))# 0

    for i in range(0,2):
        arr = asarray(pr[i])
        for j in range(0, nc):
            plot(asarray(miao[i]),arr[:,j]*pc[j],label = j+1)
            legend('123')
        show()


def validate(x,nc,c,nk):
    matrix = zeros((nc,nc))
    length = len(x.tolist())
    for i in range(0, length):
        newX = delete(x, i, axis = 0)
        test = list()
        test.append(x[i])
        test = asarray(test)
        pr = naivebayes_train(c, nc, newX, nk)
        label = naivebayes_classify(pr, test)
        matrix[label[0][0] - 1][int(c[i]) - 1] += 1
    accu = trace(matrix)/len(x.tolist())
    print(accu)
    print(matrix)



def naivebayes_train(c,nc,x,nk):
    pr = list()
    X = x.tolist()
    a = transformX(x, X, nk)
    b = getCountTable(nk, a[0], c, nc)
    pr.append(getPTable(b, getTP(c, nc), len(x[0]), nk, nc))#0
    pr.append(nc)#1
    pr.append(nk)#2
    pr.append(len(x[0]))#3
    pr.append(a[1])#4
    pr.append(a[2])#5
    return pr

def naivebayes_classify(pr,y):

    Y = y.tolist()
    attrMin = pr[4]
    diff = pr[5]
    newY = list()
    for myX in Y:
        temp = list()
        for a in myX:
            index = int((a - attrMin[myX.index(a)]) / (diff[myX.index(a)])) + 1
            if (index == (pr[2] + 1)):
                temp.append(pr[2])
            else:
                temp.append(index)
        newY.append(temp)
    haha = list()
    for i in range(0, len(newY)):
        lala = list()
        for j in range(0, pr[3]):
            lala.append(pr[0][j][newY[i][j] - 1])
        haha.append(lala)

    aa = asarray(haha)
    b = list()
    for i in aa:
        b.append(prod(i,axis=0).tolist())

    c_hat = list()
    for bb in b:
        f = list()
        f.append(bb.index(max(bb)) + 1)
        c_hat.append(f)

    return c_hat



def getTP(c, nc):
    myDict = dict()
    for i in range(1, nc + 1):
        myDict[i] = 0
    for j in c:
        myDict[j] = myDict[j] + 1

    return list(myDict.values())

def transformX(x,X,nk):

    attrMin = min(x, axis=0)
    attrMax = max(x, axis=0)
    diff = (attrMax - attrMin)/nk
    aa = list()
    newX = list()
    for myX in X:
        temp = list()
        for a in myX:
            index = int((a - attrMin[myX.index(a)])/ (diff[myX.index(a)])) + 1
            if(index == (nk+1)):
                temp.append(nk)
            else:
                temp.append(index)
        newX.append(temp)

    aa.append(newX)
    aa.append(attrMin)
    aa.append(diff)

    return aa

def getCountTable(nk, x, c, nc):

    overall = list()
    for j in range(0, len(x[0])):
        temp = list()
        for k in range(1 , nk + 1):
            temp1 = list()
            for i in range(0, nc):
                temp1.append(1)#avoid zero
            temp.append(temp1)
        overall.append(temp)

    for j in range(0, len(x[0])):
        count = -1
        for a in x:
            count += 1
            cl = c[count]
            overall[j][int(a[j] - 1)][int(cl) - 1] += 1

    return overall

def getPTable(ct, count, nx, nk ,nc):
    for a in range(0,nc):
        count[a] += nk

    for i in range(0, nx):
        for j in range(0, nk):
            for k in range(0, nc):
                ct[i][j][k] = ct[i][j][k] / count[k]

    return ct;






script6()


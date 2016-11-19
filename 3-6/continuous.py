#script6   Complete the exercise only using the core Python language and the
#following imported functions as needed:
import math
from scipy.io import loadmat as load
from numpy import reshape, array, zeros, log, argmax
#from matplotlib.pyplot import figure, plot, legend

def script6():

    data = load('seed_data.mat')
    c = array(data['c']).astype(float).tolist()
    nc = array(data['nc']).astype(float).tolist()
    x = array(data['x']).astype(float).tolist()
    nx = len(x[0])
    nc = nc[0][0]
    nc = int(nc)

    tempC = list()
    for i in c:
        tempC.append(i[0])

    a = naivebayes_train(tempC, x,nc)
    b = naivebayes_classify(a, x[1])

    print(b)


def getTP(c, nc):
    myDict = dict()
    for i in range(1, nc + 1):
        myDict[i] = 0
    for j in c:
        myDict[j] = myDict[j] + 1
    for k in myDict:
        myDict[k] = myDict[k]/len(c)
    return myDict


def naivebayes_train(c,x, nc):
    pr = list()
    a = get(len(x[0]), x,c)
    #print(getMeanAndSD(a))
    pr.append(getMeanAndSD(a))

    pr.append(getTP(c, nc))
    return pr

def getMeanAndSD(list1):
    answer = list()
    for dict1 in list1:
        mydict = dict()
        for a in dict1:
            mydict[a] = list()
            mean = calculateMean(dict1[a])
            std = calculateSTD(dict1[a], mean)
            mydict[a].append(mean)
            mydict[a].append(std)
        answer.append(mydict)
    return answer


def getPro(x, mean, sd):
    a = sd**2
    pi = 3.1415926
    b = (2*pi*a)**.5
    c = math.exp(-(float(x)-float(mean))**2/(2*a))
    return c/b

def calculateMean(list1):
    return sum(list1)/len(list1)

def calculateSTD(list, mean):
    differences = [x - mean for x in list]
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)
    variance = ssd/ (len(list) - 1)
    sd = math.sqrt(variance)
    return sd


def get(nx, x, c):
    overall = list()

    for j in range(0, nx):
        d = dict()
        for a in x:
            if c[x.index(a)] in d:
                d[c[x.index(a)]].append(a[j])
            else:
                d[c[x.index(a)]] = list();
                d[c[x.index(a)]].append(a[j])
        overall.append(d)

    return overall


def naivebayes_classify(pr,y):

    answer = list()
    for i in range(0, len(y)):
        myDict = pr[0][i]
        templist = list()
        for j in myDict:
            prob = getPro(y[i], myDict[j][0], myDict[j][1])
            templist.append(prob)
        answer.append(templist)

    final = pr[1]
    for an in answer:
        for ans in an:
            final[an.index(ans) + 1] = final[an.index(ans) + 1] * ans

    counter = 0
    for word in final.keys():
        if final[word] > counter:
            counter = word

    return counter


script6()





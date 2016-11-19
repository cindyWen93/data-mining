#Script4   Complete the exercise only using the core Python programming language
#and the following imported functions as needed:

from scipy.io import loadmat as load
from numpy import argsort, reshape, transpose, array, log2, zeros, transpose

def script4():

   data = load('restaurant.mat');
   c = array(data['c']).astype(int)
   nc = array(data['nc']).astype(int)[0]
   x = array(data['x']).astype(int)
   nx = array(data['nx']).astype(int)
   nx = reshape(nx,[1,nx.size])
   y = array(data['y']).astype(int)
   d = array(data['d']).astype(int)


   tr = tree_train(c,nc,x,nx);
   b = tree_classify(y,tr)

   your_output = b
   correct_output = d


   return


def tree_train(c,nc,x,nx):

   tr = []
   return tr

def tree_classify(y,tr):

   b = []
   return b


script4()

import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

class LM:
  def __init__(self, y, X = None, verbose = False):
    ### process arguments
    self.y = y
    self.n = len(y)
    
    if X is None:
      X = np.ones(self.n).reshape(self.n, 1)
    self.X = X
    self.p = X.shape[1]
    self.verbose = verbose
    
    ### others
    self.fitted = False
    
    self.beta_hat = None
    self.y_hat = None
    self.residuals = None
    
  def fit(self):
    ### estimate model parameters
    # beta = (X'X)^(-1) X' y
    self.beta_hat = np.linalg.inv(self.X.transpose().dot(self.X)).dot(self.X.transpose().dot(self.y)) 
  
    self.y_hat = self.X.dot(self.beta_hat)
    self.residuals = self.y - self.y_hat
      
    self.fitted = True

  def __repr__(self): 
    line_dim = ' -- ' + str(self.n) + ' observations, ' + str(self.p) + ' predictors\n'
    
    if self.fitted == False:
      return 'Linear Model (not fitted yet)\n' + line_dim
    else:
      line_beta = ' -- beta: ' + str(mod.beta_hat.transpose())
      return 'Liner Model (fitted)\n' + line_dim + line_beta
  
  def plot(self, type = 1):
    if type == 1:
      self.plotRes()
    
  def plotRes(self):
    fig = plt.figure()
    
    plt.scatter(self.y_hat, self.residuals, figure = fig)
    plt.xlabel('Fitted values')
    plt.ylabel("Residuals")
    plt.title("Linear Model")
    plt.axhline(0)
    
    fig.show()
    
#-------------
# Tests
#-------------

def sim_dat1(n = 100, beta = [3, 2, 1]):
  np.random.seed(1)

  x0 = np.ones(n).reshape((n, 1))
  x1 = np.random.normal(loc = 0, scale = 2, size = n).reshape((n, 1))
  x2 = np.matrix(np.random.normal(loc = 0, scale = 1, size = n)).reshape((n, 1))
  
  X = np.concatenate((x0, x1, x2), 1)
  
  b = np.array(beta).reshape((3, 1))
  error = np.random.normal(scale = 2, size = n).reshape((n, 1))
  
  y = X.dot(b) + error
    
  return(y, X)
  
def main():
  print ' * test `sim_dat1`:'
  (y, X) = sim_dat1()
  mod = LM(y, X)
  mod.fit()

if __name__ == '__main__': main()

(y, X) = sim_dat1()
mod = LM(y, X)
mod.fit()


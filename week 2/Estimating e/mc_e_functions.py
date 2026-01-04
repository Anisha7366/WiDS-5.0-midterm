import numpy as np
import random

def Area(n,N):
  x=np.random.uniform(1,n,N)
  y=np.random.uniform(0,1,N)

  under_curve=x*y
  inside_mask=under_curve<1
  count=np.sum(inside_mask)

  return (n-1)*count/N

#returning euler's constant by calculating area under log graph between 1 and n

def get_e_method1(n,N):
  return n**(1/Area(n,N))

#returning e by method suggested in the hint(uses for loop)

def get_e_method2(N):
  num=np.array([])

  for i in range(N):
    n=2
    num1=random.uniform(0,1)
    while(True):
      num2=random.uniform(0,1)
      if num2>=num1:
        break
      num1=num2
      n+=1
    num=np.append(num,n)

  e=np.mean(num)
  return e


import numpy as np

#function taking other functions as input

def run_simulation(predicate_func , bounds , N):
  x=np.random.uniform(bounds[0],bounds[1],N)
  y=np.random.uniform(bounds[2],bounds[3],N)

  logical_mask = predicate_func(x, y)
  count=np.sum(logical_mask)

  area=(bounds[1]-bounds[0])*(bounds[3]-bounds[2])*count/N

  return area

def is_in_circle(x,y):
  return (x**2+y**2)<=1

def is_in_parabola(x,y):
  return (y<=x**2)

def is_in_gaussian(x,y):
  return y<=np.e**(-x**2)
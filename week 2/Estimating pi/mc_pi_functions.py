import numpy as np

#function returning pi by applying monte carlo methods 

def get_pi(N):
    points=np.random.uniform(-1,1,size=(N,2))
    distances=np.sum(points**2,axis=1)
    inside_mask=distances<=1
    count=np.sum(inside_mask)

    return 4*count/N
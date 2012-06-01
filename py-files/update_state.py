#!/usr/local/bin/python
import vec_field as vf
import numpy as np
import scipy as sp


def update_vec_field(x_1,x_2,x_3,K,r,a_1,a_2,b_1,b_2,d_1,d_2,e_1,e_2,tau):

    x0=np.array([x_1,x_2,x_3])
    par=[K,r,a_1,a_2,b_1,b_2,d_1,d_2,e_1,e_2]
    x=list(x0)+par
    f_1=np.array(apply(vf.vec_field,x))
   
    x1=x0+0.5*tau*f_1
    x=list(x1)+par
    f_2=np.array(apply(vf.vec_field,x))


    x2=x1+0.5*tau*f_2
    x=list(x2)+par
    f_3=np.array(apply(vf.vec_field,x))

    x3=x2+0.5*tau*f_3
    x=list(x3)+par
    f_4=np.array(apply(vf.vec_field,x))
    
    x0=x0+((1.0/6.0)*tau )*(f_1 + 2.0*f_2 + 2.0*f_3 + f_4)

    return x0

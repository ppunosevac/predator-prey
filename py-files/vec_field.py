#!/usr/local/bin/python


def vec_field(x_1,x_2,x_3,K,r,a_1,a_2,b_1,b_2,d_1,d_2,e_1,e_2):

    v_1 = r*(1.0-x_1/float(K))*x_1-(a_1*x_1*x_2)/float(1+b_1*x_1)
    v_2 = (e_1*a_1*x_1*x_2)/float(1+b_1*x_1)-(a_2*x_2*x_3)/float(1+b_2*x_2)-d_1*x_2
    v_3 = (e_2*a_2*x_2*x_3)/float(1+b_2*x_2)-d_2*x_3


    return[v_1,v_2,v_3]

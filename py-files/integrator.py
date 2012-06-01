#!/usr/local/bin/python
import update_state as usv
import numpy as np

K = 5.0
r = 7.0
a_1 = 1.0
a_2 = 1.0
b_1 = 1.0
b_2 = 1.0
d_1 = 1.0
d_2 = 1.0
e_1 = 1.0
e_2 = 1.0
par=[K,r,a_1,a_2,b_1,b_2,d_1,d_2,e_1,e_2]

init_state =np.array([1.0,1.0,1.0])
time = 0.0
tau = 0.1
t_max = 50.0

while time <= t_max:
    print time, init_state[0],init_state[1],init_state[2]
    x=list(init_state)+par+[tau]
    state = np.array(apply(usv.update_vec_field,x))
    init_state = state
    time = time + tau


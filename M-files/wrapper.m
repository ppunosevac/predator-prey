clear all
close all

clc

file = fopen('mama.dat','w')

tspan=[0:0.1:50];
x_init=[1.0,1.0,1.0];

% solve system
[t,x]=ode45(@vec_field,tspan,x_init);        

x(:,1)

fclose(file)

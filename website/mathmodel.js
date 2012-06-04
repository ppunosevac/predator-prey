x1 = 1.089;
x2 = 0.1417;
x3 = 8.758;
a1 = 1;
a2 = 1;
b1 = 1;
b2 = 1;
e1 = 1;
e2 = 1;
d1 = 1;
d2 = 1;
r = 7;

K = 5;

tau = 0.1;




function vec_add_vec(vec1, vec2)
{
	newVec = [];
	
	for (i in vec1)
		newVec.push(vec1[i]+vec2[i]);
	return newVec;
}

function vec_multiply_by_scalar(vec1, scalar)
{
	newVec = [];
	for (i in vec1)
		newVec.push(vec1[i]*scalar);
	return newVec;
}

function vect_field(vec)
{
	x1 = vec[0];
	x2 = vec[1];
	x3 = vec[2];
	
	x1 = r*(1-x1/K)*x1 - (a1*x1*x2)/(1+b1*x1);
	x2 = (e1*a1*x1*x2)/(1+b1*x1) - (a2*x2*x3)/(1+b2*x1)-(d1*x2);
	x3 = (e2*a2*x2*x3)/(1+b2*x2) - (d2*x3);
	
	return [x1, x2, x3];
}


function update_vect_field(x0, tau)
{
	f1 = vect_field(x0);
	
	x_1 = vec_add_vec(x0, vec_multiply_by_scalar(f1, 0.5*tau));
	f2 = vect_field(x_1);
	
	x_2 = vec_add_vec(x_1, vec_multiply_by_scalar(f2, 0.5*tau));
	f3 = vect_field(x_2);
	
	x_3 = vec_add_vec(x_2, vec_multiply_by_scalar(f3, 0.5*tau));
	f4 = vect_field(x_3);
	
	x0 = vec_add_vec(
		x0,
		vec_multiply_by_scalar(
			vec_add_vec(f1, 
				vec_add_vec(
					vec_add_vec(vec_multiply_by_scalar(f2, 2), vec_multiply_by_scalar(f3, 2)),
					f4)),
			1.0/6.0)
	);
	return x0;
}


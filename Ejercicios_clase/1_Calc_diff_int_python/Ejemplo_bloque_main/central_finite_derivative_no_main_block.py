def approx_first_derivative_no_main_block(f,x,h):
    """
    Numerical differentiation by finite differences. Uses central point formula
    to approximate first derivative of function.
    Args:
        f (function): function definition.
        x (float): point where first derivative will be approximated
        h (float): step size for central differences. Tipically less than 1
    Returns:
        df (float): approximation to first_derivative.
    """
    df = (f(x+h) - f(x-h))/(2.0*h)
    return df

def approx_second_derivative_no_main_block(f,x,h):
    """
    Numerical differentiation by finite differences. Uses central point formula
    to approximate second derivative of function.
    Args:
        f (function): function definition.
        x (float): point where second derivative will be approximated
        h (float): step size for central differences. Tipically less than 1
    Returns:
        ddf (float): approximation to second_derivative.
    """
    ddf =(f(x+h) - 2.0*f(x) + f(x-h))/h**2
    return ddf

## Python libraries
import numpy as np

## Parameters
f = np.arctan
x = 0.9
h = 1e-6

## Main code
res_first_d = approx_first_derivative_no_main_block(f,x,h)
res_second_d = approx_second_derivative_no_main_block(f,x,h)

print(res_first_d)
print(res_second_d)

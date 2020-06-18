from central_finite_derivative_alternative import approx_first_derivative_alternative, \
                                                  approx_second_derivative_alternative
import numpy as np

## Parameters
f = np.arctan
x = 0.9
h = 1e-6

## Main code
res_first_d = approx_first_derivative_alternative(f,x,h)
res_second_d = approx_second_derivative_alternative(f,x,h)

print(res_first_d)
print(res_second_d)

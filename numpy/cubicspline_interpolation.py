from scipy.interpolate import CubicSpline
from scipy.interpolate import CubicHermiteSpline
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

distance = 2.4
# x = [0, 1.2 , distance,  1.5* distance, 2*distance ]
# y = [0, 0.2, 0.4, 0.2, 0, ]
x = [0,0.1, 0.2, 0.2 + distance, 0.2 + distance + 0.2,  0.2 + 2*distance ,6]
y = [0, 0 ,  0 , 0.4           ,  0.4,0         ,    0]

x = [7,8 ,9,9.1]
y= [37,35.5, 34,33]

# use bc_type = 'natural' adds the constraints as we described above
#f = CubicSpline(x, y, bc_type='natural')
#f = CubicHermiteSpline(x, y, dydx=[0,0,0,0,0, 0,0])
f = CubicHermiteSpline(x, y, dydx=[ 0,1, 1e10, 1e20])

coefficients=f.c #생성된 객체 f에 대해 
for i in range( len(x)-1 ): 
    print(f"구간 {x[i]} to {x[i+1]} : {coefficients[:,i]}")

class cubic_spline_function: 
    def __init__ (self,i, data):
        self.a=data[0]
        self.b=data[1]
        self.c=data[2]
        self.d=data[3]
        
        self.real_function(i)

    def real_function(self,i):
        print(f"{i}번쨰 구간의 함수 {self.a} *x^3 + {self.b}*x^2 + {self.c}* x + {self.d }")
        
for i in range(len(x) - 1):
    sample = cubic_spline_function(i, coefficients[:, i])


x_new = np.linspace(7, 9.1, 200)
y_new = f(x_new)

plt.figure(figsize = (20,20))
plt.plot(x_new, y_new, 'b')
plt.plot(x, y, 'ro')
plt.title('Cubic Hermite Spline Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
 


#전체 path를 따서 Cubic Spline에 넣어서 
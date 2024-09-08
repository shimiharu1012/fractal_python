
# マンデルブロ集合をmatplotlibで描画する

import numpy as np
import matplotlib.pyplot as plt


# x+yiは、[x,y]として定義する

# 複素数同士の足し算
def complex_add(z1,z2):
    return [z1[0]+z2[0],z1[1]+z2[1]]

# 複素数の2乗
def complex_double(z):
    return [z[0]**2-z[1]**2,2*z[0]*z[1]]

# 複素数の絶対値(2乗)
def complex_abs(z):
    return z[0]**2+z[1]**2
    
# 複素数cがマンデルブロ条件式を満たすか否か
# 漸化式は100項目まで、収束判定は|z|^2<4で行う
def Mandelbrot_condition(c):
    z=[0,0]
    for i in range(100):
       print(z)
       z=complex_add(complex_double(z),c)
       if complex_abs(z)>4:
        return False
    
    return True


x_max=3
x_min=-3
y_max=3
y_min=-3
fineness=1000
x_step=(x_max-x_min)/fineness
y_step=(y_max-y_min)/fineness

data=np.zeros((fineness,fineness))

for i in range(fineness):
    x=x_min+x_step*i
    for j in range(fineness):
        y=y_min+y_step*j
        c=[x,y]
        if Mandelbrot_condition(c):
            data[j][i]=1

print(data)
plt.imshow(data, cmap='PiYG', extent=(x_min, x_max, y_min, y_max))

plt.grid(False)  # グリッド線を非表示
plt.show()
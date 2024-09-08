# バーンズリーのシダをmatplotlibで描画する
# 描画の様子アニメーションで確認することができる

import numpy as np
import matplotlib.pyplot as plt

x_max=5
x_min=-5
y_max=10
y_min=0
pixel=1000 #画素数

# 描画用データ
data=np.zeros((pixel,pixel))

# アニメーション機能を作りたい...

[x,y]=[0.0,0.0]
for i in range(1000000):
    rand=np.random.rand()
    if rand<0.01:
        [[a,b],[c,d]]=[[0.,0.],[0.,0.16]]
        [e,f]=[0.,0.]
    elif rand<0.86:
        [[a,b],[c,d]]=[[0.85,0.04],[-0.04,0.85]]
        [e,f]=[0.,1.6]
    elif rand<0.93:
        [[a,b],[c,d]]=[[0.2,-0.26],[0.23,0.22]]
        [e,f]=[0.,1.6]
    else:
        [[a,b],[c,d]]=[[-0.15,0.28],[0.26,0.24]]
        [e,f]=[0.,0.44]
    
    [x,y]=[a*x+b*y+e,c*x+d*y+f]
    
    X=min(pixel-1,int(((x-x_min)/(x_max-x_min))*pixel))
    Y=-min(pixel-1,int(((y-y_min)/(y_max-y_min))*pixel))
    data[Y][X]=1
    

plt.imshow(data, cmap='Greens',extent=(x_min,x_max,y_min,y_max))

plt.grid(False)  # グリッド線を非表示
plt.show()
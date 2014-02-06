'''
Created on Feb 5, 2014

@author: c3h3
'''

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import animation

data = pd.DataFrame(data=0., index=np.arange(0, 30, 1), columns=np.arange(0,1, 0.01))
for exp in data.index.values:
    data.ix[exp] = np.arange(0,1, 0.01)**(.1*exp)
    

def animate(nframe):
    plt.cla()
    plt.plot(data.columns.values, data.ix[nframe])
    plt.ylim(0,1)
    plt.title('Exp: %.2f'%(1.*nframe/10.))
    

fig = plt.figure(figsize=(5,4))  

anim = animation.FuncAnimation(fig, animate, frames=30)
anim.save('demoanimation.gif', writer='imagemagick', fps=4);


if __name__ == '__main__':
    pass
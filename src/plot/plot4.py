import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import itertools
X = [1,2,3,4,5]
Ys = np.array([
      [0.64,0.65,0.90,0.8,0.74],
      [0.62,0.65,0.3,0.2,0.34],
      [0.68,0.63,0.5,0.6,0.43],
      [0.32,0.67,0.45,0.89,0.79],
      [0.61,0.62,0.56,0.81,0.71]])




#nCols = len(X)  
#nRows = Ys.shape[0]
##En vez de rainbow darle yo los colores
colors = cm.rainbow(np.linspace(0, 1, len(Ys)))
beta=[0.05,0.15,0.40,0.60,0.80]
#cs = [colors[i//len(X)] for i in range(len(Ys)*len(X))] 
#cs2 = ['red','green','blue','yellow','grey']
#Xs=X*nRows 
#red_patch = mpatches.Patch(color='red', label='The red data')
#plt.legend(handles=[red_patch])
#colors = cm.rainbow(np.linspace(0, 1, len(Ys)))
colors = itertools.cycle(["red", "blue", "green", "yellow", "lime"])
beta=[0.05,0.15,0.40,0.60,0.80]
i=0
for y, c in zip(Ys, colors):
    plt.scatter(X, y, color=c)   
    plt.plot(X, y,color=c, label=beta[i])
    i=i+1  
axis=[0, 6, 0, 1]
plt.axis(axis)
plt.ylabel('AUC')
plt.xlabel('NSUS')



# Now add the legend with some customizations.
plt.legend(loc='upper right', shadow=True)



plt.show()   





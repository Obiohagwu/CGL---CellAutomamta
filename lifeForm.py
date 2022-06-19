import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import animation, rc 
from matplotlib.animation import FuncAnimation


# lets initalize grid size
N = 75

generations = 40
p_seed = 0.5

# Let
Grid = np.zeros((N,N))
Data = np.zeros(N*N*generations).reshape(N, N, generations)

#random initial grid
for i in range(N):
  for j in range(N):
    if (p_seed<np.random.rand()):
      Grid[i][j]=0
    else:
      Grid[i][j]=1
    if i==0 or i==N-1:
      Grid[i][j]=0
    if j==0 or j==N-1:
      Grid[i][j]=0


#beacon - try this one!
# Grid[1][1]=1
# Grid[1][2]=1
# Grid[2][1]=1

# Grid[4][3]=1
# Grid[3][4]=1
# Grid[4][4]=1

plt.imshow(Grid, cmap='binary')
plt.show()

def neighbors(X, i, j):
  counter =0
  for n in range(3):
    for m in range(3):
      if X[i-1+n][j-1+m]>0:
        counter=counter+1
  if X[i][j]>0:
    counter= counter-1
  return counter

def evolve(X):
# Overpopulation: if a living cell is surrounded by more than three living cells, it dies.
# Stasis: if a living cell is surrounded by two or three living cells, it survives.
# Underpopulation: if a living cell is surrounded by fewer than two living cells, it dies.
# Reproduction: if a dead cell is surrounded by exactly three cells, it becomes a live cell.
  X_new = np.zeros((N,N))
  for i in range(1,N-1):
    for j in range(1,N-1):
      K = neighbors(X,i,j)
      if X[i][j]>0 and K>3:
        X_new[i][j]=0
      if X[i][j]>0 and K>1 and K<4:
        X_new[i][j]=1
      if X[i][j]>0 and K<2:
        X_new[i][j]=0
      if X[i][j]<1 and K>2 and K<4:
        X_new[i][j]=1
  X=X_new
  return X

for t in range(generations):
  for i in range(N):
    for j in range(N):
      Data[i][j][t] = Grid[i][j]
  Grid = evolve(Grid)
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig, ax = plt.subplots()

def animate(i):
   ax.clear()
   ax.imshow(Data[:, :, i],cmap='binary')

ani = animation.FuncAnimation(fig, animate, generations, interval=50, blit=False)

rc('animation', html='jshtml')


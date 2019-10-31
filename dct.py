import math
import numpy as np

def tinhTong(u,v):
   sum=0
   for i in range(8):
      for j in range(8):
         sum+=math.cos(((2*i+1)*math.pi*u)/16)*math.cos(((2*j+1)*math.pi*v)/16)*fij[i][j]
   if u==0:
      Cu=math.sqrt(2)/2
   else:
      Cu=1
   if v==0:
      Cv=math.sqrt(2)/2
   else:
      Cv=1
   Fuv[u][v]=Cu*Cv*sum/4

fij=np.array([(20,20,20,20,20,20,20,20),
	      (20,20,20,20,20,20,20,20),
	      (20,20,20,20,20,20,20,20),
	      (20,20,20,20,20,20,20,20),
	      (20,20,20,20,20,20,20,20),
	      (20,20,20,20,20,20,20,20),
	      (20,20,20,20,20,20,20,20),
	      (20,20,20,20,20,20,20,20)])

Fuv=np.array([(0,0,0,0,0,0,0,0),
	      (0,0,0,0,0,0,0,0),
	      (0,0,0,0,0,0,0,0),
	      (0,0,0,0,0,0,0,0),
	      (0,0,0,0,0,0,0,0),
	      (0,0,0,0,0,0,0,0),
	      (0,0,0,0,0,0,0,0),
	      (0,0,0,0,0,0,0,0)])

u=0
v=0
for u in range(8):
   for v in range(8):
      tinhTong(u,v)
print(fij)
print(Fuv)

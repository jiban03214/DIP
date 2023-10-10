#NOISE Generating Function 
# g(x.y)<- originaal image 
#f(x,y)<- Nosie image
#n(x,y)<- Amt of noise 
# nOISE GENERATING eXPRECSSION = f(x,y)=g(x,y)+n(x,y)

import numpy as np

p=open("tiger.pgm","r")
f1=p.readline()
f2=p.readline()
f3=p.readline()
f4=p.readline()

[c,r]=[int(i) for i in f3.split()]
k=np.zeros((r,c),np.int64)

for i in range(r):
    for j in range(c):
        k[i,j]=p.readline()
p.close()
z= int(input("Enter the max intensity value::-"))
ra=np.random.randint(z+1,size=(r,c))

q=open("tiger12.pgm","w")
q.write(f1)
q.write(f2)
q.write(f3)
q.write(f4)

for i in range(r):
    for j in range(c):
        if(ra[i,j]==z):
            k[i,j]=255
        if(ra[i,j]==0):
            k[i,j]=0
        q.write("%d\n"%k[i,j])
q.close()                
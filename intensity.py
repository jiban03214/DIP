#based on regions of intenst (ROI)we have slice image call intensity level sling .
#ex:-if  you find water body pixels from a given sattelite image
import numpy as np
p=open("water.pgm","r")
f1=p.readline()
f2=p.readline()
f3=p.readline()
f4=p.readline()

[w,h]=[int(i) for i in f3.split()]
k=np.zeros((h,w),np.int64)

for i in range(h):
    for j in range(w):
        k[i,j]=p.readline()
p.close()

q=open("Water1.pgm","w")
q.write("%s"%f1)
q.write("%s"%f2) 
q.write("%s"%f3) 
q.write("%s"%f4)  

for i  in range(h):
    for j in range(w):
        if k[i,j]>100 and k[i,j]<155:
            q.write("255\n")
        else:
            q.write(str(k[i,j])+"\n")            
q.close()
#
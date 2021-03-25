import numpy as np
a=np.array([[0.75,0.75,1],[1,1,1],[1.25,1.5,1],[0,1,-1],[0.25,1.75,-1],[1,2,-1],[1.75,1.75,-1],[2,1,-1],[1.75,0,-1],[1,0,-1],[0.25,0.25,-1]])
w1=0
w2=0
b=0
teta=0
alpha=0.7
finish=0
error=np.array([1,1,1,1,1,1,1,1,1,1,1])
for y in range(100):
    x=0
    if finish!=1:
        for i in range(11):
            net=(w1*((a[(i,0)]-1)**2))+(w2*((a[(i,1)]-1)**2))-b
            #print(net)
            if net>teta:
                h=-1
            else:
                h=1
                #print(h)
            error[i]=h-a[(i,2)]
            #print(error[i])
            if error[i]!=0:
                w1=w1+alpha*a[(i,0)]*a[(i,2)]
                #print(w1)
                w2=w2+alpha*a[(i,1)]*a[(i,2)]
                #print(w2)
                b=b+alpha*a[(i,2)]
            else:
                x=x+1
            if(x>=10):
               finish=1
               print("finish")
               print("w1:",w1)
               print("w2:",w2)
               print("b:",b)
               print("epoch:",y+1)
               print("teta:",teta)
               print("alpha:",alpha)

import numpy as np
a=np.array([[0,0,-1],[1,1,-1],[1,-1,-1],[2,0,1],[2,2,-1],[2,-2,-1],[2.5,0,1],[3,0,1],[3,3,-1],[3,-3,-1]])
w1=0
w2=0
b=0
teta=0.5
alpha=0.7
finish=0
error=np.array([1,1,1,1,1,1,1,1,1,1])
for y in range(30):
    x=0
    if finish!=1:
        for i in range(10):
            net=((a[(i,0)])**2)*w1+((a[(i,1)])**2)*w2-b
            #print(net)
            #net=(a[(i,1)]**2)-(4*w1*(a[(i,0)]-1.25))
            if net>teta:
                h=1
            else:
                h=-1
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
            if(x>=9):
               finish=1
               print("finish")
               print("w1:",w1)
               print("w2:",w2)
               print("b:",b)
               print("epoch:",y+1)
               print("teta:",teta)
               print("alpha:",alpha)

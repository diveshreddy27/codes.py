import math


def rightoperation(i,j,x,d,o,c):
    j=j+1
    if(j!=c and x[i][j]==0):
        x[i][j]=d
        d=d-1
    else:
        o='D'
        j=j-1
    return i,j,x,d,o,c
def leftoperation(i,j,x,d,o,c):
    j=j-1
    if(j!=-1 and x[i][j]==0):
        x[i][j]=d
        d=d-1
    else:
        o='U'
        j=j+1
    return i,j,x,d,o,c
def downoperation(i,j,x,d,o,c):
    i=i+1
    if(i!=c and x[i][j]==0):
        x[i][j]=d
        d=d-1
    else:
        o='L'
        i=i-1
    return i,j,x,d,o,c
def upoperation(i,j,x,d,o,c):
    i=i-1
    if(i!=-1 and x[i][j]==0):
        x[i][j]=d
        d=d-1
    else:
        o='R'
        i=i+1
    return i,j,x,d,o,c
a=int(input("enter the number :  "))
b=math.sqrt(a)
c=math.ceil(b)
x=[]
for i in range(c):
    y=[]
    for j in range(c):
        y.append(0)
    x.append(y)
flag=0
d=c*c
if(c%2==0):
    i=0
    j=0
    o='R'
    
    x[i][j]=d
    d=d-1
    while(d!=0):
        if(o=='R'):
            i,j,x,d,o,c=rightoperation(i,j,x,d,o,c)
        elif(o=='L'):
            i,j,x,d,o,c=leftoperation(i,j,x,d,o,c)    
        elif(o=='D'):
            i,j,x,d,o,c=downoperation(i,j,x,d,o,c)
        elif(o=='U'):
            i,j,x,d,o,c=upoperation(i,j,x,d,o,c)
else:
    i=c-1
    j=c-1
    o='L'
    
    x[i][j]=d
    d=d-1
    while(d!=0):
        if(o=='R'):
            i,j,x,d,o,c=rightoperation(i,j,x,d,o,c)
        elif(o=='L'):
            i,j,x,d,o,c=leftoperation(i,j,x,d,o,c)    
        elif(o=='D'):
            i,j,x,d,o,c=downoperation(i,j,x,d,o,c)
        elif(o=='U'):
            i,j,x,d,o,c=upoperation(i,j,x,d,o,c)

print("\n\n")
for i in range(c):
    print("             ",end="")
    for j in range(c):
        if(x[i][j]<=a):
            if(x[i][j]<10):
                print(x[i][j],end="  ")
            else:
                print(x[i][j],end=" ")
        else:
            print("  ",end=" ")
    print("\n")
        
        
        
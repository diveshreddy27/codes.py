n=int(input())
a=[]
while(n>0):
    a.append(n)
    n=n-1
a=list(map(str,a))
for i in range(1,len(a)+1):
    b=a.copy()
    ind=b.index(str(i))
    b[ind]="*"
    print("".join(b))
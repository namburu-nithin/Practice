a=str(input())
n=int(input())
a=a[1:(n*2)]
b=[]
j=list(a.split(","))
for i in range(n):
    j[i]=int(j[i])
print(j)
while len(j)>0:
    x=0
    for x in range(len(j)-1):
        if j[0]==j[x+1]:
            b.append(j[x+1])
    j.remove(j[0])
if len(b)==0:
    print('{-1}')
else:
    print(b)

x=int(input('enter the 1st number= '))
y=int(input('enter the 2nd number= '))
z=int(input('enter the 3rd number= '))
n=int(input('enter n= '))
i=0
j=0
k=0
l=[]
while 0<=i<=x:
    while 0<=j<=y:
        while 0<=k<=z:
            if i+j+k!=n and ([i,j,k] not in l):
                l.append([i,j,k])
            k=k+1
        k=0    
        if i+j+k!=n and ([i,j,k] not in l):
            l.append([i,j,k])
        j=j+1
    j=0    
    if i+j+k!=n and ([i,j,k] not in l):
        l.append([i,j,k])
    i=i+1
print(l)    
    
        
        
            

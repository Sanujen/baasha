w=input('Enter message: ')
n=int(input('Enter base: '))
l=len(w)
if 2<=n<=10:
    for i in range(0,l):
        t=int(ord(w[i]))
        li=[]
        while t>0:
            r=t%n
            li.append(r)
            t=t//n
        l2=li[::-1]    
        for j in l2:
            print(j,end='')
elif n==1:
    for i in range(0,l):
        t=int(ord(w[i]))
        print('1'*t,end='')
            
else:
    print('invalid base')

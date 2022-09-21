a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
def maxim(x,y,z):
    if a>b:
        if c>a:
            max=c
        else:
            max=a
    else:
        if c>b:
            max=c
        else:
            max=b
    return max
print('Maximul nr:',a,b,'si',c,'este: ',maxim(a,b,c))

def minim(x,y,z):
    if a<b:
        if c<a:
            min=c
        else:
            min=a
    else:
        if c<b:
            min=c
        else:
            min=b
    return min
print('Minimul nr:',a,b,'si',c,'este: ',minim(a,b,c))

def divizor(x,y):
    listx=[]
    listy=[]
    for i in range(1,x+1):
        if x%i==0 :
            listx.append(i)
    for k in range(1,y+1):
        if y%k==0 :
            listy.append(k)
    comun=set(listx).intersection(listy)      
    cel_mai_mare=max(comun)
    return cel_mai_mare

def divizor(x,z):
    listx=[]
    listz=[]
    for i in range(1,x+1):
        if x%i==0 :
            listx.append(i)
    for k in range(1,z+1):
        if z%k==0 :
            listz.append(k)
    comun=set(listx).intersection(listz)      
    cel_mai_mare=max(comun)
    return cel_mai_mare

def divizor(y,z):
    listy=[]
    listz=[]
    for i in range(1,y+1):
        if y%i==0 :
            listy.append(i)
    for k in range(1,z+1):
        if z%k==0 :
            listz.append(k)
    comun=set(listy).intersection(listz)      
    cel_mai_mare=max(comun)
    return cel_mai_mare

a1=divizor(a,b)
b1=divizor(a,c)
c1=divizor(b,c)

def maxim_divizorilor(a2,b2,c2):
    if a2>b2:
        if c2>a2:
            max=c2
        else:
            max=a2
    else:
        if c2>b2:
            max=c2
        else:
            max=b2
    return max
print('Cel mai mare divizor comun al celor 3 nr este: ',maxim_divizorilor(a1,b1,c1))

def multiplu(x,y):
    multiples=[]
    if(x>y):
        i=x
    if(y>x):
        i=y
    else:
        i=x
    multiple=0
    while len(multiples)<5:
        if(i%x==0 and i%y==0):
            multiples.append(i)
            i+=1
        else:
            i+=1  
    return min(multiples)

def multiplu(x,z):
    multiples=[]
    if(x>z):
        i=x
    if(z>x):
        i=z
    else:
        i=x
    multiple=0
    while len(multiples)<5:
        if(i%x==0 and i%z==0):
            multiples.append(i)
            i+=1
        else:
            i+=1  
    return min(multiples)

def multiplu(y,z):
    multiples=[]
    if(y>z):
        i=y
    if(z>y):
        i=z
    else:
        i=y
    multiple=0
    while len(multiples)<5:
        if(i%y==0 and i%z==0):
            multiples.append(i)
            i+=1
        else:
            i+=1  
    return min(multiples)

j=multiplu(a,b)
k=multiplu(a,c)
l=multiplu(b,c)
def minim(j1,k1,l1):
    if j1<k1:
        if l1<j1:
            min=l1
        else:
            min=j1
    else:
        if l1<k1:
            min=l1
        else:
            min=k1
    return min
print('Cel mai mic multiplu comun al celor 3 nr este: ',minim(j,k,l))



from math import *

def sem(n):
    a = ''
    while n!=0:
        a+=str(n%7)
        n = n//7
    return a[::-1]

def pr(n):
    a = [1,n]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if n == i**2:
                a.append(i)
            else:
                a.append(i)
                a.append(n//i)
    c = 1
    for i in range(len(a)):
        c = c*a[i]
    return c

b = []
for i in range(1,100):
    s1 = sem(i)
    if s1.count('1')==2:
        s1 = '1' + s1 + '2'
    s1 = int(s1,7)
    for j in range(1,100):
        s2 = sem(j)
        if s2.count('1')==2:
            s2 = '1' + s2 + '2'
        s2 = int(s2,7)
    R = ceil(pr(s1)/pr(s2))
    if R > 30:
        b.append(R)
print(min(b))
    
    

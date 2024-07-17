def tr(n):
    a = ''
    while n!=0:
        a+=str(n%3)
        n = n//3
    return a[::-1]
def pt(n):
    a = ''
    while n!=0:
        a+=str(n%5)
        n = n//5
    return a[::-1]
c = []
for n in range (1,10000):
    s = bin(n)[2:]
    if s.count('1')%4==0:
        s = pt(n)+s[:-2] + tr(n)
    else:
        s = tr(n) + s[2:] + '100'
    a = 0
    for i in range(len(s)):
        a+=int(s[i])
    if pt(a).count('2')<3 and tr(a).count('1')<5:
        r = int(s,5)
        if r % a == 1 and r>1000:
            c.append(r)
print(min(c))


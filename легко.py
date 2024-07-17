def pt(n):
    a = ''
    while n!=0:
        a+=str(n%5)
        n = n//5
    return a[::-1]

a = []
kol=0
for n in range (1,10000):
    s = str(n)
    s = s[::-1]
    for i in range (len(s)):
        while '0' in s[i]:
            s = s.replace('0','9')
        else:
            break
    s = pt(int(s))
    if s.count('2')>2:
        s = '2'+s+'2'
    else:
        s = '1'+s+'1'
    R = int(s,5)
    if R%1111==0:
        a.append(n)
    
        
    
print(min(a))


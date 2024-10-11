f=open('input.txt','r')
c=f.readlines()
a=list(map(int,c[0].split()))
results=0
resultpr=1
resultrz=a[0]
for i in range(len(a)):
    if c[1][0]=='+':
        results+=a[i]
    if c[1][0]=='*':
        resultpr*=a[i]
    if c[1][0]=='-':
        if i==0:
            continue
        else:
            resultrz-=a[i]
f=open('output.txt','w')
if c[1][0] == '+':
    f.write(str(results))
if c[1][0] == '*':
    f.write(str(resultpr))
if c[1][0] == '-':
    f.write(str(resultrz))






N = int(input())
s=input()
len_s=len(s)
k=len_s//N
print(k)
a=[]
s1=''
for i in range(len(s)):
    s1+=s[i]
    if (i+1)%k==0:
        a.append(s1)
        s1=''

result=''
for i in range(len(a)):
    result+=a[i][::-1]
print(result)



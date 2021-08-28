user=input("enter name:")
i=0
s=""
while i<2:
    s=s+user[i]
    i=i+1
s1=""+s
i=2
while i>=1:
    s1=s1+user[-i]
    i=i-1
print(s1)

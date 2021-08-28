s="my name is shailu"
i=0
d={}
while i<len(s):
    if s[i]=="":
        d["space"]=""
    else:
        d[i]=s[i]
    i+=1
print(d)

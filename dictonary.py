a=input("enter number:")
i=0
d={}
while i<len(a):
    d[a[i]]=i
    i=i+1
print(d)

#######################################

a=input("enter number:")
i=0
d={}
while i<len(a):
    d[a[i]]=a
    i=i+1
print(d)


###########################################

a=[1,2,3,4]
b=[]
i=0
while i<len(a):
    b.append({a[i]})
    i=i+1
print(b)



# [[1,2],[1,3],[2,3]]
    
a=[1,2,3]
b=[]
i=0
while i<len(a):
    j=i+1
    while j<len(a):
        b.append([a[i],a[j]])
        j+=1
    i+=1
print(b)
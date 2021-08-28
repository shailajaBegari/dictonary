words='w3resource'
# words="shailaja"
i=0
d={}
while i<len(words):
    j=0
    count=0
    while j<len(words):
        if words[i]==words[j]:
            count+=1
        j=j+1
    d[words[i]]=count
    i=i+1
print(d)
word="MISSISSIPPI"
i=0
d={}
while i<len(word):
    j=0
    count=0
    while j<len(word):
        if word[i]==word[j]:
            count+=1
        j=j+1
    d[word[i]]=count
    i=i+1
print(d)
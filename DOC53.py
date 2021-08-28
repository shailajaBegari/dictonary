b=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
i=0
dic={}
while i<len(b):
    j=0
    l=[]
    while j<len(b[i]):
        if b[i][j]!=b[i][0]:
            l.append(b[i][j])
        j+=1
    dic[b[i][0]]=l
    i+=1
print(dic)






# {1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}

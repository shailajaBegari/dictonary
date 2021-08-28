d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
b=[]
for  i in d.values():
    b.append(i)
i=0
b1=[]
while i<4:
    d1={}
    j=0
    for k in d:
        d1[k]=b[j][i]
        j=j+1
    b1.append(d1)
    i=i+1
print(b1)
    









# output::::::::::::::::::
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]


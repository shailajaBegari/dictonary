d={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
b=[]
k1=[]
for k , v in d.items():
    b.append(v)
    k1.append(k)
i=0
d1={}
while i<len(b):
    j=0
    b1=[]
    while j<len(b[i]):
        if b[i][j]%2==0:
            b1.append(b[i][j])
        j=j+1
    d1[k1[i]]=b1
    i=i+1
print(d1)

############################################################3

# for k in d:
#     b=[]
#     for v in d[k]:
#         if v%2==0:
#             b.append(v)
#     d[k]=b
# print(d)

###########################################################

d={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
for k in d:
    b=[]
    for v in d[k]:
        if v%2==0:
            b.append(v)
    d[k]=b
print(d)



# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
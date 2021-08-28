list=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d={}
for i in list:
    k=i[0]
    b=[]
    for j in list:
        if j[0]==k:
            b.append(j[1])
            d[k]=b
print(d)

# 2 method
d={}
i=0
while i<len(list):
    j=0
    b=[]
    while j<len(list):
        if list[i][0]==list[j][0]:
            b.append(list[j][1])
        j=j+1
    d.update({list[i][0]:b})
    i=i+1
print(d)  





# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
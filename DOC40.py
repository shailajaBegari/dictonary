a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
e=[]
d={}
i=0
while i<len(b):
    d1={}
    d1[b[i]]=c[i]
    d[a[i]]=d1
    i=i+1
e.append(d)
print(e)

    








# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'c':400}
# sum=0
# d={}
# for x in d1:
#     for y in d2:
#         if x==y:
#             d[x]=d1[x]+d2[y]
# print(d)

b=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
i=0
d=[]
for i in b:
    for j,k in i.items():
        if k not in d:
            d.append(k)
print("unique values",":",d)
 
# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():    
#     sum=sum+i
# print(sum) 


# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 300, 'd':700}
# d={}
# for x in d1:
#     if x in d2:
#         d2[x]=d1[x]+d2[x]
#     else:
#         pass
# print(d2)

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 300, 'c':700}
d={}
for x in d1.keys():
    for y in d2.keys():
        if x==y:
            d[x]=d1[x]+d2[y]
        # d[y]=d2[y]               (2method)
# d[x]=d1[x]
print(d)
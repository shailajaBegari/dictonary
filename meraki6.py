dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
d={}
for i in dic:
    if dic[i] not in d:
        d[i]=dic[i]
print(d)


# simple method
# print(dic)


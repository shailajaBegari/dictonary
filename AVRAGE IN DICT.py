# dict={1:45,3:59,7:50,"nani":60}
# k=list(dict.keys())
# v=list(dict.values())
# print(v)
# print(k)


dict={1:30,3:50,4:68,7:89,6:90}
sum=0
for x in dict.values():
    sum=sum+x
print("avrage",sum/len(dict))

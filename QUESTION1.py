list=[{"name":"kumar","cash":20},{"name":"shailu","cash":40},{"name":"kumarnayak","cash":50},{"name":"shailubujji","cash":60}]
user=input("enter a name:")
for i in list:
    n=i["name"]
    s=""
    if user in n:
        print(i)
        

        
#     while j<len(user):
#         for v in n:
#             if v==user[j]:
#                 if v not in s:
#                     s=s+v
#         j=j+1
#     if user==s:
#         print(i)
# #######################################


# sum=0
# for i in list:
#     sum=sum+i["cash"]
# print(sum)




# n=int(input("enter a num:"))
# d={}
# i=1
# k=1
# while k<=n:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c=c+1
#         j=j+1
#     if c==2:
#         d[k]=i
#         k=k+1
#     i=i+1
# print(d)



########################################################


n=int(input("enter number:"))
i=1
p=1
while 0<=n:
    j=1
    c1=0
    while j<=i:
        if i%j==0:
            c1=c1+1
        j=j+1
    if c1==2:
        if p==n:
            print(i)
            break
        p=p+1
    i=i+1
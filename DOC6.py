dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
d={}
for  i in (dic1,dic2,dic3):
    d.update(dic1)
    d.update(dic2)
    d.update(dic3)
print(d)
################################$$$$$$$$$$$$$4



user=int(input("enter number:===="))
d={}
i=1
while i<(user):
    sqaure=i*10
    d[i]=sqaure
    i=i+1
print(d) 


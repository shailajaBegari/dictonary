 
# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():    
#     sum=sum+i
# print(sum) 

# c=dict()
# for i in range(1,16):
#     d=i*i
#     c[i]=d
# print(c)  



s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
for i in (s,a):
    # c.update(s)
    s.update(a)
print(s) 
list1=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}] 
dic=[]
for x in list1:
    for y in x.values():
        if y not in dic:
            dic.append(y)
print(dic)
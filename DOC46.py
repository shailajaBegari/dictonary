list=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
a=[]
for i in list:
    d={}
    for k,v in i.items():
        d[k]=int(v)
    a.append(d)
print(a)
        
    







# String values of a given dictionary, into integer types:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
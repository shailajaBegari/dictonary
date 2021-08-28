d={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
for i in d:
    d[i]=[]
print(d)


# 2 method::::::::::::

d={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
for key, value in d.items():
    variable=value
    variable.clear()
    d[key]=variable
print(d)








# outputzz{'C1': [], 'C2': [], 'C3': []}

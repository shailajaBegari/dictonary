dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
max=0
s_m=0
t_m=0
d={}
for i in dict:
    if dict[i]>max:
        s_m=max
        max=dict[i]
    elif dict[i]>s_m:
        s_m=dict[i]
        t_m=s_m
    elif dict[i]>t_m:
        t_m=dict[i]
print(max)
print(s_m)
print(t_m)
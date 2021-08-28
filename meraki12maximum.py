dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    } 
max=0
s_m=0
t_m=0
for i,j in dict.items():
    if dict[i]>max:
        s_m=max
        max=dict[i]
    elif dict[i]>s_m:
        s_m=dict[i]
    elif dict[i]>t_m:
        t_m=s_m
        dict[i]=t_m
print(max)
print(s_m)
print(t_m)
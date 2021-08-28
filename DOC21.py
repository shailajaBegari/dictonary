list=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
empty=[]
for i in list:
    for j,k in i.items():
        if k not in empty:
            empty.append(k)
print("unqiue values:",empty)

####
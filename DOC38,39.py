# dict={'c1': 'Red', 'c2': 'Green', 'c3': None}
# dict.popitem()
# print(dict)

# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}


dict={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
d={}
for key ,value in dict.items():
    if value>=170:
        # print(key,value)
        d[key]=value
print(d)
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}


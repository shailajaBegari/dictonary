# Original Dictionary:
d={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (6.9, 75), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
for key,value in d.items():
    if value[0]>=6.0 and value[1]>=70:
        print({key:value})
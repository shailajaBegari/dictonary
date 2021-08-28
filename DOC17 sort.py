d={"shailu":3,"goutham":8,"nani":9,"rani":5}
for x in d:
    for y in d:
        if d[x]>d[y]:
            d[x],d[y]=d[y],d[x]
print(d)

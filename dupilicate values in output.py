d={"h":"red","m":"red","s":"green","k":"black","g":"green"}
s=""
for key in d:
    for value in d:
        if key==value and key!="k":
            s=key
            print(s)
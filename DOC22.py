dict= {'1':['a','b'], '2':['c','d']}
for x in dict.values():
    for y in x:
        for z in x:
            if y!=z :
                print(y+z)

########################################
dict= {'1':['a','b'], '2':['c','d']}              
for x in dict["1"]:
    for y in dict["2"]:
        print(x+y)



# xpected Output:
# ac
# ad
# bc

d={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
max=0
d1={}
for  k in d.items():
    for v in d:
        if d[v]>max:
            max=d[v]
    d1[v]=max
print(d1[v])





# ***************####################################

# def test(dictt, N):
#     result = sorted(dictt, key=dictt.get, reverse=True)[:N]
#     return result 
# dictt = {'a':5, 'b':14, 'c': 32, 'd':35, 'e':24, 'f': 100, 'g':57, 'h':8, 'i': 100}
# N=1
# print(test(dictt,N))
# N=2
# print(test(dictt, N))
# N=5
# print(test(dictt, N))



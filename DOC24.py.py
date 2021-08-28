a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# d={}
# i=0
# amt=0
# amt1=0
# while i<len(a):
#   if a[i]["item"]=="item1":
#     amt=amt+a[i]["amount"]
#   elif a[i]["item"]=="item2":
#     amt1=amt1+a[i]["amount"]
#   i+=1
# d={"item1":amt,"item2":amt1}
# print(d)


c={}
for d in a:
  if d["item"] not in c:
    c[d["item"]]=d["amount"]
  else:
    c[d["item"]]+=d["amount"]
print(c)



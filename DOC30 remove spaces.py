d={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
d1={}
for i in d:
  s=i.split()
  s=s[0]+s[1]
  d1[s]=d[i]
print(d1)




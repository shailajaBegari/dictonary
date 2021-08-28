

user=input("enter name:::")
i=0
str2=""
while i<len(user):
    if user[i]>="a" and user[i]<="z":
        str2=str2+user[i].upper()
    else:
        str2=str2+user[i].lower()
    i=i+1
print(str2)


#################################



str='MoNa'
i=0
while i<len(str):
    if ord(str[i])>=65 and ord(str[i])<=90:
        a=ord(str[i])+32
        print(chr(a),end="")
    else:
        b=ord(str[i])-32
        print(chr(b),end="")
    i+=1
    
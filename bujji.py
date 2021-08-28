user=input("enter number:")
b=list(user)
i=0
while i<len(b):
    s=b[i]
    j=0
    string=""
    while j<len(b):    
        if s[j]=="one":
            string+=1
        elif s[j]=="two":
            string+=2
        elif s[j]=="three":
            string+=3
            j=j+1
        i=i+1
    # print(string)
    sum=sum+string[j]
print(sum)
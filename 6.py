

input=open("input6.txt","r")
form=[]
temp=[]
for txt in input:
    if(txt!='\n'):
        temp.append(txt)
    else:
        
        form.append(temp)
        temp=[]

form.append(temp)

res=0
for elem1 in form:
    ans=set(elem1[0])
    for elem2 in elem1:
        ans=ans&set(elem2)
    res+=len(ans)-1  
    print(ans)

print(res+1)

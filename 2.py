import re

input=open("input2","r")
i=0
j=0
for txt in input:
    data=re.split("[-\s:+]",txt)
    minx=int(data[0])
    maxx=int(data[1])
    charx=data[2]
    password=data[4]
    numMatch=re.findall(charx,password)
    if(len(numMatch)>=minx and len(numMatch)<=maxx):
        i+=1
    if(password[minx-1]==charx):
        if(password[maxx-1]!=charx):
            j+=1
    else:
        if(password[maxx-1]==charx):
            j+=1    
print("zad1 = ",i)
print("zad2 = ",j)

input.close()
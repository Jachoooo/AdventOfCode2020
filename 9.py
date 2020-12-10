

input=open("input9.txt","r")

msg=[]
for line in input:
    
    msg.append(int(line[:-1]))




#part1
preamble=25
for i in range(preamble,len(msg)):
    curr=msg[i-preamble:i]
    flag=0
    for j in range(0,preamble):
        for k in range(0,preamble):  
            if curr[j]+curr[k]==msg[i] and j!=k:
                
                flag=1
    if not flag:
        print(msg[i])

#part2

for i in range(0,len(msg)):
    comp=msg[i]
    j=1
    while(comp<=393911906):
        comp+=msg[i+j]
        j+=1
        if comp == 393911906:
            print(min(msg[i:i+j])+max(msg[i:i+j]))
            break

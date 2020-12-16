

input=open("input14.txt","r")


memory={}
for line in input:
    if line[0:3]=="mas":
        print('mask =',line[7:-1])
        mask=line[7:-1]
        mask1=[]
        mask2=[]
        for i in range(0,len(mask)):
            if mask[i].isnumeric():
                mask1.append('0')
                mask2.append(mask[i])   
            else:
                mask1.append('1')
                mask2.append('0')
        
        ANDmask=''.join(mask1)       
        ORmask=''.join(mask2)

        ANDmask=int(ANDmask,2)
        ORmask=int(ORmask,2)
        
    elif line[0:3]=="mem":
        
        res=line.split('=')
        mem=int(res[1][1:-1])
        mem&=ANDmask
        mem|=ORmask

        addr=line.split(']')[0][4:]
        memory[addr]=mem
    

    else:
        break

print(sum(memory.values()))

    


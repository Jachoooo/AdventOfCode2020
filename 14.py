
#part1
input=open("input14.txt","r")

memory={}
for line in input:
    if line[0:3]=="mas":
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

print('Part1 result =',sum(memory.values()))
input.close()


#part2  
input=open("input14.txt","r")

memory={}
for line in input:
    if line[0:3]=="mas":
        mask=line[7:-1]
        mask1=[]
        NX=0
        for i in range(0,len(mask)):
            if mask[i]=='X':
                mask1.append('0')
                mask2.append('0')
                NX+=1 
            else:
                mask1.append(mask[i])
                mask2.append('1')
        ORmask=''.join(mask1)
        ANDmask=''.join(mask2)  

        nums=[]
        for i in range(0,pow(2,NX)):
            nums.append(bin(i)[2:])
        
    elif line[0:3]=="mem":
        
        res=line.split('=')
        mem=int(res[1][1:-1])
        
        addr=int(line.split(']')[0][4:])
        addr=addr&int(ANDmask,2)
        addr=addr|int(ORmask,2)
        
        masks=[]
        for i in range(0,pow(2,NX)):
            cnt=0
            ln=len(nums[i])
            num=nums[i]
            temp=[]
            for t in range(0,NX-ln):
                num='0'+num
            
            for j in range(0,len(mask)):
                if mask[j]=='X':
                    temp.append(num[cnt])
                    cnt+=1
                else:
                    temp.append('0')    
            masks.append(''.join(temp))
        for i in range(0,len(masks)):
            memory[addr|int(masks[i],2)]=mem
    

    else:
        break
print('Part2 result =',sum(memory.values()))
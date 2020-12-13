import math

input=open("input12.txt","r")

dirs=[]
vals=[]
for line in input:
    
    dirs.append(line[0])
    vals.append(int(line[1:-1]))

head=0
NS=0
EW=0
NSmul=0
EWmul=1

#part1
for i in range(0,len(dirs)):
    
    if dirs[i]=='N':
        NS+=vals[i]
    elif dirs[i]=='S':
        NS-=vals[i]
    elif dirs[i]=='E':
        EW+=vals[i]
    elif dirs[i]=='W':
        EW-=vals[i]
    elif dirs[i]=='L':
        head+=vals[i]
        head=head%360
        NSmul=math.sin(math.radians(head))
        EWmul=math.cos(math.radians(head))
    elif dirs[i]=='R':
        head-=vals[i]
        head=head%360
        NSmul=math.sin(math.radians(head))
        EWmul=math.cos(math.radians(head))
    elif dirs[i]=='F':
        NS+=vals[i]*NSmul
        EW+=vals[i]*EWmul
    #print(i,'x=',EW,'\ty=',NS,'head=',head,NSmul,EWmul)

print('x=',EW,'\ty=',NS,'\tRes=',round(abs(NS)+abs(EW)))    

#part 2 


NS=1
EW=10
Ship_NS=0
Ship_EW=0
temp=0
for i in range(0,len(dirs)):
    
    if dirs[i]=='N':
        NS+=vals[i]
    elif dirs[i]=='S':
        NS-=vals[i]
    elif dirs[i]=='E':
        EW+=vals[i]
    elif dirs[i]=='W':
        EW-=vals[i]
    elif dirs[i]=='R':
        if vals[i]==90:
            temp=NS
            NS=-EW
            EW=temp
        elif vals[i]==180:
            NS=-NS
            EW=-EW
        elif vals[i]==270:
            temp=NS
            NS=EW
            EW=-temp
        else:
            print('ERROR BAD INPUT!')
    elif dirs[i]=='L':
        if vals[i]==90:
            temp=NS
            NS=EW
            EW=-temp
        elif vals[i]==180:
            NS=-NS
            EW=-EW
        elif vals[i]==270:
            temp=NS
            NS=-EW
            EW=temp
        else:
            print('ERROR BAD INPUT!')
    elif dirs[i]=='F':
        Ship_NS+=NS*vals[i]
        Ship_EW+=EW*vals[i]
        #NS=(-NS)*(vals[i]-1)
        #EW=(-EW)*(vals[i]-1)
        
    
    print(i,'x=',EW,' \ty=',NS,'\t| Ship x=',Ship_EW,' \tShip y=',Ship_NS)


print('Res=',round(abs(Ship_NS)+abs(Ship_EW)))




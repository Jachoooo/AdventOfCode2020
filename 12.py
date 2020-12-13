import math

input=open("input12.txt","r")

dirs=[]
vals=[]
for line in input:
    
    dirs.append(line[0])
    vals.append(int(line[1:-1]))

print(dirs,vals)

head=0
NS=0
EW=0
NSmul=0
EWmul=1
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
    elif dirs[i]=='R':
        head-=vals[i]
        head=head%360
        NSmul=math.sin(math.radians(head))
        EWmul=math.cos(math.radians(head))
    elif dirs[i]=='F':
        NS+=vals[i]*NSmul
        EW+=vals[i]*EWmul
    print(i,'x=',EW,'\ty=',NS)

print('x=',EW,'\ty=',NS,'\tRes=',round(abs(NS)+abs(EW)))    

        





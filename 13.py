import sys
import time

input=open("input13.txt","r")

tim=int(input.readline())
sch=input.readline()
sch=sch[:-1].split(',')


mintim=sys.maxsize
busID=0
sch_int=sch[:]
for i in range(0,len(sch)):
    if sch[i]=='x':
        sch_int[i]=0
        continue        
    else:
        sch_int[i]=int(sch[i])
        res=int(sch[i])-(tim%int(sch[i]))
        if mintim>res:
            mintim=res
            busID=int(sch[i])

print('Part1 result =',mintim*busID)

start=time.thread_time()
inc=max(sch_int)
idx=sch_int.index(inc)
i=0
for j in range(0,len(sch)):
    if sch[j]=='x':
        continue
    i*=(sch_int[j]-j)

i=i-(i%inc)-idx
sch[idx]='x'

while(1):
    temp=0
    for j in range(0,len(sch)):
        if sch[j]=='x':
            continue
        tim=sch_int[j]
        if (i+j)%tim:
            temp+=(i+j)%tim
        else:    
            inc*=sch_int[j]
            sch[j]='x'
    if not i%1000:
        print((i+idx)%sch_int[idx])
    if temp:
        i+=inc
        continue
    else:
        break

print('Part2 result =',i)



    






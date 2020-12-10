
def findnumchains(fsub):
    if len(fsub)==2 or len(fsub)==1:
        return 1
    if len(fsub)==3:
        return 2
    if len(fsub)==4:
        return 4
    if len(fsub)==5:
        return 7
    return 0

input=open("input10.txt","r")


chain=[]
for line in input:
    
    chain.append(int(line[:-1]))

chain.sort()
chain.insert(0,0)
chain.append(chain[-1]+3)
print(chain)

cnt1=0
cnt2=0
cnt3=0

for i in range(0,len(chain)-1):
    if chain[i+1]-chain[i]==1:
        cnt1+=1
    elif chain[i+1]-chain[i]==3:
        cnt3+=1
    elif chain[i+1]-chain[i]==2:
        cnt2+=1

print("1 jolt diffs =",cnt1,'\t2 jolt diffs =',cnt2,'\t3 jolt diffs =',cnt3)
print("solution =",cnt1*cnt3)


#part2
subchains=[]
start=0
for i in range(0,len(chain)-1):
    if chain[i+1]-chain[i]==3:
        subchains.append(chain[start:i+1])
        start=i+1  

cnt=1
for subchain in subchains:
    cnt*=findnumchains(subchain)
print(cnt)
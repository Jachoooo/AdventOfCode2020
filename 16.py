#STOP
#this code is absolute garbage
#turn away while you still can

input=open("input16.txt","r")

rules=[]
while(1): 
    line=input.readline()
    if line=='\n':
        break
    else:
        rules.append(line.split(' ')[1].split('-')+line.split(' ')[3][:-1].split('-'))
        #rules.append(line.split(' ')[3][:-1].split('-'))
        




while(1): 
    line=input.readline()
    if line=='\n':
        break
    else:
        yourTicket=line[:-1].split(',')

Nvals=[]
valLines=[]
while(1): 
    line=input.readline()
    if line=='nearby tickets:\n':
        continue
    elif line=='\n':
        break
    else:
        line=line[:-1].split(',')
        temp=0
        temp2=0
        for num in line:
            temp2=0
            for rule in rules:
                num=int(num)
                if (((num>=int(rule[0])) and (num<=int(rule[1])))or
                    ((num>=int(rule[2])) and (num<=int(rule[3])))):
                    temp+=1    
                    break
                temp2+=1
            if temp2==len(rules):   
                Nvals.append(num)
                
        if temp>=len(line):
            valLines.append(line)
print('Part1 =',sum(Nvals))

result=[]
for i in range(0,len(valLines[0])):
    res=[]
    for p in range(0,len(rules)):
        rule=rules[p]
        
        temp=0
        for j in range(0,len(valLines)):
            num=int(valLines[j][i])
            #print(num)
            if (((num>=int(rule[0])) and (num<=int(rule[1])))or
                ((num>=int(rule[2])) and (num<=int(rule[3])))):
                temp+=1
        
        if temp==len(valLines):
            res.append(p)
    result.append(res)
  
print(result)
for j in range(0,len(rules)):    
    result_size=[len(i) for i in result]
    idx=result_size.index(min(result_size))
    val=result[idx][0]

    for i in range(0,len(result)):
        if i==idx:
            result[i].append(-1)
            result[i].append(-1)
            result[i].append(-1)
            result[i].append(-1)
            result[i].append(-1)
            print(j,'=',idx,'=',val)
        else:
            try:
                result[i].remove(val)
            except:
                pass


#salkjglsajdgl;jsvn;zsndfgb;nzdf;gnz;kfdng;kzdnfbjkfnbdf
for i in result:
    print(max(i),end=' ')
print('\n')

temp=1
for i in range(0,6):
    print(int(yourTicket[max(result[i])]))
    temp*=int(yourTicket[max(result[i])])
print('\nshitresult2imstupid=',temp)

temp=0
idx=[]
for j in range(0,6): 
    for i in result:
        if max(i)==j:
            idx.append(result.index(i))
print('\n')
temp=1
for i in range(0,6):
    temp*=int(yourTicket[idx[i]])
print('\nresult2=',temp)




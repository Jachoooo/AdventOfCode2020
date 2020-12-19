import re
import time

print("Advent of Code 2020 - Day 19\n_________________________________")
startTime=time.thread_time()
input=open("input19.txt","r")


rules={}
messages=[]
while(1):
    line=input.readline()
    if line=='\n':
        break
    line=line.split(':')
    rules[int(line[0])]=line[1][:-1]+' '
    
#print(rules)
while(1):
    line=input.readline()
    if line=='\n':
        break
    messages.append(line.strip())
#print(messages)

while(1):
    execTime=time.thread_time()
    temp=0
    for c in rules[0]:
        if c.isnumeric():
            temp+=1
    if not temp:
        break
            
    for i in rules.keys():
        line=rules[i]
        lineSplit=line.split(' ')
        #print(lineSplit)
        for c in lineSplit:
            if c.isnumeric():
                line=line.replace(' '+c+' ',' ('+rules[int(c)]+') ')
        rules[i]=line
    #print(rules)
    if time.thread_time()-execTime>0.1:
        break

rule=rules[0]
rule=rule.replace('"','')
rule=rule.replace(' ','')


result1=0
for msg in messages:
    if re.fullmatch(rule,msg):
        
        result1+=1

print('Result =',result1)



print("_________________________________\nDone in",time.thread_time()-startTime,'s')
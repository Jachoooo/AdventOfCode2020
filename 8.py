
input=open("input8.txt","r")

code=[]
for line in input:
    
    code.append(line[:-1])

acc=0
prog_counter=0

codefix=[]
#brootforcetime
for i in range(0,len(code)):
    if code[i][:3]=='nop':
        code[i]=code[i].replace('nop','jmp')  
    elif code[i][:3]=='jmp':
        code[i]=code[i].replace('jmp','nop')  

    #print(code[3] )
    codefix.append(code[:])
    #tst=codefix[i]
    #print(tst[3] )
    if code[i][:3]=='nop':
        code[i]=code[i].replace('nop','jmp')  
    elif code[i][:3]=='jmp':
        code[i]=code[i].replace('jmp','nop')
    


maxpc=0
for j in range(0,len(code)):
    code=codefix[j][:]
    i=0
    acc=0
    prog_counter=0
    #print('iter',j,code[0])
    while(1):
        i+=1
        mem=code[prog_counter]
        instruction=mem[:3]
        sign=mem[4]
        if sign=='+':
            mul=1
        else:
            mul=-1    
        value=int(mem[5:])*mul
        
        #print(i,':',prog_counter,'\t|',instruction,'\t',value,'\t|',acc)
        code[prog_counter]='stp +420'
        if instruction=='acc':
            acc+=value
            prog_counter+=1
        elif instruction=='jmp':
            prog_counter+=value
        elif instruction=='nop':
            prog_counter+=1
        else:
            break
            
    #print(codefix[i+1][0])
    
    #print('prog counter =',prog_counter,'\tacc =',acc)
    if maxpc<prog_counter:
        maxpc=prog_counter
        print('maxpc dla ',j)
        print('prog counter =',prog_counter,'\tacc =',acc)

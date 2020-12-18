import re,time

def solve(line):
    while(1):
        res=re.findall(r'\(([^(-))]+)\)',line)
        if res:
            for subeq in res:
                line=line.replace('('+subeq+')',solve(subeq))
        else:
            
            break
    
    line=line.strip()
    line=line.split(' ')
    
    a=int(line[0])
    operation='+'
    b=0
    for i in range(1,len(line)):
        if line[i].isnumeric():
            b=int(line[i])
            if operation=='+':
                a+=b
            elif operation=='*':
                a*=b
            else:
                raise Exception("Wrong operation!")
        else:
            operation=line[i]
    return str(a)


def solve2(line):
    while(1):
        res=re.findall(r'\(([^(-))]+)\)',line)
        if res:
            for subeq in res:
                line=line.replace('('+subeq+')',solve2(subeq))
        else:
            
            break
    
    line=line.strip()
    line=line.split('*')
    sums=[]
    for eq in line:
        res=0
        nums=eq.split(' ')
        for num in nums:
            if num.isnumeric():
                res+=int(num)
        sums.append(res)
    res=1
    for num in sums:
        res*=num
    
    return str(res)
    

print("Advent of Code 2020 - Day 18\n_________________________________")
startTime=time.thread_time()
input=open("input18.txt","r")

result=0
result2=0
for line in input:
    res=int(solve(line))
    #print(line[:-1],'=',res)
    result+=res

    res=int(solve2(line))
    #print(line[:-1],'=',res)
    result2+=res
    

print('Part1 result =',result)
print('Part2 result =',result2)
print('_________________________________\nDone in',
      time.thread_time()-startTime,'s')
    
    

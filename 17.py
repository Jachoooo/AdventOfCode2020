import time


#part1
def nextstep(matrix):
    res=[]
    tempx=[]
    tempy=[]
    for z in range(0,len(matrix)):
        for y in range(0,len(matrix[0])):
            for x in range(0,len(matrix[0][0])):
                tempx.append('.')
            tempy.append(tempx[:])
            tempx=[]
        res.append(tempy)
        tempy=[]
    
    for z in range(1,len(matrix)-1):
        for y in range(1,len(matrix[0])-1):
            for x in range(1,len(matrix[0])-1):
                if(matrix[z][y][x]=='#'):
                    temp=0
                    for o in range(-1,2):
                        for p in range(-1,2):
                            for k in range(-1,2):                       
                                if matrix[z+o][y+p][x+k] == '#':
                                    temp+=1
                    if temp==3 or temp==4:
                        res[z][y][x]='#'
                    else:
                        res[z][y][x]='.'

                elif(matrix[z][y][x]=='.'):
                    temp=0
                    for o in range(-1,2):
                        for p in range(-1,2):
                            for k in range(-1,2):                       
                                if matrix[z+o][y+p][x+k] == '#':
                                    temp+=1
                    if temp==3:
                        res[z][y][x]='#'
                    else:
                        res[z][y][x]='.'
                
                else:
                    return 0
    return res[:][:][:]


#part2
def nextstep2(matrix):
    res=[]
    tempx=[]
    tempy=[]
    tempz=[]
    for w in range(0,len(matrix)):
        for z in range(0,len(matrix[0])):
            for y in range(0,len(matrix[0][0])):
                for x in range(0,len(matrix[0][0][0])):
                    tempx.append('.')
                tempy.append(tempx[:])
                tempx=[]
            tempz.append(tempy)
            tempy=[]
        res.append(tempz)
        tempz=[]
    for w in range(1,len(matrix)-1):
        for z in range(1,len(matrix[0])-1):
            for y in range(1,len(matrix[0][0])-1):
                for x in range(1,len(matrix[0][0][0])-1):
                    if(matrix[w][z][y][x]=='#'):
                        temp=0
                        for o in range(-1,2):
                            for p in range(-1,2):
                                for k in range(-1,2):
                                    for l in range(-1,2):                       
                                        if matrix[w+l][z+o][y+p][x+k] == '#':
                                            temp+=1
                        if temp==3 or temp==4:
                            res[w][z][y][x]='#'
                        else:
                            res[w][z][y][x]='.'

                    elif(matrix[w][z][y][x]=='.'):
                        temp=0
                        for o in range(-1,2):
                            for p in range(-1,2):
                                for k in range(-1,2):
                                    for l in range(-1,2):                       
                                        if matrix[w+l][z+o][y+p][x+k] == '#':
                                            temp+=1
                        if temp==3:
                            res[w][z][y][x]='#'
                        else:
                            res[w][z][y][x]='.'
                    
                    else:
                        return 0
    return res[:][:][:][:]




def cntResult(M):
    temp=0
    for z in range(0,len(M)):
        for y in range(0,len(M[0])):
            for x in range(0,len(M[0])):
                if(M[z][y][x]=='#'):
                    temp+=1
    return temp

def cntResult2(M):
    temp=0
    for w in range(0,len(M)):
        for z in range(0,len(M[0])):
            for y in range(0,len(M[0][0])):
                for x in range(0,len(M[0][0])):
                    if(M[w][z][y][x]=='#'):
                        temp+=1
    return temp     


#display function
def printmat(M):
    for i in range(0,len(M[0])):
        print('_',end=' ')
    print('')
    for i in range(0,len(M)):
        for j in range(0,len(M[0])):
            print(M[i][j],end=' ')
        print('')


NO_OF_ITERATIONS = 7 #add 1 to desired no. of iterations
START_SIZE = 4

###
### -> START_SIZE = 1
###

#####
#####
##### -> START_SIZE = 2
#####
#####

input=open("input17.txt","r")

start=time.thread_time()
M3=[]
M=[]
for line in input:              #read input
    temp=[]
    for i in range(0,NO_OF_ITERATIONS+1):
        temp.append('.')
    for char in line:
        temp.append(char)
    temp=temp[:-1]
    for i in range(0,NO_OF_ITERATIONS+1):
        temp.append('.')
    M.append(temp)
temp=[]
for i in range(0,len(M[0])):    #add borders
    temp.append('.')
for i in range(0,NO_OF_ITERATIONS+1):    
    M.insert(0,temp)
    M.append(temp)
temp=[]
Mtemp=[]
for i in range(0,len(M[0])):
    temp=[]
    for j in range(0,len(M[0])):
        temp.append('.')
    Mtemp.append(temp)

M3.append(M)
for i in range(0,NO_OF_ITERATIONS+START_SIZE):
    M3.insert(0,Mtemp)
    M3.append(Mtemp)

Mp1=M3[:][:][:]

#main
for i in range(0,NO_OF_ITERATIONS-1):    
    M3=nextstep(M3) 
    print('I=',i,'res=',cntResult(M3))
input.close()  
print('Part1 done in',time.thread_time()-start,'s')



#PART2
start=time.thread_time()
M4=[]
temp=[]
Mtemp=[]
M3temp=[]
for z in range(0,len(Mp1)):
    Mtemp=[]
    for y in range(0,len(Mp1[0])):
        temp=[]
        for x in range(0,len(Mp1[0][0])):
            temp.append('.')
        Mtemp.append(temp)
    M3temp.append(Mtemp)

M4.append(Mp1)
for i in range(0,NO_OF_ITERATIONS+START_SIZE):
    M4.insert(0,M3temp)
    M4.append(M3temp)

for i in range(0,NO_OF_ITERATIONS-1):
    
       
    M4=nextstep2(M4) 
    print('I=',i,'res=',cntResult2(M4))    
input.close()
print('Part2 done in',time.thread_time()-start,'s')
import time

def nextstep(matrix):
    res=[]
    temp=[]
    
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            temp.append('.')
        res.append(temp[:])
        temp=[]
    
    
    for i in range(1,len(matrix)-1):
        for j in range(1,len(matrix[0])-1):
            if(matrix[i][j]=='L'):
                temp=0
                for o in range(-1,2):
                    for p in range(-1,2):
                        if matrix[i+o][j+p] == '#':
                            temp+=1
                if temp==0:
                    res[i][j]='#'
                else:
                    res[i][j]='L'
            elif(matrix[i][j]=='#'):
                temp=0
                for o in range(-1,2):
                    for p in range(-1,2):
                        if matrix[i+o][j+p] == '#':
                            temp+=1
                if temp>4:
                    res[i][j]='L'
                else:
                    res[i][j]='#'
            elif(matrix[i][j]=='.'):
                pass
            else:
                return 0
    return res[:][:]
    
def nextstep2(matrix):
    res=[]
    temp=[]
    
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            temp.append('.')
        res.append(temp[:])
        temp=[]
    
    
    for i in range(1,len(matrix)-1):
        for j in range(1,len(matrix[0])-1):
            if(matrix[i][j]=='L'):
               
                if checkVisibleTaken(matrix,i,j)==0:
                    res[i][j]='#'
                else:
                    res[i][j]='L'
            elif(matrix[i][j]=='#'):
                if checkVisibleTaken(matrix,i,j)>4:
                    res[i][j]='L'
                else:
                    res[i][j]='#'
            elif(matrix[i][j]=='.'):
                pass
            else:
                return 0
    return res[:][:]

def checkVisibleTaken(M,i,j):
    
    taken=0
    for Ymod in range(-1,2):
        for Xmod in range(-1,2):
            o=Ymod
            p=Xmod
            while(i+o>0 and i+o<len(M) and j+p>0 and j+p<len(M[0])):
                if Xmod==0 and Ymod==0:
                    break
                if M[i+o][j+p]=='L':
                    break
                elif M[i+o][j+p]=='#':
                    taken+=1
                    break
                else:
                    o+=Ymod
                    p+=Xmod
                    continue
    return taken





def cntResult(M):
    temp=0
    for i in range(1,len(M)-1):
        for j in range(1,len(M[0])-1):
            if(M[i][j]=='#'):
                temp+=1
    return temp    


def printmat(M):
    for i in range(0,len(M[0])):
        print('_',end=' ')
    print('')
    for i in range(0,len(M)):
        for j in range(0,len(M[0])):
            print(M[i][j],end=' ')
        print('')



#input=open("test.txt","r")
input=open("input11.txt","r")
M=[]
for line in input:
    temp=['.']
    for char in line:
        temp.append(char)
    temp=temp[:-1]
    temp.append('.')
    M.append(temp)


temp=[]
for i in range(0,len(M[0])):
    temp.append('.')
M.insert(0,temp)
M.append(temp)


M1=M[:][:]
M2=M[:][:]

while(1):
    
    M2=nextstep2(M1)
    
    #printmat(M2)
    if M1==M2:
        break
    M1=M2[:][:]
    print('No. of full seats =',cntResult(M1))
    #time.sleep(1)
    

#print('No. of full seats =',cntResult(M1))
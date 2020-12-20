import re
import time
import copy

class Tile(object):
    
    def __init__(self, name, mat):
        self.neighbors=[]
        self.x=-1
        self.y=-1
        self.location=''
        self.name=name[5:-1]
        self.mat=mat
        self.numbers=[]
        self.numbersValid=[]
        self.aligned=0
        self.nbrsValid={}
        temp1=''
        temp2=''
        for c in mat[0]:
            if c=='#':
                temp1=temp1+'1'
                temp2='1'+temp2
            else:
                temp1=temp1+'0'
                temp2='0'+temp2
        self.numbers.append(int(temp1,2))
        self.numbersValid.append(int(temp1,2))     
        self.numbers.append(int(temp2,2)) 
        temp1=''
        temp2=''
        for c in mat[-1]:
            if c=='#':
                temp1=temp1+'1'
                temp2='1'+temp2
            else:
                temp1=temp1+'0'
                temp2='0'+temp2
        self.numbers.append(int(temp1,2))
        self.numbersValid.append(int(temp1,2))    
        self.numbers.append(int(temp2,2)) 
        temp1=''
        temp2=''
        for c in mat:
            if c[0]=='#':
                temp1=temp1+'1'
                temp2='1'+temp2
            else:
                temp1=temp1+'0'
                temp2='0'+temp2
        self.numbers.append(int(temp1,2))
        self.numbersValid.append(int(temp1,2))    
        self.numbers.append(int(temp2,2)) 
        temp1=''
        temp2=''
        for c in mat:
            if c[-1]=='#':
                temp1=temp1+'1'
                temp2='1'+temp2
            else:
                temp1=temp1+'0'
                temp2='0'+temp2
        self.numbers.append(int(temp1,2))
        self.numbersValid.append(int(temp1,2))    
        self.numbers.append(int(temp2,2)) 

    def updatevalidnums(self):
        self.numbersValid=[]
        temp1=''
        temp2=''
        for c in self.mat[0]:
            if c=='#':
                temp1=temp1+'1'
                temp2='1'+temp2
            else:
                temp1=temp1+'0'
                temp2='0'+temp2
        
        self.numbersValid.append(int(temp1,2))     
        
        temp1=''
        temp2=''
        for c in self.mat[-1]:
            if c=='#':
                temp1=temp1+'1'
                temp2='1'+temp2
            else:
                temp1=temp1+'0'
                temp2='0'+temp2
       
        self.numbersValid.append(int(temp1,2))    
        
        temp1=''
        temp2=''
        for c in self.mat:
            if c[0]=='#':
                temp1=temp1+'1'
                temp2='1'+temp2
            else:
                temp1=temp1+'0'
                temp2='0'+temp2
        
        self.numbersValid.append(int(temp1,2))    
        
        temp1=''
        temp2=''
        for c in self.mat:
            if c[-1]=='#':
                temp1=temp1+'1'
                temp2='1'+temp2
            else:
                temp1=temp1+'0'
                temp2='0'+temp2
        
        self.numbersValid.append(int(temp1,2))    
         
    def flip(self):
        temp=[]
        for i in range(0,10):
            temp.append(self.mat[9-i])
        self.mat=temp[:]
        self.updatevalidnums()

    def rotate90(self):
        self.mat=[[self.mat[j][i] for j in range(len(self.mat))] for i in range(len(self.mat[0])-1,-1,-1)]
        self.updatevalidnums()

    def addngbr(self,nbr):

        try:
            self.neighbors.index(nbr)
        except:
            self.neighbors.append(nbr)

    def checkvalidnbr(self,nbr):
        if self.numbersValid[0]==nbr.numbersValid[1]:
            self.nbrsValid['TOP']=nbr.name
            nbr.addvalidnbr('BOTTOM',self.name)
            return True
            
        if self.numbersValid[1]==nbr.numbersValid[0]:
            self.nbrsValid['BOTTOM']=nbr.name
            nbr.addvalidnbr('TOP',self.name)
            return True
        if self.numbersValid[2]==nbr.numbersValid[3]:
            self.nbrsValid['LEFT']=nbr.name
            nbr.addvalidnbr('RIGHT',self.name)
            return True
        if self.numbersValid[3]==nbr.numbersValid[2]:
            self.nbrsValid['RIGHT']=nbr.name
            nbr.addvalidnbr('LEFT',self.name)
            return True            
        return False
    def setalligned(self):
        self.aligned=1
        #print(self.name,'is alligned')

    def addvalidnbr(self,side,name):
        self.nbrsValid[side]=name

def checkalltiles(tiles):
    ret=0
    for tile1 in tiles:
        matches=0
        for tile2 in tiles:
            if tile1.name==tile2.name:
                continue
            for num1 in tile1.numbersValid:
                for num2 in tile2.numbersValid:
                    if num1==num2:
                        matches+=1
        
        if int(matches)==2 and tile1.location=='corner':
            ret+=1
            print(tile1.name,'OK')
        elif int(matches)==3 and tile1.location=='side':
            ret+=1
            print(tile1.name,'OK')        
        elif int(matches)==4 and tile1.location=='center':
            ret+=1
            print(tile1.name,'OK')
        else:
            print('Problem with tile',tile1.name)
            return False  
    return ret==len(tiles)

def allignnbrs(tile1,tiles):
    ret=[]
    for nbr in tile1.neighbors:
        for tile2 in tiles:
            if tile2.name!=nbr or tile1.name==tile2.name:
                continue
            if tile2.aligned==1:
                continue
            while(1):
                if tile1.checkvalidnbr(tile2):
                    break
                tile2.flip()
                if tile1.checkvalidnbr(tile2):
                    break
                tile2.flip()
                tile2.rotate90() 
            tile2.setalligned()
            allignnbrs(tile2,tiles)

def flipmap(mat):
    temp=[]
    for i in range(0,len(mat)):
        temp.append(mat[len(mat)-1-i])
    mat=temp[:]
    return mat[:]
        

def rotate90map(mat):
    mat=[[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0])-1,-1,-1)]
    return mat[:]    

def findmonster(fullMap,monster):

    count=0
    for x in range(0,len(fullMap)-len(monster[0])):
        for y in range(0,len(fullMap)-len(monster)):
            cnt=0
            for x2 in range(0,len(monster[0])):
                for y2 in range(0,len(monster)):
                    if fullMap[y+y2][x+x2]=='#' and monster[y2][x2]=='#':
                        cnt+=1
            if cnt==15:
                count+=1
                for x2 in range(0,len(monster[0])):
                    for y2 in range(0,len(monster)):
                        if monster[y2][x2]=='#':
                            fullMap[y+y2][x+x2]='O'
    return count,fullMap[:]

def printmap(fullMap):
    res=0
    for y in range(0,len(fullMap)):
        for x in range(0,len(fullMap)): 
            #print(fullMap[y][x],end=' ')
            if fullMap[y][x]=='#':
                res+=1
        #print('')

    return res


#INPUT_SIZE=9
#INPUT_SIZE_RT=3
#input=open("test.txt","r")
INPUT_SIZE=144
INPUT_SIZE_RT=12
input=open("input20.txt","r")


print("Advent of Code 2020 - Day 20\n_________________________________")
startTime=time.thread_time()


tiles=[]
for i in range(0,INPUT_SIZE):
    name=input.readline().strip()
    mat=[]
    for j in range(0,10):
        mat.append(input.readline().strip())
    input.readline()
    tiles.append(Tile(name,mat))

#debug zone

testTile1=tiles[0]
testTile2=copy.copy(tiles[0])
testTile2.rotate90()
#print(testTile1.numbersValid,testTile2.numbersValid)



#debug zone
corners=1
for tile1 in tiles:
    matches=0
    for tile2 in tiles:
        if tile1.name==tile2.name:
            continue
        for num1 in tile1.numbers:
            for num2 in tile2.numbers:
                if num1==num2:
                    #print('Possible match:',tile1.name,'+',
                    #tile2.name,' value=',num1)
                    matches+=1
                    tile1.addngbr(tile2.name)
    #print(tile1.name,'\t',int(matches/2),'possible matches')
    if int(matches/2)==2:
        corners*=int(tile1.name)
        tile1.location='corner'
    elif int(matches/2)==3:
        tile1.location='side'        
    elif int(matches/2)==4:
        tile1.location='center'
    
print('Part1 result =',corners)

#print(checkalltiles(tiles))


tiles[0].setalligned()
allignnbrs(tiles[0],tiles)




#print(checkalltiles(tiles))
#print('---------------\n')
for tile1 in tiles:
    for nbr in tile1.neighbors:
        for tile2 in tiles:
            if tile2.name!=nbr or tile1.name==tile2.name:
                continue

            tile1.checkvalidnbr(tile2)    

startIDX=-1
for i,tile1 in enumerate(tiles):
    keys=list(tile1.nbrsValid.keys())
    if(keys==['RIGHT', 'BOTTOM'] or keys==['BOTTOM','RIGHT']):
        startIDX=i


IDmap=[]
temp=[]

for i in range(0,INPUT_SIZE_RT):
    temp=[]
    for j in range(0,INPUT_SIZE_RT): 
        temp.append(-1)
    IDmap.append(temp)
IDmap[0][0]=startIDX
curr=startIDX
nxt=0
for y in range(0,INPUT_SIZE_RT):
    for x in range(1,INPUT_SIZE_RT):
        for j,tile1 in enumerate(tiles):
            try:
                if(tile1.name==tiles[curr].nbrsValid['RIGHT']):
                    curr=j
                    IDmap[y][x]=j
                    break
                    
            except:
                continue
    for j,tile1 in enumerate(tiles):
        try:
            if tile1.name==tiles[IDmap[y][0]].nbrsValid['BOTTOM']:
                IDmap[y+1][0]=j
                curr=j
        except:
            continue




fullMap=[]
temp=[]
for y in range(0,INPUT_SIZE_RT):
    for yMAT in range(1,9):
        for x in range(0,INPUT_SIZE_RT):
            for xMAT in range(1,9):
                temp.append(tiles[IDmap[y][x]].mat[yMAT][xMAT])
        fullMap.append(temp)
        temp=[]



#print('---------------------------------------------------------------')

monster=[]
temp=[]
for elem in '                  # ':
    temp.append(elem)
monster.append(temp)
temp=[]
for elem in '#    ##    ##    ###':
    temp.append(elem)
monster.append(temp)
temp=[]
for elem in ' #  #  #  #  #  #   ':
    temp.append(elem)
monster.append(temp)


results=[]
numHash=[]

fullMap1=copy.deepcopy(fullMap)
count,fullMap1 = findmonster(fullMap1[:],monster)
res=printmap(fullMap1)
#print('found',count)
results.append(count)
numHash.append(res)

fullMap=flipmap(fullMap)

fullMap1=copy.deepcopy(fullMap)
count,fullMap2 = findmonster(fullMap1[:],monster)
res=printmap(fullMap1)
#print('found',count)
results.append(count)
numHash.append(res)

fullMap=flipmap(fullMap) 
fullMap=rotate90map(fullMap)

fullMap1=copy.deepcopy(fullMap)
count,fullMap1 = findmonster(fullMap1[:],monster)
res=printmap(fullMap1)
#print('found',count)
results.append(count)
numHash.append(res)

fullMap=flipmap(fullMap)

fullMap1=copy.deepcopy(fullMap)
count,fullMap2 = findmonster(fullMap1[:],monster)
res=printmap(fullMap1)
#print('found',count)
results.append(count)
numHash.append(res)

fullMap=flipmap(fullMap) 
fullMap=rotate90map(fullMap)

fullMap1=copy.deepcopy(fullMap)
count,fullMap1 = findmonster(fullMap1[:],monster)
res=printmap(fullMap1)
#print('found',count)
results.append(count)
numHash.append(res)

fullMap=flipmap(fullMap)

fullMap1=copy.deepcopy(fullMap)
count,fullMap2 = findmonster(fullMap1[:],monster)
res=printmap(fullMap1)
#print('found',count)
results.append(count)
numHash.append(res)

fullMap=flipmap(fullMap) 
fullMap=rotate90map(fullMap)

fullMap1=copy.deepcopy(fullMap)
count,fullMap1 = findmonster(fullMap1[:],monster)
res=printmap(fullMap1)
#print('found',count)
results.append(count)
numHash.append(res)

fullMap=flipmap(fullMap)

fullMap1=copy.deepcopy(fullMap)
count,fullMap2 = findmonster(fullMap1[:],monster)
res=printmap(fullMap1)
#print('found',count)
results.append(count)
numHash.append(res)

fullMap=flipmap(fullMap) 
fullMap=rotate90map(fullMap)


#print(results)
#print(numHash)

print('Part2 result =',min(numHash))
print("_________________________________\nDone in",
      time.thread_time()-startTime,'s')
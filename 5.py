def binToDec(binNum):
    decNum = 0
    power = 0
    while binNum>0:
        decNum += 2 **power* (binNum%10)
        binNum //=10
        power += 1
    return decNum

input=open("input5.txt","r")
text=input.read()
text=text.split('\n')
i=0
maxid=0
seatmap=[]
for i in range(0,1024):
    seatmap.append(".")                                                

for BP in text:
    i+=1
    print(i,BP,end=' | ')
    col=BP[7:]
    row=BP[:7]
    col=col.replace('R','1')
    col=col.replace('L','0')
    row=row.replace('B','1')
    row=row.replace('F','0')
    row=binToDec(int(row))
    col=binToDec(int(col))
    id=row*8+col
    print(row,col,end=" | ")
    print(id)
    if id>maxid:
        maxid=id
    seatmap[id]='X'
print("MaxId = ",maxid)

for i in range(1,1023):
    if seatmap[i-1]=='X'and seatmap[i]=='.'and seatmap[i+1]=='X':
        print("ID = ",i)
input.close()
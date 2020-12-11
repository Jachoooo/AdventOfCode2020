import re

input=open("input3.txt","r")
slope=[]
for txt in input:
    slope.append(txt[:-1])



j=0
x_mul=3
y_mul=1
for y in range(0,int(((len(slope)/y_mul)-1))):
    y*=y_mul
    x=int((y*x_mul)%len(slope[0]))
    test_str=slope[y][x]
    if test_str=='#':
        j+=1
        slope[y]=slope[y][:x]+"X"+slope[y][x+1:]
    else:
        slope[y]=slope[y][:x]+"O"+slope[y][x+1:]

print(j)
print(148*50*53*64*29)
input.close()
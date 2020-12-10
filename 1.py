

input=open("input1.txt","r")
n=[]
for x in input:
    n.append(int(x))
for x in n:
    for y in n:
        for z in n:
            if x+y+z==2020:
                print(x*y*z)
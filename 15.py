
#part1
input=open("test.txt","r")

memory={}
nums=input.read()[:-1].split(',')
print(nums)
nxt=0
last=0
for i in range(0,30000000-1):
    if i<len(nums):
        memory[nums[i]]=i
        nxt='0'
        #print(i+1,'->',nums[i],' next =','0')
    else:
        try:
            last=memory[nxt]
            memory[nxt]=i
            #print(i+1,'->',nxt,end='  ')
            nxt=str(i-last)
            #print('next =',nxt)
        except:
            memory[nxt]=i
            #print(i+1,'->',nxt,' next =','0')
            nxt='0'
    if not i%300000:
       print(i/300000,'%')

print('part2 =',nxt)
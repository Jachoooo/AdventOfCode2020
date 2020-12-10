
def checkForTarget(target, insideBags):
    for child in insideBags:
        if child == target:
            return True
        if checkForTarget(target, rules[child]):
            return True
    return False

def countInside(insideBags):
    if insideBags == {}:
        return 0
    total = 0
    for insideBagName in insideBags:
        total += ((countInside(rules[insideBagName]) + 1) * insideBags[insideBagName])
    return total


input=open("input7.txt","r")

rules={}
for line in input:
    
    words=line.split()
    key=words[0] + words[1]
    rules[key]={}
    for i in range(0,len(words)):
        if words[i].isnumeric():
            subkey = words[i+1]+words[i + 2]
            rules[key][subkey]=int(words[i])

answer=[]
target = 'shinygold'

for bag in rules:
    if checkForTarget(target, rules[bag]):
        answer.append(bag)
    

print(rules)
        
print("1 =", len(answer))
print("2 =", countInside(rules[target]))    

input.close()

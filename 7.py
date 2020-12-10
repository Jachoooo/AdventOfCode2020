
def containsTargetBag(targetName, insideBags):
    for child in insideBags:
        if child == targetName:
            return True
        if containsTargetBag(targetName, rules[child]):
            return True
    return False

def countInsideBags(insideBags):
    if insideBags == {}:
        return 0
    total = 0
    for insideBagName in insideBags:
        total += ((countInsideBags(rules[insideBagName]) + 1) * insideBags[insideBagName])
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
targetName = 'shinygold'

for bag in rules:
    if containsTargetBag(targetName, rules[bag]):
        answer.append(bag)
    

print(rules)
        
print("SUM Parents of {}\t\t".format(targetName), len(answer))
print("TOTAL INSIDE bags of {}\t\t".format(targetName), countInsideBags(rules[targetName]))    

input.close()

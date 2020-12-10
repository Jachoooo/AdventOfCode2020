import re

input=open("input4.txt","r")
passport=[]
temp=''
for txt in input:
    if(txt!='\n'):
        temp+=txt
    else:
        temp=temp.replace("\n"," ")
        passport.append(temp)
        temp=''
temp=temp.replace("\n"," ")
passport.append(temp)
j=0
for i in range(0,(len(passport))):
    print(passport[i])    
    if re.search('byr:',passport[i]):
        res=re.search('byr:',passport[i])
        idx=res.regs[0][1]
        year=int(passport[i][idx:idx+5])
        if(year>=1920 and year<=2002):
            print('byr:',year,end=" | ")

#ok#########################################################################
            if re.search('iyr:',passport[i]):
                res=re.search('iyr:',passport[i])
                idx=res.regs[0][1]
                year=int(passport[i][idx:idx+5])
                if(year>=2010 and year<=2020):
                    print('iyr:',year,end=" | ")

#ok#########################################################################
                    if re.search('eyr:',passport[i]):
                        res=re.search('eyr:',passport[i])
                        idx=res.regs[0][1]
                        year=int(passport[i][idx:idx+5])
                        if(year>=2020 and year<=2030):
                            print('eyr:',year,end=" | ")

##########################################################################
                            if re.search(r'hgt:\d\d\dcm|hgt:\d\din',passport[i]):
                                res=re.search(r'hgt:(\d\d\d)(cm)|hgt:(\d\d)(in)',passport[i])
                                res2=re.search(r'hgt:\d\d\d(cm)|hgt:\d\d(in)',passport[i])
                                res=res.groups()
                                
                                if res[1]=='cm':
                                    if int(res[0])>=150 and int(res[0])<=193:
                                        print('hgt:',res[0],'cm',end=" | ")
                                    else:
                                        print('\nINVALID hgt\n')
                                        continue
                                else:
                                    if int(res[2])>=59 and int(res[2])<=76:
                                        print('hgt:',res[2],'in',end=" | ")
                                    else:
                                        print('\nINVALID hgt\n')
                                        continue



                                
#ok#########################################################################                               
                                if re.search(r'(hcl:#[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9])',passport[i]):
                                    res=re.search(r'(hcl:#[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9])',passport[i])
                                    print(res.group(1),end=" | ")
#ok#########################################################################                                    
                                    if re.search(r'(ecl:amb\s|ecl:blu\s|ecl:brn\s|ecl:gry\s|ecl:grn\s|ecl:hzl\s|ecl:oth\s)',passport[i]):
                                        res=re.search(r'(ecl:amb|ecl:blu|ecl:brn|ecl:gry|ecl:grn|ecl:hzl|ecl:oth)',passport[i])
                                        print(res.group(1),end=" | ")
#ok#########################################################################                                        
                                        if re.search(r'pid:\d\d\d\d\d\d\d\d\d\s',passport[i]):
                                            res=re.search(r'pid:\d\d\d\d\d\d\d\d\d\s',passport[i])
                                            idx=res.regs[0][0]
                                            print(passport[i][idx:idx+13])
                                            j+=1
                                            #print("[",i+1,"]"," VALID  - ",passport[i])
                                            print('VALID\n')
                                            continue
        #print("[",i+1,"]","INVALID - ",passport[i])
        print('\nINVALID\n')

print(j,' of ',len(passport))

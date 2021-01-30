import sys

def getInput():
    fields = []
    field = {}
    for x in [x.split() for x in sys.stdin]:
        if x == []:
                fields.append(field)
                field = {}
        else:
            for y in x:
                field[y.split(':')[0]] = y.split(':')[1]
    fields.append(field)
    print(sol(fields))
                
def sol(fields):
    valid = 0
    units = {'in':(59,77),'cm':(150,194)}
    colors = {'amb','blu','gry','grn','hzl','oth','brn'}
    for field in fields:
        if len(field) == 8 or (len(field) == 7 and 'cid' not in field.keys()): 
            if len(field.get('byr')) == 4 and len(field.get('eyr')) == 4 and len(field.get('iyr')) == 4:
                if (1920 <= int(field.get('byr')) <= 2002) and (2020 <= int(field.get('eyr')) <= 2030) and (2010 <= int(field.get('iyr')) <= 2020):
                    if (field.get('hgt')[-2:] in units.keys()) and (field.get('ecl') in colors):
                        if int(field.get('hgt')[:-2]) in range(*units.get(field.get('hgt')[-2:])):
                            if verifyHair(field.get('hcl')):
                                if len(field.get('pid')) == 9:
                                    valid += 1
    return valid

def verifyHair(str):
    if len(str) != 7 or str[0] != '#':
        return False
    for x in str: 
        if x not in {'#','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}:
            return False
    return True

getInput()

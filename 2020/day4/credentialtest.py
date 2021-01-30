def testByr(byr):
    if len(byr) == 4 and (1920 <= int(byr) <= 2002):
        return True
    return False

def testHgt(hgt):
    units = {'in':(59,77),'cm':(150,194)}
    if hgt[-2:] in units.keys():
        if int(hgt[:-2]) in range(*units.get(hgt[-2:])):
            return True
    return False

def testHcl(hcl):
    if verifyHair(hcl):
        return True
    return False

def testEcl(ecl):
    if ecl in {'amb','blu','gry','grn','hzl','oth','brn'}:
        return True
    return False

def testPid(pid):
    pass

def verifyHair(str):
    if len(str) != 7 or str[0] != '#':
        return False
    for x in str:
        if x not in {'#','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}:
            return False
    return True

assert(testByr('2002')) == True
assert(testHgt('60in')) == True
assert(testHgt('190cm')) == True
assert(testHgt('190in')) == False 
assert(testHcl('#123abc')) == True 
assert(testHcl('#123abz')) == False
assert(testHcl('123abc')) == False
assert(testEcl('brn')) == True
assert(testEcl('wat')) == False



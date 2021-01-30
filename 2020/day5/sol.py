import sys

def main():
    CODES = [''.join(x.split()) for x in sys.stdin]
    ids = []

    for code in CODES:
        if len(code) == 10:
            row = locate(code[:-3],0,(0,127),6)
            column = locate(code[-3:],0,(0,7),3)
            ids.append(row * 8 + column) 
    print(sorted(ids))
    for x in range(1,len(ids),1):
        if (sorted(ids)[x] - sorted(ids)[x-1]) != 1:
            print(sorted(ids)[x]-1)

def locate(code,level,scope,end):
    if level == end:
        if code[-1] == 'F' or code[-1] == 'L':
                return scope[0]
        return scope[1]

    elif code[level] == 'F' or code[level] == 'L':
        return locate(code,level+1,(scope[0],int((scope[1] + scope[0]) / 2)),end)
    else:
        return locate(code,level+1,(int((scope[1] + scope[0]) / 2) + 1, scope[1]),end) 

main()




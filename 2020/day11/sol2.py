import sys, copy, functools
@functools.lru_cache(maxsize=1000)
def main():
    arr = [list(x.strip()) for x in sys.stdin]
    for x in arr:
        print(len(x))
    counted = 0
    for x in solve(arr):
        counted += x.count('#')
    print(counted)

def solve(arr):
    aux = None
    while aux != arr:
        aux = copy.deepcopy(arr)
        for x in range(len(arr)):
            for y in range(len(arr[x])):
                    occupied = 0
                    for z in findAdjacents(aux,x,y):
                        p2 = (z[0]-x,z[1]-y)
                        if recurse(aux,(x+p2[0],y+p2[1]),p2):
                            occupied += 1
                    if aux[x][y] == 'L':
                        if not occupied:
                            arr[x][y] = '#'
                    elif aux[x][y] == '#':
                        if occupied >= 5:
                            arr[x][y] = 'L'
    return arr

def recurse(arr,p1,p2):
    if p1[0] not in range(len(arr)) or p1[1] not in range(len(arr[0])):
            return  
    if arr[p1[0]][p1[1]] == '#':
        return True
    elif arr[p1[0]][p1[1]] == 'L':
        return 
    p1 = (p1[0]+p2[0],p1[1]+p2[1])
    return recurse(arr,p1,p2)

        

def findAdjacents(arr,x,y):
    if  (0 < x < (len(arr)-1)) and (0 < y < (len(arr[x])-1)):
        return [(x,y-1),(x,y+1),(x-1,y),(x+1,y),(x-1,y-1),(x-1,y+1),(x+1,y+1),(x+1,y-1)]
    else:
        if y == 0:
            if x == 0:
                return [(x,y+1),(x+1,y),(x+1,y+1)]
            elif x == len(arr)-1:
                return [(x,y-1),(x-1,y),(x-1,y-1)]
            else:
                return [(x-1,y),(x+1,y),(x,y+1),(x-1,y+1),(x+1,y+1)]
        if y == len(arr[x])-1:
            if x == 0:
                return [(x,y-1),(x+1,y),(x+1,y-1)]
                
            elif x == len(arr)-1:
                return [(x-1,y),(x,y-1),(x-1,y-1)]
            else:
                return [(x,y-1),(x+1,y),(x-1,y),(x-1,y-1),(x+1,y-1)]
        else:
            if x == 0:
                return [(x+1,y),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y+1)]
            else:
                return [(x,y-1),(x,y+1),(x-1,y),(x-1,y-1),(x-1,y+1)]
main()

            


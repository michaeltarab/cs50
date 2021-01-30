import sys, copy
def main():
    arr = [list(x.strip()) for x in sys.stdin]
    new_arr = solve(arr)
    counted = 0
    for x in new_arr:
        counted += x.count('#')
    print(counted)

def solve(arr):
    aux = None
    while aux != arr:
        aux = copy.deepcopy(arr)
        for x in range(len(arr)):
            for y in range(len(arr[x])):
                if aux[x][y] == 'L':
                    print(x,y)
                    occupied = False
                    for z in findAdjacents(aux,x,y):
                        print(z)
                        if aux[z[0]][z[1]] == '#':
                            occupied = True
                    if not occupied:
                        arr[x][y] = '#'
                elif aux[x][y] == '#':
                    occupied = 0
                    for z in findAdjacents(aux,x,y):
                        if aux[z[0]][z[1]] == '#':
                            occupied += 1
                    if occupied >= 4:
                        arr[x][y] = 'L'
    return arr

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
            


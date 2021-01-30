import sys,math 
def main():
    arr = [0] + sorted([int(x.rstrip()) for x in sys.stdin]) 
    arr.append(max(arr) + 3)
    indices = countRemovable(arr)
    distinct = flawPermutations(indices)
    print(findPermutations(arr,indices,distinct))


def countRemovable(arr):
    indices = []
    for x in range(2,len(arr),1):
        if (arr[x] - arr[x-2]) in range(1,4):
            indices.append(arr[x] - 1)
    return sorted(indices)

def flawPermutations(indices):
    distinct = 0
    for x in range(2,len(indices),1):
        if (indices[x] - indices[x-1]) + (indices[x] - indices[x-2]) == 3:
            distinct += 1
    return distinct


def findPermutations(arr,indices,distinct):
    perms = 1
    for x in range(len(indices)-(distinct*3),0,-1):
        perms +=  math.comb(len(indices)-(distinct*3),x)
    for x in range(distinct):
        perms += perms * 6
    return perms



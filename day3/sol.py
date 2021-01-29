import sys

def main():
    arr = [''.join(x.split()) for x in sys.stdin]
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    trees = [0 for trees in range(5)]
    product = 1
    for count,x in enumerate(slopes): 
        i = x[1]
        j = x[0]
        while i < len(arr):
            if  j > len(arr[i])-1: 
                print(i,x)
                j = (j - (len(arr[i])-1)) - 1
            else:
                print(x,i)
                if arr[i][j] == '#': 
                    trees[count] += 1 
                i += x[1]
                j += x[0]
    for x in trees:
        product *= x
    return product

print(main())

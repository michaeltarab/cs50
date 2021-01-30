import sys, quicksort, binarysearch
def main():
    arr = [int(''.join(x.split())) for x in sys.stdin]
    arr.pop()
    return sol(quicksort.sort(arr,0,len(arr)-1))

def sol(arr):
    for count,x in enumerate(arr):
        for y in arr[:count-1]:
            if binarysearch.search(arr[:count-1],(2020-x)-y):
                return x * y * ((2020-x)-y)
print(main())
#go through sorted arr for x 
#go through sorted(arr) for y excluding values equal and above that 2020-x 
#binary search (2020-x)-y






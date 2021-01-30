import sys

def main():
    arr = [0] + sorted([int(x.rstrip()) for x in sys.stdin])
    print(countDifferences(arr))

def countDifferences(arr):
    differences  = {1:0,2:0,3:1}
    for x in range(1,len(arr),1):
        if (arr[x] - arr[x-1]) in range(1,4):
            print(arr[x],arr[x-1])
            differences[(arr[x] - arr[x-1])] += 1

    return sum(differences.values())
    #return (differences[1] * differences[3])
main()

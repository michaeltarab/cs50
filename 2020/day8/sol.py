import sys

def main():
    arr = [x.rstrip() for x in sys.stdin]
    print(accumulate(arr,0,set()))

def accumulate(arr,mark,seen):
    print(seen)
    if mark in seen:
        print(mark)
        return 0
    seen.add(mark)
    if arr[mark][0] == 'j':
        return accumulate(arr,mark + int(arr[mark].split()[1]),seen)
    elif arr[mark][0] == 'a':
        return int(arr[mark].split()[1]) + accumulate(arr,mark+1,seen) 
    else:
        return accumulate(arr,mark+1,seen)

def accumulate2(arr):
    print(arr)
    mark = 0
    seen = set()
    accumulated = 0
    while mark not in seen:
        seen.add(mark)
        if arr[mark][0] == 'j':
            mark += int(arr[mark].split()[1])
        else:
            if arr[mark][0] == 'a':
                accumulated += int(arr[mark].split()[1])
            mark += 1
    return accumulated

main()

    



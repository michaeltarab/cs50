import sys

def main():
    arr = [x.rstrip() for x in sys.stdin]  
    jumps = [count for count,x in enumerate(arr) if x[0] == 'j']
    print(accumulate(arr,jumps))

def accumulate(arr,jumps):
    for jump_index in jumps:
        accumulated = 0
        aux = arr.copy()
        aux[jump_index] = 'nop +0'
        seen = set()
        mark = 0
        while mark not in seen:
            seen.add(mark)
            if mark == len(aux) - 1:
                if aux[mark][0] == 'a':
                    accumulated += int(aux[mark].split()[1])
                return accumulated
            elif aux[mark][0] == 'j':
                mark += int(aux[mark].split()[1])
            else:
                if aux[mark][0] == 'a':
                    accumulated += int(aux[mark].split()[1])
                mark += 1

main()


    



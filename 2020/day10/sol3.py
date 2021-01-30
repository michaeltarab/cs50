import sys,functools 
lines = [0] + [int(line.strip()) for line in sys.stdin.readlines()]
lines.sort()
lines.append(lines[-1] + 3)

@functools.lru_cache(maxsize=None) # memoize
def count(start): # calculate num adapter chains starting at lines[start]
    # end of adapter
    if start == len(lines) - 1:
        return 1

    num = 0
    for i in range(start + 1, len(lines)):
        diff = lines[i] - lines[start]
        if 1 <= diff <= 3:
            num += count(i)
        elif diff > 3:
            break

    return num

print(count(0))

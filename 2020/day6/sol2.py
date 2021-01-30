import sys

def main():
    arr = [''.join(x.split()) for x in sys.stdin]
    print(arr)
    print(tally(arr))

def tally(arr):
    scores = 0
    letters = {}
    count = 0
    for step,x in enumerate(arr):
        if x != '':
            count += 1
            for y in x:
                if y not in letters.keys():
                    letters[y] = 1
                else:
                    letters[y] += 1
        if x == '' or step == len(arr)-1:
            for y in letters.values():
                if y == count: 
                    scores += 1
            count = 0
            letters = {}
    return scores
main()

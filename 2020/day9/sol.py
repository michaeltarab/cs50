import sys,bs
def main():
    arr = [int(x.rstrip()) for x in sys.stdin]
    print(findSet(arr,findNum(arr)))


def findNum(arr):
    for x in range(len(arr)):
        mini_arr = arr[x-25:x]
        if mini_arr: 
            for y in mini_arr:
                val = bs.search(sorted(mini_arr),0,len(mini_arr)-1,arr[x] - y)
                if val != -1:
                    break
            if val == -1:
                return arr[x]

def findSet(arr,num):
    print(arr,num)
    for x in range(len(arr)):
        summed = 0 
        for y in range(x,len(arr),1):
            summed += arr[y]
            if summed == num:
                print(arr[x:y+1])
                return min(arr[x:y+1]) + max(arr[x:y+1])
            elif summed > num:
                break
main()






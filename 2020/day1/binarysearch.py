
def search(a,key):
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if key < a[mid]: 
            hi = mid -1
        elif key > a[mid]:
            lo = mid + 1
        else:
            return True
    return False


#def main(a):
#    key = 10
#    a.sort()
#    if HasKey(a,key): 
#        return True


#assert main([1,2,3,4,4,6,7,8,8,9,10]) == True
#print('passed')

def sort(a,lo,hi):
    if hi <= lo:
        return
    j = partition(a,lo,hi)
    sort(a,lo,j-1) 
    sort(a,j+1,hi)
    return a 
    
def partition(a,lo,hi):
    i = lo + 1
    j = hi
    v = a[lo]
    while True:
        while a[i] < v:
            if i == hi:
                break
            i += 1
        while v < a[j]:
            if j == lo:
                break
            j -= 1
        if i >= j:
            break
        exchange(a,i,j)
        i += 1
        j -= 1

    exchange(a,lo,j)
    return j

def exchange(a,i,j):
    a[i],a[j] = a[j],a[i]

def check(a):
    if sort(arr,0,len(arr) - 1) == sorted(arr):
        return True
    return False




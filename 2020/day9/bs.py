def search(arr, low, high, x): 
  
    if high >= low: 
        mid = (high + low) // 2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return search(arr, low, mid - 1, x) 
        else: 
            return search(arr, mid + 1, high, x) 
    else: 
        return -1
print(search([65,55,62,40,47],0,4,55))

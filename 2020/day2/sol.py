import sys
def main():
    arr = [x.strip().split(" ") for x in sys.stdin]
    return sol(arr,0)

def sol(arr,valid):
    for x in arr:
        nums = []
        index1 = int(x[0].split("-")[0])
        index2 = int(x[0].split("-")[1])
        nums.append(x[2][index1-1])
        nums.append(x[2][index2-1])
        if len(set(nums)) != 1 and x[1][0] in nums:
            valid += 1
    return valid
print(main())


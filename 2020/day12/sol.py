import sys 
def main():
    arr = [x.split() for x in sys.stdin]
    print(solve(arr))

def solve(arr):
    GCS = [0,0,0,0]
    DIR = 1
    SUM = 90 
    for x in arr:
        if (SUM <= -360) or (SUM >= 360)
            SUM = SUM % 360
        DIR = SUM / 90
        if x[0] == 'F':
            GCS[DIR] += [1:]
        elif x[0] == 'N':
            GCS[0] += x[1:]
        elif x[0]  == 'E':
            GCS[1] += x[1:]
        elif x[0] == 'S':
            GCS[2] += x[1:]
        elif x[0] == 'W':
            GCS[3] += x[1:]
        else:
            if x[0] == 'R':
                SUM += x[1:]
            else:
                SUM -= x[1:]
main()






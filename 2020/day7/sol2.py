import sys
def main():
    arr = [x.rstrip().split() for x in sys.stdin]
    bags = store(arr,{})
    print(bagsRequired(bags,bags['shiny gold']))

def store(arr,bags):
    for s in arr:
        
        types = {}
        for count,s2 in enumerate(s):
            if s2 in {'1','2','3','4','5','6','7','8','9'}:
                types[s[count+1] + ' ' + s[count+2]] = int(s2)
        bags[s[0] + ' ' + s[1]] = types
    return bags

def bagsRequired(all_bags,bag):
    if not bag:
        return 0 
    summed = 0
    for bags in bag:
        summed += bag[bags] + (bag[bags] * bagsRequired(all_bags,all_bags[bags]))
    return summed
    





main()
    




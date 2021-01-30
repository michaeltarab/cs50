import sys

def main():
    arr = [x.rstrip().split() for x in sys.stdin]
    print(arr)
    bags = store(arr,{})
    gold_bags = 0
    for bag in bags:
        if countGoldBags(bags,bags[bag]):
                gold_bags += 1
    print(gold_bags)


def store(arr,bags):
    for s in arr:
        types = set()
        for count,s2 in enumerate(s):
            if s2 in {'1','2','3','4','5','6','7','8','9'}:
                types.add(s[count+1] + ' ' + s[count+2])
        bags[s[0] + ' ' + s[1]] = types 
    return bags

def countGoldBags(all_bags,bags):
    if not bags:
        return False
    elif 'shiny gold' in bags:
        return True
    for bag in bags:
       result = countGoldBags(all_bags,all_bags[bag])
       if result:
           return result
main()









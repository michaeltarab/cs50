import sys

def main():
    question_counts = []
    arr = [x.rstrip() for x in sys.stdin]
    count = set()

    for x in arr:
        if x == '':
            question_counts.append(len(count))
            count = set()
        else:
            for y in x:
                if y not in count:
                    count.add(y)
    question_counts.append(len(count))
    print(sum(question_counts))



main()
 

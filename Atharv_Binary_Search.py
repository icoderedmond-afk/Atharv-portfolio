def binary_search(list, target):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while (start<=end):
        print("Step", steps, ":",str(list[start:end+1]))


        steps += 1
        middle = (start+end)/2
        if target == list[middle]:
            return middle
        if target < list[middle]
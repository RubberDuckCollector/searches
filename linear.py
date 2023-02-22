def linear_search(l, target): # l means list

    for i in range(len(l)):
        if l[i] == target:
            return i # index of target
    return -1

nums = [5, 22, 10, 1, 0, 50, 100, 44, 70]
#       0  1   2   3  4  5   6    7   8

print(linear_search(nums, 70))

def binary_search(l, target): # l means list

    found = False
    start = 0
    end = len(l) - 1
    
    while start <= end and found == False:
        midpoint = (start + end) // 2
        if l[midpoint] == target:
            found = True
            return midpoint
        elif l[midpoint] > target:
            end = midpoint - 1 # if the content at the midpoint is larger than target, the end of the searchable region of the list is brought one index to the left than that midpoint.
        else:
            start = midpoint + 1 # otherwise, the start of the searchable region of the list is brought one index to the right of that midpoint. the list now starts from the index to the right of the midpoint, to the end.
            
    return -1

nums = [1, 2, 3, 38, 48, 51, 53, 61, 62, 65, 72, 73, 83, 83, 93]
#       0  1  2  3   4   5   6   7   8   9   10  11  12  13  14

for i in range(len(nums)):
    print(binary_search(nums, nums[i]))

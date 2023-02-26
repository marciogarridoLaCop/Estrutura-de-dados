def max_sum_subarray(arr):
    max_so_far = 0
    max_ending_here = 0
    for i in range(0, len(arr)):
        max_ending_here += arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

arr = [1, 2, 3, -4, 6]
print(str(max_sum_subarray(arr)))

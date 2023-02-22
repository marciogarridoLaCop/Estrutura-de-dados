def hourglass_sum(arr):
  rows = len(arr)
  columns = len(arr[0])
  max_total = True
  for i in range(0, rows-2):
    for j in range(0, columns-2):
        total = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] \
          + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if max_total == True:
            max_total = total
        max_total = max(max_total, total)
  return max_total

arr = [[1, 1, 1, 0, 0, 0],
      [0, 1, 0, 0, 0, 0],
      [1, 1, 1, 0, 0, 0],
      [0, 0, 2, 4, 4, 0],
      [0, 0, 0, 2, 0, 0],
      [0, 0, 1, 2, 4, 0],
                        ]
print(hourglass_sum(arr))

def hourglassSum(arr):
    # Write your code here
    sum_ls = []
    for r in range(4):
        for c in range(4):
            _sum = arr[r][c] + arr[r][c+1] + arr[r][c+2] + arr[r+1][c+1] + arr[r+2][c+1] + arr[r+2][c+2] + arr[r+2][c]
            sum_ls.append(_sum)
    return max(sum_ls)
def minimumAbsoluteDifference(arr):
    # Write your code here
    arr_sort = sorted(arr)
    min_value = abs(arr_sort[0]-arr_sort[1])
    
    for i in range(1,len(arr)-1):
        value = abs(arr_sort[i]-arr_sort[i+1])
        if value<min_value:
            min_value = value
            
    return min_value

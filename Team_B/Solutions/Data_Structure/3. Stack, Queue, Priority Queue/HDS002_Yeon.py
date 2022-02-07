def largestRectangle(h):
    # Write your code here
    
    n = len(h)
    stack = []
    
    i = 0
    top = 0
    area = 0
    max_area = 0
    
    while i < n:
        if not stack or h[i] >= h[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            if not stack:                
                area = h[top] * i                
            else:
                area = h[top] * (i-stack[-1] -1)
            if area > max_area:
                max_area = area
                
    while stack:
        top = stack.pop()
        if not stack:            
            area = h[top] * i                            
        else:
            area = h[top] * (i-stack[-1] -1)
        if area > max_area:
            max_area = area      
    
    return max_area

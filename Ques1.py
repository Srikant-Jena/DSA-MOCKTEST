def Sqrt(x):
    if x == 0:
        return 0

    left, right = 1, x
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1

    return right

# Testing the code
print(Sqrt(4)) 
print(Sqrt(8)) 

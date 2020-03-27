def sqrt(number):
    front = 0
    end = number
    if (number<0):
        return -1
    if end == 1 or end == 0:
        return end
    while front < end:
        mid = (front + end) //2
        if mid**2==number or (mid**2 < number and number < (mid + 1)**2):
            return mid
        if mid**2 > number:
            end = mid
        else:
            front = mid
    return -1

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

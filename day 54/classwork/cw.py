#1
def angle(n):
    if n > 3:
        return 180 + (180 * (n-3))
    else:
        return 180


#2
def solution(nums):
    if (nums is None):
        return []
    else:
        return sorted(nums)

#3
def in_asc_order(arr):
    return arr == sorted(arr)
#linear search function
def linear_search(arr, target1):
    for i in range(len(arr)):
        if arr[i] == target1:
            return i
    return -1 

#binary search function
def binary_search(arr, target2):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target2:
            return mid
        elif arr[mid] < target2:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6]
target1 = 3
target2 = 4
#searching using linear search
result1 = linear_search(arr, target1)
if result1 != -1:
    print(f"Element {target1} found at index {result1}")
else:
    print(f"Element {target1} not found in the list")
#searching using binary search
result2 = binary_search(arr, target2)
if result2 != -1:
    print(f"Element {target2} found at index {result2}")
else:
    print(f"Element {target2} not found in the list")

'''
Question:

Please write a binary search function which searches an item in a sorted list. 
The function should return the index of element to be searched in the list.


Hints:
Use if/elif to deal with conditions.

'''



def binary_search(arr, low, high, x):
    '''
    Returns index of x in arr if present, else -1 
    -------------------------------------------------------------------
    Function call
    
    result = binary_search(arr ,low,   high    , x)

    result = binary_search(arr , 0 , len(arr)-1, x)
            
    -------------------------------------------------------------------
    1. Compare x with the middle element.
    2. If x matches with the middle element, we return the mid index.
    3. Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
    4. Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.
    '''
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1
 
# Test array
arr = [ 2, 3, 4, 10, 40 , 46,21 ,345,55,12,45,9]
arr.sort()
# element
x = 10
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print(f"Sorted List : {arr}\nElement {x} is present at index ", str(result) )
else:
    print("Element is not present in array")
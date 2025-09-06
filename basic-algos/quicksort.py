def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    leftSubArr = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    rightSubArr = [x for x in arr if x > pivot]
    return quickSort(leftSubArr) + mid + quickSort(rightSubArr)

def quickSortInplace(arr, low = 0, high = None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = partition(arr, low, high)
        quickSortInplace(arr, low, pivot_index - 1)
        quickSortInplace(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1




if __name__ == "__main__":
    test_arr = [5, 2, 9, 3, 7, 6, 1, 8, 4]
    print("origin arr:", test_arr)
    
    sorted_arr = quickSort(test_arr)
    print("test result", sorted_arr)

    test_arr2 = [5, 2, 9, 3, 7, 6, 1, 8, 4]
    print("origin arr:", test_arr2)
    
    quickSortInplace(test_arr2)
    print("test result", test_arr2)





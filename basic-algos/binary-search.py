#迭代版
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l)//2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
    return -1
    
#递归版
def binary_search_recur(arr, target, l = 0, r = None):
    if r is None:
        r = len(arr) - 1
    #设置终止条件
    if l > r:
        return -1
    mid = l + (r - l)//2
    if arr[mid] == target:
        return mid 
    elif arr[mid] > target:
        return binary_search_recur(arr, target, l, mid - 1)
    elif arr[mid] < target:
        return binary_search_recur(arr, target, mid + 1, r)
    
testarr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
print(binary_search(testarr, 23))
print(binary_search_recur(testarr,23))

#寻找第一个/最后一个元素（arr中有重复）
def binary_search_dup_first(arr, target):
    res = -1
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l)//2
        if arr[mid] == target:
            #记录但是继续寻找更小的
            res = mid 
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
    return res
testarr = [2, 5, 8, 12, 16, 23, 23, 23, 38, 45, 56, 72]
print(binary_search_dup_first(testarr, 23))

def binary_search_dup_last(arr, target):
    res = -1
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l)//2
        if arr[mid] == target:
            res = mid 
            l = mid + 1
        elif arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
    return res
testarr = [2, 5, 8, 12, 16, 23, 23, 23, 38, 45, 56, 72]
print(binary_search_dup_last(testarr, 23))

#旋转数组（利用旋转数组的有序部分进行判断和搜索）
def binary_search_rot(arr, target):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            return mid 
        #判断哪边有序
        #左半边有序
        if arr[l] <= arr[mid]:
            #左半边可以等于，右半边在这里不等于的原因是target == arr[mid]在之前就会被返回，所以不存在这种情况
            #改成 arr[l] <= target <= arr[mid] 结果仍然相同
            if arr[l] <= target < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        #右半边有序
        else:
            #同上
            if arr[mid] < target <= arr[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1

testarr = [4,5,6,7,1,2,3]
print(binary_search_rot(testarr, 1))

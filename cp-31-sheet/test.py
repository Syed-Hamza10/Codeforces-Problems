def foo(arr):
    n = len(arr)

    for i in range(n):
        if arr[i] == 0:
            j = i
            break
    i = j + 1
    
    while i < n:
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1
    return arr

#print(foo([0,1,0,3,12]))

def dupl(nums):
    n = len(nums)

    i = j = 0

    while j < n:
        if nums[j] != nums[i]: #first value which is different
            i += 1
            nums[i] = nums[j]

        j += 1
    return i + 1, nums

#print(dupl([1,1,2,2,3,3]))    

def left_rot_by1(nums):
    n = len(nums)

    temp = nums[0]

    for i in range(1, n):
        nums[i - 1] = nums[i]

    nums[-1] = temp
    return nums
    # 1 2 3 4 5
    # 2 3 4 5 1
#print(left_rot_by1([1,2,3,4,5]))

def left_rot_by_k(nums, k):

    n = len(nums)

    temp = []

    for i in range(k):
        temp.append(nums[i])
    
    for j in range(k, n):
        nums[j - k] = nums[j]

    # [1,2,3,4,5,6,7]
    # [3,4,5,6,7, _ , _]
    
    i = 0

    for x in range(n - k, n):
        nums[x] = temp[i]
        i += 1
    
    return nums

#print(left_rot_by_k([1,2,3,4,5,6,7],2))


def right_rot_by_k(nums, k):
    n = len(nums)
    temp = []
    for i in range(n - k, n):
        temp.append(nums[i])

    m = -1
    for j in range(n-k-1, -1, -1):
        nums[m] = nums[j]
        m -= 1
    i = 0
    for x in range(k):
        nums[x] = temp[i]
        i += 1
    return nums    

print(right_rot_by_k([1,2,3,4,5,6,7],3))
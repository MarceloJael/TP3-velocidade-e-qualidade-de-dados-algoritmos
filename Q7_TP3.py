def quick_select(arr, left, right, k):
    if left == right:
        return arr[left]

    pivot_index = partition(arr, left, right)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quick_select(arr, left, pivot_index - 1, k)
    else:
        return quick_select(arr, pivot_index + 1, right, k)
    
def partition(arr, left, right):
    pivot = arr[right]
    i = left

    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

def find_kth_smallest(arr, k):
    if k < 1 or k > len(arr):
        return None
    return quick_select(arr, 0, len(arr) - 1, k - 1)

arr = [7, 10, 4, 3, 20, 15]
k = 3
kth_smallest = find_kth_smallest(arr, k)
print(f"O {k}-ésimo menor elemento é: {kth_smallest}")
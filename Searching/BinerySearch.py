def iterative_binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (right + left) // 2
        if arr[middle] == target:
            return middle
        elif target > arr[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return -1

def recursive_binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    middle = (left + right) // 2

    if arr[middle] == target:
        return middle
    elif target > arr[middle]:
        return recursive_binary_search(arr, target, middle + 1, right)
    else:
        return recursive_binary_search(arr, target, left, middle - 1)




def test():
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    result_iterative = iterative_binary_search(data, 70)
    result_recursive = recursive_binary_search(data, 70)
    print("From iterative method, founded at index : ", result_iterative)
    print("From recursive method, founded at index : ", result_recursive)


if __name__ ==  '__main__':
    test()
def binary_search(arr, left, right, target):
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

def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    i = 1
    while i<len(arr):
        i = i*2
    return binary_search(arr, i//2, min(i, len(arr) - 1), target)


def test():
    data = [2, 4, 6, 8, 10, 12, 14, 16]
    print("Found at index :", exponential_search(data, 8))

if __name__ == '__main__':
    test()
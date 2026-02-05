def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low<= high and arr[low] <= target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos+1
        else:
            high = pos-1
    
    return -1


def test():
    data = [10, 20, 30, 40, 50, 60] # the data sould be uniformly distributed
    print("Found at index : ", interpolation_search(data, 50))

if __name__ == '__main__':
    test()
def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
        
    return -1

def test():
    data = [5, 3, 1, 9, 21, 7]
    result = linear_search(data, 21)
    print("Founded at index : ", result)

if __name__ == '__main__':
    test()
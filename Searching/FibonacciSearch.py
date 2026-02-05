def fibonacci_search(arr, target):
    n = len(arr)

    fibM2 = 0
    fibM1 = 1
    fibM = fibM1 + fibM2
    while fibM < n:
        fibM2 = fibM1
        fibM1 = fibM
        fibM = fibM1 + fibM2

    offset = -1

    while fibM > 1:
        i = min(offset + fibM, n - 1)

        if arr[i] < target:
            fibM = fibM1
            fibM1 = fibM2
            fibM2 = fibM - fibM1
            offset = i
        elif arr[i] > target:
            fibM = fibM2
            fibM1 = fibM1 - fibM2
            fibM2 = fibM - fibM1
        else:
            return i 
        if fibM1 and offset+1<n and arr[offset+1] == target:
            return offset+1

def test():
    data = [3, 5, 8, 15, 37, 40]
    print("Found at index : ", fibonacci_search(data, 37))
if __name__ == '__main__':
    test()

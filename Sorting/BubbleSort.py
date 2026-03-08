def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    

def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                swapped = True
        if not swapped:
            break

def test():
    arr = [15, 1, 8, 22, 5]
    # bubble_sort(arr)
    bubble_sort_optimized(arr)
    print(arr)

if __name__ == "__main__":
    test()
        
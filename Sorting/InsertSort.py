def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        
        while j>=0 and arr[i]<arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
        
def test():
    arr = [3, 1, 8, 3, 9]
    insert_sort(arr)
    print(arr)
    
if __name__ == "__main__":
    test()
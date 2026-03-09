def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    middle = n // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    
    return merge(left, right)

def merge(left, right):
    i = j = 0
    
    merged_list = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i+=1
        else: 
            merged_list.append(right[j])
            j+=1
            
        merged_list.extend(left[i:])
        merged_list.extend(right[j:])
        
        return merged_list

def test():
    arr = [7, 2, 1, 10, 22]
    print(merge_sort(arr))
    
if __name__ == "__main__":
    test()
        
        
    
    
    
    
def is_sublist(main_list, sub_list):
    n = len(main_list)
    m = len(sub_list)

    if m == 0:
        return True
    if m > n:
        return False
    
    for i in range(n-m+1):
        if main_list[i:i+m] == sub_list:
            return True
        
    return False


def test():
    main = [1, 2, 3, 4, 5]
    sub1 = [4, 5]
    sub2 = [6, 7]

    print("Found : ", is_sublist(main, sub1))
    print("Found : ", is_sublist(main, sub2))


if __name__ == "__main__":
    test()
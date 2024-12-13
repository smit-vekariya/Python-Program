def binary_search(datalist, target, start, end):
    if start > end:
        return "Not found"
    
    mid = (start + end) // 2

    if datalist[mid] == target:
        return mid

    if datalist[mid] < target:
       return binary_search(datalist, target, mid+1, end)
    else:
       return binary_search(datalist, target, start, mid-1)


if __name__ == "__main__":
    datalist = [2, 4, 6, 10, 12, 130, 143, 443]  # binary search not work on unorder list
    target = 143
    response = binary_search(datalist, target, 0, len(datalist)-1)
    print(response)

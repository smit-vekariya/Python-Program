def liner_search(datalist, target):
    for index, data in enumerate(datalist):
        if data == target:
            return index
    return "Not Found"


if __name__ == "__main__":
    datalist = [10,130,143,443,2,4 ,12,6]
    target = 443
    response = liner_search(datalist, target)
    print(response)

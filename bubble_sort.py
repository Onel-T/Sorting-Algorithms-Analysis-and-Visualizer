# Swaps two elements
def swap(data, i):
    temp = data[i]
    data[i] = data[i + 1]
    data[i + 1] = temp


# Sorts data using bubble sort
def sort(data):
    size = len(data)
    for i in range(0, size - 1):
        for j in range(0, size - 1):
            if data[j] > data[j + 1]:
                swap(data, j)
    return data

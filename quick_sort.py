# Swaps two elements
def swap(data, i, j):
    temp = data[i]
    data[i] = data[j]
    data[j] = temp


# Partitions data
def partition(data, low, high):
    # Pivot set at left most position
    pivot_index = low
    pivot = data[pivot_index]

    while low < high:
        # Finding higher num than pivot
        while low < len(data) and data[low] <= pivot:
            low += 1

        while data[high] > pivot:
            high -= 1

        if low < high:
            swap(data, low, high)
    swap(data, high, pivot_index)
    return high


# Recursion
def qsort(data, low, high):
    if low < high:
        p = partition(data, low, high)
        qsort(data, low, p - 1)
        qsort(data, p + 1, high)


# Starts the sort
def sort(data):
    low = 0
    high = len(data) - 1
    qsort(data, low, high)
    return data

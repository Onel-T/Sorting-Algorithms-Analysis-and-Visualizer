# Sort using insertion sort
def sort(data):
    size = len(data)
    for i in range(1, size):
        current_element = data[i]
        j = i - 1
        while j >= 0 and current_element < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current_element
    return data

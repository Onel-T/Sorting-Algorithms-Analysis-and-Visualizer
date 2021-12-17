# Sort using merge sort algorithm
def sort(data):
    if len(data) <= 1:
        return data
    # Stop condition single/empty list
    middle_index = len(data) // 2
    left_data = sort(data[:middle_index])   # Recursion
    right_data = sort(data[middle_index:])  # Recursion

    sorted_data = []
    left_index = 0
    right_index = 0

    while left_index < len(left_data) and right_index < len(right_data):
        if left_data[left_index] < right_data[right_index]:
            sorted_data.append(left_data[left_index])
            left_index += 1
        else:
            sorted_data.append(right_data[right_index])
            right_index += 1

    sorted_data += left_data[left_index:]
    sorted_data += right_data[right_index:]

    return sorted_data

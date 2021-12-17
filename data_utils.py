from random import randint
import time


# Gets data set length based on given parameter
def get_data_set_lengths(loop_limit):
    lengths = []
    size = 2
    for i in range(0, loop_limit):
        lengths.append(size)
        size *= 2

    return lengths


# Generates random int data
def generate_data(size):
    data = []
    for i in range(0, size):
        random_num = randint(0, size * 4)
        data.append(random_num)

    return data


# Validates if data is actually sorted
def validator(data):
    i = 0
    length = len(data)
    while i < length - 1:
        if data[i] > data[i + 1]:
            return False
        i += 1
    if data[length - 2] > data[length - 1]:
        return False
    return True


# Runs data through the algorithm
def run_data(algorithm, loop_limit):
    all_times = []
    size = 2

    # Each loop runs a new bigger data set through algorithm
    for i in range(0, loop_limit):
        data = generate_data(size)
        unsorted_data = list(data)

        start_time = time.time()
        sorted_data = algorithm.sort(data)
        total_time = time.time() - start_time

        all_times.append(total_time)

        if size <= 128:
            print("Unsorted: ")
            print(unsorted_data)
            print("Sorted: ")
            print(sorted_data)
        else:
            print("** Data of size %d elements too large to print **" % size)
            print("\tSort Validation: " + str(validator(sorted_data)) + "\n")
        size *= 2

    return all_times

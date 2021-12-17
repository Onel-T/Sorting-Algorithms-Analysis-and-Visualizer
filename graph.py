import matplotlib.pyplot as plt
import numpy
import math


def graph_bubble_sort(real_x, real_y):
    theoretical_x = []
    theoretical_y = []

    # Calculates theoretical bubble sort complexity (O(n^2))
    for i in range(0, 10):
        theoretical_x.append(i)
        theoretical_y.append(math.pow(i, 2))

    fig, ax1 = plt.subplots()
    left, bottom, width, height = [0.25, 0.6, 0.2, 0.2]
    ax2 = fig.add_axes([left, bottom, width, height])

    ax1.plot(real_x, real_y, color='blue')
    ax1.title.set_text('Bubble Sort Big O Results')
    ax1.set(xlabel="Input Size (n)", ylabel="Time")

    ax2.plot(theoretical_x, theoretical_y, color='orange')
    plt.title('Theoretical')

    plt.show()


def graph_merge_sort(real_x, real_y):
    theoretical_x = []
    theoretical_y = []

    # Calculates theoretical quick sort complexity (O(n log n))
    for i in range(1, 500):
        theoretical_x.append(i)
        theoretical_y.append(i * (numpy.log(i)))

    fig, ax1 = plt.subplots()
    left, bottom, width, height = [0.25, 0.6, 0.2, 0.2]
    ax2 = fig.add_axes([left, bottom, width, height])

    ax1.plot(real_x, real_y, color='blue')
    ax1.title.set_text('Merge Sort Big O Results')
    ax1.set(xlabel="Input Size (n)", ylabel="Time")

    ax2.plot(theoretical_x, theoretical_y, color='orange')
    plt.title('Theoretical')

    plt.show()


def graph_quick_sort(real_x, real_y):
    theoretical_x = []
    theoretical_y = []

    # Calculates theoretical quick sort complexity (O(n log(n))
    for i in range(1, 500):
        theoretical_x.append(i)
        theoretical_y.append(i * (numpy.log(i)))

    fig, ax1 = plt.subplots()
    left, bottom, width, height = [0.25, 0.6, 0.2, 0.2]
    ax2 = fig.add_axes([left, bottom, width, height])

    ax1.plot(real_x, real_y, color='blue')
    ax1.title.set_text('Quick Sort Big O Results')
    ax1.set(xlabel="Input Size (n)", ylabel="Time")

    ax2.plot(theoretical_x, theoretical_y, color='orange')
    plt.title('Theoretical')

    plt.show()


def graph_insertion_sort(real_x, real_y):
    theoretical_x = []
    theoretical_y = []

    # Calculates theoretical insertion sort complexity (O(n^2))
    for i in range(0, 10):
        theoretical_x.append(i)
        theoretical_y.append(math.pow(i, 2))

    fig, ax1 = plt.subplots()
    left, bottom, width, height = [0.25, 0.6, 0.2, 0.2]
    ax2 = fig.add_axes([left, bottom, width, height])

    ax1.plot(real_x, real_y, color='blue')
    ax1.title.set_text('Insertion Sort Big O Results')
    ax1.set(xlabel="Input Size (n)", ylabel="Time")

    ax2.plot(theoretical_x, theoretical_y, color='orange')
    plt.title('Theoretical')

    plt.show()

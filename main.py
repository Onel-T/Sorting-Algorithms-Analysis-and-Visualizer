import bubble_sort
import data_utils
import graph
import insertion_sort
import merge_sort
import quick_sort

choice = -1
while choice != 5:
    print("Choose which sorting algorithm to run: ")
    print("[1] BubbleSort")
    print("[2] MergeSort")
    print("[3] QuickSort")
    print("[4] InsertionSort")
    print("[5] EXIT")
    choice = int(input(" Option: "))

    if choice == 1:
        x = data_utils.get_data_set_lengths(13)
        y = data_utils.run_data(bubble_sort, 13)
        graph.graph_bubble_sort(x, y)
    elif choice == 2:
        x = data_utils.get_data_set_lengths(20)
        y = data_utils.run_data(merge_sort, 20)
        graph.graph_merge_sort(x, y)
    elif choice == 3:
        x = data_utils.get_data_set_lengths(20)
        y = data_utils.run_data(quick_sort, 20)
        graph.graph_quick_sort(x, y)
    elif choice == 4:
        x = data_utils.get_data_set_lengths(14)
        y = data_utils.run_data(insertion_sort, 14)
        graph.graph_insertion_sort(x, y)

print("** Thank you, Program Exit. **")

from algoritmos.selectionSort import selection_sort_menu
from algoritmos.insertionSort import insertion_sort_menu
from algoritmos.mergeSort import merge_sort_menu
from algoritmos.quickSort import quick_sort_menu

if __name__ == "__main__":
    op = 1
    while(op != 0):
        print("╵-----------------------╵")
        print("╵ Escolha um algoritimo ╵")
        print("╵ 1 - Selection Sort    ╵")
        print("╵ 2 - Insertion Sort    ╵")
        print("╵ 3 - Merge Sort        ╵")
        print("╵ 4 - Quick Sort        ╵")
        print("╵-----------------------╵\n")
        op = input()

        if op == '1':
            selection_sort_menu()
        if op == '2':
            insertion_sort_menu()
        if op == '3':
            merge_sort_menu()
        if op == '4':
            quick_sort_menu()


#insert sort [x]
#select sort [x]
#merge sort [x]
#quick sort [x]
#bubble sort []  
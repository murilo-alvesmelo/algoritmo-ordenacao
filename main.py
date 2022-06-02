from algoritmos.bubbleSort import bubble_sort_menu
from algoritmos.selectionSort import selection_sort_menu
from algoritmos.insertionSort import insertion_sort_menu
from algoritmos.mergeSort import merge_sort_menu
from algoritmos.quickSort import quick_sort_menu

if __name__ == "__main__":
    op = 1
    while(op != '0'):
        print("╵-----------------------╵")
        print("╵ Escolha um algoritimo ╵")
        print("╵ 1 - Insertion Sort    ╵")
        print("╵ 2 - Selection Sort    ╵")
        print("╵ 3 - Bubble Sort       ╵")
        print("╵ 4 - Merge Sort        ╵")
        print("╵ 5 - Quick Sort        ╵")
        print("╵ 0 - Sair              ╵")
        print("╵-----------------------╵\n")
        op = input()

        if op == '1':
            insertion_sort_menu()
        if op == '2':
            selection_sort_menu()
        if op == '3':
            bubble_sort_menu()
        if op == '4':
            merge_sort_menu()
        if op == '5':
            quick_sort_menu()

#insert sort [x]
#select sort [x]
#merge sort [x]
#quick sort [x]
#bubble sort [x]  
from re import T
from timeit import default_timer as timer
from get_numbers import get_cem, get_Mil, get_dezMil, get_vinteMil, get_cinquentaMil, get_cemMil, get_duzentosMil, get_quinhetosMil, get_umMilhao, get_doisMilhao, get_cincoMilhao


def bubble_sort(List, n):
    for i in range(n - 1):
        for j in range(n - 1):
            if List[j] > List[j + 1]:
                aux = List[j]
                List[j] = List[j + 1]
                List[j+1] = aux

def bubble_sort_menu():
    
    print('╵----Selecione a quantidade-----╵')
    print('1 - cem\n2 - mil\n3 - dezMil\n4 - vinteMil\n5 - cinquentaMil\n6 - cemMil\n7 - duzentosMil\n8 - quinhetosMil\n9 - umMilhao\n10 - doisMilhoes\n11 - cincoMilhoes')
    print("╵------------------------------╵")

    
    op = input()
    if op == '1':
        List = get_cem()
        tsort = timer()
        bubble_sort(List, len(List))
        tsort = timer() - tsort
        print(List)
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '2':
        List = get_Mil()
        tsort = timer()
        bubble_sort(List, len(List))
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '3':
        List = get_dezMil()
        tsort = timer()
        bubble_sort(List, len(List))
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '4':
        List = get_vinteMil()
        tsort = timer()
        bubble_sort(List, len(List))
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '5':
        List = get_cinquentaMil()
        tsort = timer()
        bubble_sort(List, len(List))
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '6':
        List = get_cemMil()
        tsort = timer()
        bubble_sort(List, len(List))
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '7':
        List = get_duzentosMil()
        tsort = timer()
        bubble_sort(List, len(List))
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '8':
        List = get_quinhetosMil()
        tsort = timer()
        bubble_sort(List, len(List))
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '9':
        List = get_umMilhao()
        tsort = timer()
        bubble_sort(List, len(List))
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '10':
        List = get_doisMilhao()
        tsort = timer()
        bubble_sort(List, len(List))
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '11':
        List = get_cincoMilhao()
        tsort = timer()
        bubble_sort(List, len(List))
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
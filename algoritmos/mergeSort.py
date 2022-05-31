from timeit import default_timer as timer
from get_numbers import get_cem, get_Mil, get_dezMil, get_vinteMil, get_cinquentaMil, get_cemMil, get_duzentosMil, get_quinhetosMil, get_umMilhao, get_doisMilhao, get_cincoMilhao


#O(n log(n))
def merge_sort(List, inicio, final):
    if inicio < final:
        centro = (inicio + final) >> 1
        merge_sort(List, inicio, centro)
        merge_sort(List, centro + 1, final)  
        merge(List, inicio, centro, final)

def merge(List, inicio, centro, final):
    inicio1 = inicio
    inicio2 = centro + 1
    aux = []

    while (inicio1 <= centro) and (inicio2 <= final):
        if List[inicio1] < List[inicio2]:
            aux.append(List[inicio1])
            inicio1 = inicio1 + 1
        else:
            aux.append(List[inicio2])
            inicio2 = inicio2 + 1

    while (inicio1 <= centro):
        aux.append(List[inicio1])
        inicio1 = inicio1 + 1

    while (inicio2 <= final):
        aux.append(List[inicio2])
        inicio2 = inicio2 + 1

    for i in range(len(aux)):
        List[inicio + i] = aux[i]

def merge_sort_menu():
    
    print('╵----Selecione a quantidade-----╵')
    print('1 - cem\n2 - mil\n3 - dezMil\n4 - vinteMil\n5 - cinquentaMil\n6 - cemMil\n7 - duzentosMil\n8 - quinhetosMil\n9 - umMilhao\n10 - doisMilhoes\n11 - cincoMilhoes')
    print("╵------------------------------╵")

    
    op = input()
    if op == '1':
        List = get_cem()
        tsort = timer()
        merge_sort(List, 0, len(List) - 1)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '2':
        List = get_Mil()
        tsort = timer()
        merge_sort(List, 0, len(List) - 1)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '3':
        List = get_dezMil()
        tsort = timer()
        merge_sort(List, 0, len(List) - 1)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '4':
        List = get_vinteMil()
        tsort = timer()
        merge_sort(List, 0, len(List) - 1)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '5':
        List = get_cinquentaMil()
        tsort = timer()
        merge_sort(List, 0, len(List) - 1)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '6':
        List = get_cemMil()
        tsort = timer()
        merge_sort(List, 0, len(List) - 1)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '7':
        List = get_duzentosMil()
        tsort = timer()
        merge_sort(List, 0, len(List) - 1)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '8':
        List = get_quinhetosMil()
        tsort = timer()
        merge_sort(List, 0, len(List) - 1)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '9':
        List = get_umMilhao()
        tsort = timer()
        merge_sort(List, 0, len(List) - 1)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '10':
        List = get_doisMilhao()
        tsort = timer()
        merge_sort(List, 0, len(List) - 1)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '11':
        List = get_cincoMilhao()
        tsort = timer()
        merge_sort(List, 0, len(List) - 1)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
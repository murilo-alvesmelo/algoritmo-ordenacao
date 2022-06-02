from timeit import default_timer as timer
from get_numbers import get_cem, get_Mil, get_dezMil, get_vinteMil, get_cinquentaMil, get_cemMil, get_duzentosMil, get_quinhetosMil, get_umMilhao, get_doisMilhao, get_cincoMilhao

#O(n log(n))
def quick_sort(List, inicio, final):
    if inicio < final:
        pivo = particao(List, inicio, final)
        quick_sort(List, inicio, pivo-1)
        quick_sort(List, pivo, final)

def particao(List, inicio, final):
    centro = (final - inicio) >> 1
    pivo = List[inicio + centro]
    
    i = inicio
    j = final

    while True:
        while List[i] < pivo:
            i = i + 1

        while List[j] > pivo:
            j = j - 1
        
        if i >= j:
            break
        
        aux = List[i]
        List[i] = List[j]
        List[j] = aux
        i = i + 1
        j = j - 1
    aux = List[i]
    List[i] = List[final]
    List[final] = aux

    return i

def quick_sort_menu():
    print('╵--------Quick Sort-------------╵')
    print('╵----Selecione a quantidade-----╵')
    print('1 - cem\n2 - mil\n3 - dezMil\n4 - vinteMil\n5 - cinquentaMil\n6 - cemMil\n7 - duzentosMil\n8 - quinhetosMil\n9 - umMilhao\n10 - doisMilhoes\n11 - cincoMilhoes')
    print("╵-------------------------------╵")
    
    op = input()
    if op == '1':
        List = get_cem()
        tsort = timer()
        quick_sort(List, 0, len(List) - 1 )
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '2':
        List = get_Mil()
        tsort = timer()
        quick_sort(List, 0, len(List) -1 )
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '3':
        List = get_dezMil()
        tsort = timer()
        quick_sort(List, 0, len(List) -1 )
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '4':
        List = get_vinteMil()
        tsort = timer()
        quick_sort(List, 0, len(List) -1 )
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '5':
        List = get_cinquentaMil()
        tsort = timer()
        quick_sort(List, 0, len(List) -1 )
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '6':
        List = get_cemMil()
        tsort = timer()
        quick_sort(List, 0, len(List) -1 )
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '7':
        List = get_duzentosMil()
        tsort = timer()
        quick_sort(List, 0, len(List) -1 )
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '8':
        List = get_quinhetosMil()
        tsort = timer()
        quick_sort(List, 0, len(List) -1 )
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '9':
        List = get_umMilhao()
        tsort = timer()
        quick_sort(List, 0, len(List) -1 )
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '10':
        List = get_doisMilhao()
        tsort = timer()
        quick_sort(List, 0, len(List) -1 )
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '11':
        List = get_cincoMilhao()
        tsort = timer()
        quick_sort(List, 0, len(List) -1 )
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
from timeit import default_timer as timer
from get_numbers import get_cem, get_Mil, get_dezMil, get_vinteMil, get_cinquentaMil, get_cemMil, get_duzentosMil, get_quinhetosMil, get_umMilhao, get_doisMilhao, get_cincoMilhao

#O(n^2 ) 
# Melhor caso o(n) quando o vetor já está ordernado
def insertion_sort(List):
    for i in range(1, len(List)):
        index = List[i]
        j = i - 1

        while( j >= 0) and (List[j] > index):
            List[j + 1] = List[j] 
            j = j - 1

        List[j+1] = index

def insertion_sort_menu():
    
    print('╵----Selecione a quantidade-----╵')
    print('1 - cem\n2 - mil\n3 - dezMil\n4 - vinteMil\n5 - cinquentaMil\n6 - cemMil\n7 - duzentosMil\n8 - quinhetosMil\n9 - umMilhao\n10 - doisMilhoes\n11 - cincoMilhoes')
    print("╵------------------------------╵")

    
    op = input()
    if op == '1':
        List = get_cem()
        tsort = timer()
        insertion_sort(List)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '2':
        List = get_Mil()
        tsort = timer()
        insertion_sort(List)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '3':
        List = get_dezMil()
        tsort = timer()
        insertion_sort(List)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '4':
        List = get_vinteMil()
        tsort = timer()
        insertion_sort(List)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '5':
        List = get_cinquentaMil()
        tsort = timer()
        insertion_sort(List)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '6':
        List = get_cemMil()
        tsort = timer()
        insertion_sort(List)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '7':
        List = get_duzentosMil()
        tsort = timer()
        insertion_sort(List)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '8':
        List = get_quinhetosMil()
        tsort = timer()
        insertion_sort(List)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '9':
        List = get_umMilhao()
        tsort = timer()
        insertion_sort(List)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '10':
        List = get_doisMilhao()
        tsort = timer()
        insertion_sort(List)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
    if op == '11':
        List = get_cincoMilhao()
        tsort = timer()
        insertion_sort(List)
        tsort = timer() - tsort
        print(List[:11])
        print('Tempo de execucao do algoritmo: ', tsort)
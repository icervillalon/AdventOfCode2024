'''
El algoritmo consiste en crear un diccionario con las páginas "primarias" como claves, que deben ser impresas antes que
las segundas (separadas con un | en el fichero de datos), y que se meten en una lista dentro de la clave de la página primaria.

Para las listas de orden de impresión, vamos a recorrer la lista comprobando que la página que estamos validando no
depende de otra página primaria, viendo si la página a comprobar está dentro de otra entrada del diccionario. Si no
lo está, sumamos el valor de la página que se encuentra en mitad de la lista.
'''



def create_datasets(file_path: str) -> tuple:
    with open(file_path, 'r') as file:
        data = file.read()
    page_dict = {}
    page_order = []
    for line in data.split('\n'):
        if '|' in line:
            x,y = line.split('|')
            x = int(x)
            y = int(y)
            if x in page_dict:
                page_dict[x].append(y)
            else:
                page_dict[x]=[y]
        elif ',' in line:
            page_order.append(line.split(','))
        else:
            continue
    return page_dict, page_order

def check_page_order(page_dict: dict, page_order: list) -> int:
    total_result = 0
    for order in page_order:
        approved_print = True
        for current_page_index in range(0,len(order)):
            for next_page_index in range(current_page_index, len(order)):
                if int(order[next_page_index]) in page_dict.keys():
                    # Check if the current page depends on the following pages
                    if int(order[current_page_index]) in page_dict[int(order[next_page_index])]:
                        approved_print = False
        if approved_print:
            total_result += int(order[int((len(order)-1)/2)])
    return total_result

def ex_5(path_file: str) -> int:
    page_dict, page_order = create_datasets(path_file)
    return check_page_order(page_dict, page_order)

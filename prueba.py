"""
Prueba de Monoku - En Monoku compran muchas galguerias y muchas veces hay que
botarlas porque se vencen. Por eso este programa responde las siguientes preguntas:
- Que come cada miembro del equipo?
- El nombre de la persona que mas consumio
- Nombre del producto que mas se consumio.
"""
import csv
from json import loads, dumps


#Leer csv y pasarlo a un nested dictionary
def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename, "r") as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            row.pop(keyfield)
            table[rowid] = row
    return table

#tests
# test1 = read_csv_as_nested_dict("table1.csv", "name", ",", "'")
# print(test1)
# expected = {"sara": {"achira":0, "club social":1},
#             "milena": {"achira":4, "club social":1},
#             "julian": {"achira":2, "club social":3}}
#print("")
# print(expected)

#test2 = read_csv_as_nested_dict("chucherias.csv", "Nombre", ",", "'")
#print(test2["Luis Villalobos"])


#Funcion que procesa tabla para obtener valores mensuales y elimina columnas innecesarias
def clean_table(filename, keyfield, pop_key):
    """
    Inputs:
    - filename - Name of CSV file
    - keyfield - Field to use as key for rows
    - pop_key - Column key that is going to be deleted from the dictionary
    Outputs:
    - Dictionary of dictionaries where the outer dictionary
    maps the value in the key_field to the corresponding row in the
    CSV file. The inner dictionaries map the field names to the
    field values for that row.
    """

    table= read_csv_as_nested_dict(filename, keyfield, ",", "'")

    for value in table.values():
        value.pop(pop_key)
        for inner_key in value:
            inner_value = value[inner_key]
            int_value = int(inner_value) * 4
            value[inner_key] = int_value

    return table

#tests
#clean_test = clean_table("chucherias.csv", "Nombre", "Timestamp")
#print(clean_test["Luis Villalobos"])
# print("'Timestamp' no deberia estar. Los numeros deben ser tipo int y no string")

tabla2 = clean_table("chucherias2.csv", "Nombre", "Timestamp")
#print(clean_table("chucherias2.csv", "Nombre", "Timestamp"))


#From ordered dict to dict
def to_dict(ordered_dict):
    return loads(dumps(ordered_dict))

table_dict = to_dict(tabla2)


def remove_ceros(table):
    new_table = {}

    for key, value in table.items():
        inner_dict = {}
        new_table[key] = inner_dict
        for inner_key, inner_value in value.items():
            if inner_value > 0:
                inner_dict[inner_key] = inner_value

    return new_table

print(remove_ceros(table_dict))


#Funcion que imprime lo que come cada persona
def print_table(table):
    """
    Input:
    - table - Dictionary of dictionaries
    Output:
    Prints table
    """
    new_table = {}

    for key, value in table.items():
        row = []
        #row.append(key)
        for chucheria in value:
            if value[chucheria] > 0:
                row.append(chucheria)
        new_table[key] = row
        print(",".join(row))

    return new_table

#print_table(clean_test)
#print(print_table(tabla2))


def print_rows(table):
    """
    Input:
    - table - Dictionary of dictionaries
    Output:
    Prints table
    """

    for key, value in table.items():
        row = [key]
        for chucheria in value:
            if value[chucheria] > 0 and value[chucheria] not in row:
                row.append([chucheria, value[chucheria]])
        print(row)


#print_rows(tabla2)


def get_names(table):
    """
    Input:
    - table - Dictionary of dictionaries
    Output:
    List of team member names
    """
    NAMES = []

    for key in table:
        NAMES.append(key)

    return NAMES


#print(get_names(tabla2))

#Funcion que retorne nombre de la persona que mas consumio (suma de todos los valores)
def ate_the_most(table):
    """
    Input:
    - table - Dictionary of dictionaries
    Output:
    Returns who ate the most in the month
    """
    consumo = []

    for key, value in table.items():
        total = 0
        for chucheria in value:
            inner_value = value[chucheria]
            total = total + inner_value
        tup = (key, total)
        consumo.append(tup)

    consumo.sort(key=lambda x: x[1], reverse=True)
    mayor_consumo = consumo[0]

    return "El que mas consumio fue " + mayor_consumo[0]

print(ate_the_most(tabla2))


#Funcion que retorne producto que mas se consumio
def most_consumed(table):
    """
    - table - Dictionary of dictionaries
    Output:
    Returns what product was consumed the most in the month
    """
    chucherias = {}

    for value in table.values():
        for chucheria in value:
            if chucheria not in chucherias:
                inner_value = value[chucheria]
                chucherias[chucheria] = inner_value
            else:
                inner_value = chucherias[chucheria]
                inner_value = inner_value + value[chucheria]
                chucherias[chucheria] = inner_value

    chucherias_list = [(key, value) for key, value in chucherias.items()]
    chucherias_list.sort(key=lambda x: x[1], reverse=True)

    mas_consumido = chucherias_list[0]

    return "El producto mas consumido fue " + mas_consumido[0]


print(most_consumed(tabla2))

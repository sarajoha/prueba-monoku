"""
Prueba de Monoku - En Monoku compran muchas galguerias y muchas veces hay que
botarlas porque se vencen. Por eso este programa responde las siguientes preguntas:
- Que come cada miembro del equipo?
- El nombre de la persona que mas consumio
- Nombre del producto que mas se consumio.
"""
import csv


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
    with open(filename, "rb") as csvfile:
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
clean_test = clean_table("chucherias.csv", "Nombre", "Timestamp")
#print(clean_test["Luis Villalobos"])
# print("'Timestamp' no deberia estar. Los numeros deben ser tipo int y no string")

tabla2 = clean_table("chucherias2.csv", "Nombre", "Timestamp")

#Funcion que imprime lo que come cada persona
def print_table(table):
    """
    Input:
    - table - Dictionary of dictionaries
    Output:
    Prints table
    """

    for key, value in table.items():
        row = []
        row.append(key)
        for chucheria in value:
            if value[chucheria] > 0:
                row.append(chucheria)
        print(",".join(row))

#print_table(clean_test)
#print_table(tabla2)


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

    return("El que mas consumio fue " + mayor_consumo[0])

print(ate_the_most(tabla2))


#Funcion que retorne producto que mas se consumio

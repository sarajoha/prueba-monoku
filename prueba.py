"""
Pruebla de Monoku - En Monoku compran muchas galguerias y muchas veces hay que
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
test1= read_csv_as_nested_dict("table1.csv", "name", ",", "'")
print(test1)
expected = {"sara": {"achira":0, "club social":1},
            "milena": {"achira":4, "club social":1},
            "julian": {"achira":2, "club social":3}}
print(expected)


#Funcion que imprima lo que come cada persona, ignorando valores de 0


#Funcion que retorne nombre de la persona que mas consumio (suma de todos los valores)


#Funcion que retorne producto que mas se consumio

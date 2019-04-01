"""
Pruebla de Monoku - En Monoku compran muchas galguerias y muchas veces hay que
botarlas porque se vencen. Por eso este programa responde las siguientes preguntas:
- Qué come cada miembro del equipo?
- El nombre de la persona que más consumió
- Nombre del producto que más se consumió.
"""

#Datos del consumo mensual de galguerias (chucherias)
galguerias: {"Leonel": {"Cocosette": 4, "Cub social": 0, "Ritz": 0, "Jumbo":0,
                        "Jet":0, "Pringles":0, "Chips Ahoy":0, "Palomitas":0,
                        "Tosh": 0, "Bridge":0, "Bon Bon Bum":0, "Frunas": 0,
                        "Saltin Noel":0, "Gansito":0, "Chocorramos":0, "Gala Miti":0,
                        "Achiras":0
                        },
            "Jose": {"Cocosette": 4, "Cub social": 0, "Ritz": 0, "Jumbo":0,
                    "Jet":0, "Pringles":0, "Chips Ahoy":0, "Palomitas":0,
                    "Tosh": 0, "Bridge":0, "Bon Bon Bum":0, "Frunas": 0,
                    "Saltin Noel":0, "Gansito":0, "Chocorramos":0, "Gala Miti":0,
                    "Achiras":0
                    },
            "Julian": {"Cocosette": 4, "Cub social": 0, "Ritz": 0, "Jumbo":0,
                    "Jet":0, "Pringles":0, "Chips Ahoy":0, "Palomitas":0,
                    "Tosh": 0, "Bridge":0, "Bon Bon Bum":0, "Frunas": 0,
                    "Saltin Noel":0, "Gansito":0, "Chocorramos":0, "Gala Miti":0,
                    "Achiras":0
                        },
            "Juan": {"Cocosette": 4, "Cub social": 0, "Ritz": 0, "Jumbo":0,
                    "Jet":0, "Pringles":0, "Chips Ahoy":0, "Palomitas":0,
                    "Tosh": 0, "Bridge":0, "Bon Bon Bum":0, "Frunas": 0,
                    "Saltin Noel":0, "Gansito":0, "Chocorramos":0, "Gala Miti":0,
                    "Achiras":0
                    },
            "Luis": {"Cocosette": 4, "Cub social": 0, "Ritz": 0, "Jumbo":0,
                    "Jet":0, "Pringles":0, "Chips Ahoy":0, "Palomitas":0,
                    "Tosh": 0, "Bridge":0, "Bon Bon Bum":0, "Frunas": 0,
                    "Saltin Noel":0, "Gansito":0, "Chocorramos":0, "Gala Miti":0,
                    "Achiras":0
                    },
            "Yeison": {"Cocosette": 4, "Cub social": 0, "Ritz": 0, "Jumbo":0,
                    "Jet":0, "Pringles":0, "Chips Ahoy":0, "Palomitas":0,
                    "Tosh": 0, "Bridge":0, "Bon Bon Bum":0, "Frunas": 0,
                    "Saltin Noel":0, "Gansito":0, "Chocorramos":0, "Gala Miti":0,
                    "Achiras":0
                    },
            "Andres C": {"Cocosette": 4, "Cub social": 0, "Ritz": 0, "Jumbo":0,
                    "Jet":0, "Pringles":0, "Chips Ahoy":0, "Palomitas":0,
                    "Tosh": 0, "Bridge":0, "Bon Bon Bum":0, "Frunas": 0,
                    "Saltin Noel":0, "Gansito":0, "Chocorramos":0, "Gala Miti":0,
                    "Achiras":0
                    },
            "Eli": {"Cocosette": 4, "Cub social": 0, "Ritz": 0, "Jumbo":0,
                    "Jet":0, "Pringles":0, "Chips Ahoy":0, "Palomitas":0,
                    "Tosh": 0, "Bridge":0, "Bon Bon Bum":0, "Frunas": 0,
                    "Saltin Noel":0, "Gansito":0, "Chocorramos":0, "Gala Miti":0,
                    "Achiras":0
                    },
            "Alejandra": {"Cocosette": 4, "Cub social": 0, "Ritz": 0, "Jumbo":0,
                    "Jet":0, "Pringles":0, "Chips Ahoy":0, "Palomitas":0,
                    "Tosh": 0, "Bridge":0, "Bon Bon Bum":0, "Frunas": 0,
                    "Saltin Noel":0, "Gansito":0, "Chocorramos":0, "Gala Miti":0,
                    "Achiras":0
                    },
            "Estefany": {"Cocosette": 4, "Cub social": 0, "Ritz": 0, "Jumbo":0,
                    "Jet":0, "Pringles":0, "Chips Ahoy":0, "Palomitas":0,
                    "Tosh": 0, "Bridge":0, "Bon Bon Bum":0, "Frunas": 0,
                    "Saltin Noel":0, "Gansito":0, "Chocorramos":0, "Gala Miti":0,
                    "Achiras":0
                    },
            "Brian": {"Cocosette": 4, "Cub social": 0, "Ritz": 0, "Jumbo":0,
                    "Jet":0, "Pringles":0, "Chips Ahoy":0, "Palomitas":0,
                    "Tosh": 0, "Bridge":0, "Bon Bon Bum":0, "Frunas": 0,
                    "Saltin Noel":0, "Gansito":0, "Chocorramos":0, "Gala Miti":0,
                    "Achiras":0
                    },
            "Natalia": {"Cocosette": 4, "Cub social": 0, "Ritz": 0, "Jumbo":0,
                    "Jet":0, "Pringles":0, "Chips Ahoy":0, "Palomitas":0,
                    "Tosh": 0, "Bridge":0, "Bon Bon Bum":0, "Frunas": 0,
                    "Saltin Noel":0, "Gansito":0, "Chocorramos":0, "Gala Miti":0,
                    "Achiras":0
                    },
            "Luix": {"Cocosette": 4, "Cub social": 0, "Ritz": 0, "Jumbo":0,
                    "Jet":0, "Pringles":0, "Chips Ahoy":0, "Palomitas":0,
                    "Tosh": 0, "Bridge":0, "Bon Bon Bum":0, "Frunas": 0,
                    "Saltin Noel":0, "Gansito":0, "Chocorramos":0, "Gala Miti":0,
                    "Achiras":0
                    },
            "Andres A":{"Cocosette": 4, "Cub social": 0, "Ritz": 0, "Jumbo":0,
                    "Jet":0, "Pringles":0, "Chips Ahoy":0, "Palomitas":0,
                    "Tosh": 0, "Bridge":0, "Bon Bon Bum":0, "Frunas": 0,
                    "Saltin Noel":0, "Gansito":0, "Chocorramos":0, "Gala Miti":0,
                    "Achiras":0
                    }
            }


#Funcion que imprima lo que come cada persona, ignorando valores de 0

#Funcion que retorne nombre de la persona que mas consumio (suma de todos los valores)

#Funcion que retorne producto que mas se consumio

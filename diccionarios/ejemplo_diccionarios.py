# La agenda de contactos

# cual es el elemento llave de una agenda?
# nombre  -> {"telefono": "1234",
#             "email": "qwer@asd.com",
#             "lugar_trabajo": "mcdonalds"
#             }
#
#

# la agenda vacia
agenda = {}

# juanito conoce a carlitos
agenda['carlitos'] = {"telefono": "987654",
                      "email": "carlitos@aol.com",
                      "lugar_trabajo": "pali"
                      }

# agregar la informacion de maria
agenda.update({"maria": {"telefono": "4567334",
                      "email": "maria@aol.com",
                      "lugar_trabajo": "ice"
                      }
               })

print(agenda)
# como se  consulta?

telefono_maria = agenda["maria"]["telefono"]
print(telefono_maria)

# como hago para actualizar el telefono de carlitos? el nuevo es 765434
# hay muchas


# esto me va a dar una diccionario
agenda["carlitos"]["telefono"] = "345678"

print(agenda["carlitos"])
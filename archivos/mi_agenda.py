# se supone que existe un archivo llamado mi_agenda.json

import json

with open("mi_agenda.json", mode="r") as mi_archivo:
    mi_agenda = json.load(mi_archivo)

pass
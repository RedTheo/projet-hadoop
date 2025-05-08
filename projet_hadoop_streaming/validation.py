#!/usr/bin/env python
# validation.py

import sys

HEADER_PREFIX = "sexe;"

for line in sys.stdin:
    line = line.rstrip('\n')
    if not line:
        continue

    # Filtrer l'en-tete (peut reapparaitre a chaque split Hadoop)
    if line.startswith(HEADER_PREFIX):
        continue

    parts = line.split(';')
    if len(parts) != 5:
        continue

    # champs : sexe;prenom;annee;departement;nombre
    sexe, preusuel, annais, dept, nombre = [p.strip() for p in parts]

    # aucun champ vide, pas de valeurs systemes
    if not (sexe and preusuel and annais and dept and nombre):
        continue
    if preusuel in ('_PRENOMS_RARES', 'XXXX'):
        continue
    if annais == 'XXXX':
        continue
    if dept == 'XX':
        continue

    # emet la ligne validee
    sys.stdout.write("%s;%s;%s;%s;%s\n" % (sexe, preusuel, annais, dept, nombre))

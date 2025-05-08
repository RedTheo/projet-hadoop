#!/usr/bin/env python
# mapper.py

import sys

for line in sys.stdin:
    line = line.rstrip('\n')
    if not line:
        continue

    parts = line.split(';')
    if len(parts) != 5:
        continue

    sexe, preusuel, annais, dept, nombre = [p.strip() for p in parts]

    # cle : annee_sexe_prenom
    key = "%s_%s_%s" % (annais, sexe, preusuel)
    sys.stdout.write("%s\t%s\n" % (key, nombre))

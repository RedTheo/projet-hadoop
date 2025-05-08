#!/usr/bin/env python
# post_traitement.py

import sys
from collections import defaultdict

groups = defaultdict(list)

for line in sys.stdin:
    line = line.rstrip('\n')
    if not line:
        continue

    parts = line.split('\t')
    if len(parts) != 2:
        continue

    key, value = parts
    try:
        count = int(value)
    except ValueError:
        continue

    # key = "annee_sexe_prenom"
    elems = key.split('_', 2)
    if len(elems) != 3:
        continue
    year, sexe, prenom = elems
    groups[(year, sexe)].append((prenom, count))

# pour chaque (annee, sexe), trier et garder Top 5
for (year, sexe) in sorted(groups):
    top5 = sorted(groups[(year, sexe)], key=lambda x: x[1], reverse=True)[:5]
    for prenom, count in top5:
        # emet : annee\tsexe\tprenom\ttotal
        sys.stdout.write("%s\t%s\t%s\t%d\n" % (year, sexe, prenom, count))

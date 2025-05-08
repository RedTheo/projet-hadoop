#!/usr/bin/env python3
# validation.py
# Prétraitement et validation des données
# Lit directement nat2022.csv et écrit nat2022_valid.csv

import csv

def validate():
    # Ouvre en latin-1 pour respecter l'encodage des fichiers INSEE
    with open('dpt2022.csv', mode='r', newline='', encoding='latin-1') as f_in, \
         open('dpt2022_valid.csv', mode='w', newline='', encoding='latin-1') as f_out:

        reader = csv.reader(f_in, delimiter=';')
        writer = csv.writer(f_out, delimiter=';')

        first = True
        for row in reader:
            if first:
                first = False
                continue  # ignorer l'en-tête

            # Vérifier qu'il y a exactement 5 champs
            if len(row) != 5:
                continue

            # Supprimer les espaces superflus
            sexe, preusuel, annais, dept, nombre = [r.strip() for r in row]

            # Aucun champ ne doit être vide
            if not (annais and preusuel and sexe and nombre and dept):
                continue
            if (preusuel == '_PRENOMS_RARES' or preusuel == 'XXXX'):
                continue
            if (annais == 'XXXX'):
                continue
            if(dept == 'XX'):
                continue

            # Écrire la ligne validée
            writer.writerow([sexe, preusuel, annais, dept, nombre])

if __name__ == '__main__':
    validate()
#!/usr/bin/env python3
# mapper.py

import csv

def map_records():
    with open('dpt2022_valid.csv', mode='r', newline='', encoding='latin-1') as f_in, \
         open('dpt2022_mapped.csv', mode='w', newline='', encoding='latin-1') as f_out:

        reader = csv.reader(f_in, delimiter=';')
        writer = csv.writer(f_out, delimiter='\t')

        for row in reader:
            sexe, preusuel, annais, _, nombre = [r.strip() for r in row]

            key = f"{annais}_{sexe}_{preusuel}"

            writer.writerow([key, nombre])

if __name__ == '__main__':
    map_records()
#!/usr/bin/env python3
# reducer.py
# Lit nat2022_mapped.csv et produit nat2022_reduced.csv par agrégation locale

import csv

def reducer(input_path='dpt2022_mapped.csv', output_path='dpt2022_reduced.csv'):
    with open(input_path, mode='r', newline='', encoding='latin-1') as f_in, \
         open(output_path, mode='w', newline='', encoding='latin-1') as f_out:

        reader = csv.reader(f_in, delimiter='\t')
        writer = csv.writer(f_out, delimiter='\t')

        current_key = None
        total = 0

        for row in reader:
            if len(row) != 2:
                continue
            key, value = row
            try:
                count = int(value)
            except ValueError:
                continue

            if key == current_key:
                total += count
            else:
                if current_key is not None:
                    writer.writerow([current_key, total])
                current_key = key
                total = count

        if current_key is not None:
            writer.writerow([current_key, total])

if __name__ == '__main__':
    reducer()
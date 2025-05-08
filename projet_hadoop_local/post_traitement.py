#!/usr/bin/env python3
# post_traitement.py

import csv
from collections import defaultdict

def post_process(input_path='dpt2022_reduced.csv', output_path='dpt2022_top5.csv'):
    groups = defaultdict(list)
    with open(input_path, mode='r', newline='', encoding='latin-1') as f_in:
        reader = csv.reader(f_in, delimiter='\t')
        for row in reader:
            if len(row) != 2:
                continue
            key, value = row
            try:
                count = int(value)
            except ValueError:
                continue
            year, sexe, prenom = key.split('_', 2)
            groups[(year, sexe)].append((prenom, count))

    # Trier et garder le Top 5
    with open(output_path, mode='w', newline='', encoding='latin-1') as f_out:
        writer = csv.writer(f_out, delimiter='\t')
        for (year, sexe) in sorted(groups):
            entries = groups[(year, sexe)]
            top5 = sorted(entries, key=lambda x: x[1], reverse=True)[:5]
            for prenom, count in top5:
                writer.writerow([year, sexe, prenom, count])

if __name__ == '__main__':
    post_process()

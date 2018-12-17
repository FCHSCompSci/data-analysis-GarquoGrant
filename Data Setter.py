# Importations
import csv
from matplotlib import pyplot as plt


filename = 'videogame_sales.csv'
with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = []
    for column in reader:
        high = round(float(column[5]), 2)
        highs.append(column[5])
    print(highs)

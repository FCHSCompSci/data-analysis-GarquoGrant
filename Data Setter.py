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
        # highs.sort()
    print(highs)

fig = plt.figure(dpi=94, figsize= (10, 6))
plt.plot(highs, c='red')

plt.title("Earnings from Video Game Companies")
plt.xlabel('', fontsize=16)
plt.ylabel("Sales (Millions)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
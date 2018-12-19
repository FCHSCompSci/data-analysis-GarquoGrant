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
y = [0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4]
fig = plt.figure(dpi=85, figsize= (10, 6))
plt.plot(highs, c='red')
plt.title("Shooting Games NA Earnings from 1980-2016")
plt.xlabel('', fontsize=16)
plt.ylabel("Sales (Millions)", fontsize=16, )
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
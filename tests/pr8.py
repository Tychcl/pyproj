import math
import numpy as np
import scipy.stats as ss

str = "-15.536759561549772 38.32170754074998 23.984390321619106 41.70031043865848 24.196416554118837 8.84854586854787 15.672022774882915 25.156338429489658 25.78195655961498 15.840082180913008 18.918950055298044 8.476208401765913 15.581686621918074 45.59331139865343 25.68817196198363 28.30492002407349 22.717604530299603 14.909774578403649 20.891951574672273 4.484215747004438 32.33346798255519 32.508346197545436 38.915099381033606 54.09421163869851 20.4644372976311 26.111486302016026 12.079817861042978 17.7705584750976 26.715694289339883 13.925096033532041 34.09710750420216 24.378904222157235 35.698017288940285 19.338600814337013 25.359968744433516 20.602701539217524 26.653833603126404 38.28262544183859 17.78761543281003 10.539248726988205 25.15592065754991 42.62872894690214 26.83432732495953 16.83506857480339 31.41486546097367 24.159720873587744 27.05943814616417 22.00635364954367 -3.223695658827811 23.61623847735759 14.981360471391516 5.061000896391981 28.47094065679889 15.396624008844327 1.2403921874805235 30.342062881979498 29.0745232090532 38.926062525676116 28.22274916981804 30.25650121273785 19.704453737806787 26.151748251161834 14.600748611230348 26.366441006268673 5.299887417037862 24.984849144201497 18.400430595815752 19.991031390046 13.92297113618965 17.790207766163398 20.410787667996225 9.773818589544504 21.975388160510224 23.62842638259111 28.73796428290601 25.40941537431607 14.030902586657392 34.766713405797965 28.885340236154946 4.04026138102946"
mas = sorted(list(map(lambda z: round(float(z),2), str.split(" "))))
Xmax = max(mas)
Xmin = min(mas)
n = len(mas)
#1)
R = Xmax - Xmin
h = round(R/(1+ math.log2(n)),2)
#2)
intervals = np.arange(Xmin, Xmax + h, h)
#3)
# Определение эмпирических частот
hist, bin_edges = np.histogram(mas, bins=intervals)

# Объединение интервалов, если частота меньше 5
def merge_intervals(hist, bin_edges):
    new_hist = []
    new_edges = [bin_edges[0]]
    i = 0
    while i < len(hist):
        if hist[i] < 5 and i < len(hist) - 1:
            new_hist.append(hist[i] + hist[i + 1])
            new_edges.append(bin_edges[i + 2])
            i += 2
        else:
            new_hist.append(hist[i])
            new_edges.append(bin_edges[i + 1])
            i += 1
    return np.array(new_hist), np.array(new_edges)

hist, bin_edges = merge_intervals(hist, bin_edges)

print(f"Xmax = {Xmax}; Xmin = {Xmin}")
print(f"1) R = {R} h = {h}")
print("2) Интервалы:", intervals)
print("3) Эмпирические частоты:", hist)
print("Интервалы после объединения:", bin_edges)
for i in range(len(bin_edges)-1):
    print(f"{round(bin_edges[i],2)} ; {round(bin_edges[i+1],2)} | {round((bin_edges[i] + bin_edges[i+1])/2,2)} | {hist[i]}")
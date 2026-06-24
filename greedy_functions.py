import csv
import numpy as np

with open("NVDIA_Stock_Data.csv", "r") as f:
    next(f) 
    data = csv.reader(f)
    NVIDIA = []
    for row in data:
        NVIDIA.append(float(row[4]))

with open("AMD_Stock_Data.csv", "r") as c:
    next(c) 
    data = csv.reader(c)
    AMD = []
    for row in data:
        AMD.append(float(row[4]))
print(f"Number of days analyzed: {len(NVIDIA)}\n")

print(f"Range of NVIDIA stock prices: {round(max(NVIDIA) - min(NVIDIA), 3)}")
print(f"Range of AMD stock prices: {round(max(AMD) - min(AMD), 3)}\n")

meanNVIDIA = round(sum(NVIDIA)/len(NVIDIA), 3)
meanAMD = round(sum(AMD)/len(AMD), 3)
print(f"Mean of NVIDIA stock prices: {meanNVIDIA}")
print(f"Mean of AMD stock prices: {meanAMD}\n")

varNVIDIA = round(sum((x - meanNVIDIA) ** 2 for x in NVIDIA) / len(NVIDIA), 3)
varAMD = round(sum((x - meanAMD) ** 2 for x in AMD) / len(AMD), 3)
print(f"Variance of NVIDIA stock prices: {varNVIDIA}")
print(f"Variance of AMD stock prices: {varAMD}\n")

print(f"Standard Deviation of NVIDIA stock prices: {round(varNVIDIA ** 0.5, 3)}")
print(f"Standard Deviation of AMD stock prices: {round(varAMD ** 0.5, 3)}\n")

print(f"IQR of NVIDIA stock prices: {round(np.percentile(NVIDIA, 75) - np.percentile(NVIDIA, 25), 3)}")
print(f"IQR of AMD stock prices: {round(np.percentile(AMD, 75) - np.percentile(AMD, 25), 3)}")
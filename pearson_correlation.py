import csv
import math

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

sumNA = 0
sumN = 0
sumA = 0
sumNN = 0
sumAA = 0
n = len(NVIDIA)
for i in range(n):
    sumNA += NVIDIA[i] * AMD[i]
    sumN += NVIDIA[i]
    sumA += AMD[i]
    sumNN += NVIDIA[i] * NVIDIA[i]
    sumAA += AMD[i] * AMD[i]
meanN = sumN/n
meanA = sumA/n
pearson = ((n * sumNA) - (sumN * sumA)) / math.sqrt((n * sumNN - sumN ** 2) * (n * sumAA - sumA ** 2))
print(pearson)
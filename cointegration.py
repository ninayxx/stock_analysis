import numpy as np
import statsmodels.tsa.stattools as ts
import csv


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

coint_t, p_value, critical_values = ts.coint(NVIDIA, AMD)

print(f"t-statistic: {coint_t}")
print(f"p-value: {p_value}")
print(f"Critical Values: {critical_values}")
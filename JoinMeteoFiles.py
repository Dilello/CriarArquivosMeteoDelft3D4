# version 2
# Marcelo Di Lello Jordão
# 
# AVIABLE FUNCTIONS:
# DISPLAY INFORMATION ABOUT INPUT NETCDF FILE AND AVIABLE DATA
# READ DATA FROM NC FILE USING NETCDF4 PYTHON LIBRARY
# CREATE INPUT FILES OF METEOROLOGICAL (OPTIONALY) DATA FOR DELTARES DELFT3D MODEL IN PROPER FORMAT
# 
# AVIABLE METEO FILES DATA UNITS:
# AIR TEMPERATURE (2 METER UNDER WATER SURFACE) (.AMT)
# RELATIVE HUMIDITY (.ARN)
# CLOUDNESS (.AMC)
# U-DIRECTION WIND (2 METER UNDER WATER SURFACE) (.AMU)
# V-DIRECTION WIND (2 METER UNDER WATER SURFACE) (.AMV)
# AIR PRESSURE (.AMP)
# 
import sys
import numpy as np
import pandas as pd

print('Save first month file as MSLcompleteFile.amp, U10McompleteFile.amu, etc ')
year_start = int(input('Input year start SECOND month run (YYYY): '))
year_end = int(input('Input year end run (YYYY): '))
month_start = int(input('Input month start SECOND month run (number: 1, 2, ..., 11, 12): '))
month_end = int(input('Input month end run (number: 1, 2, ..., 11, 12): '))
years_run = np.arange(year_start, year_end+1, 1)
if (month_end == 12): month_end1 = 1
if (month_end == 12): year_end1 = year_end + 1
if (month_end < 12): month_end1 = month_end + 1
if (month_end < 12): year_end1 = year_end
months = pd.date_range(start = str(year_start)+'-'+str(month_start),end = str(year_end1)+'-'+str(month_end1), freq = 'M')
months_run = np.array(months.month)
years_run = np.array(months.year)
var_run = []
# number of elements as input
n_elem = int(input("Enter number of variables : "))
# iterating till the range
for i in range(0, n_elem):
    elem = str(input("Enter variables (MSL, U10M, V10M, ...): "))
    # adding the element
    var_run.append(elem) 
 
print(var_run)

for ivar_run in var_run:

    for i in range(0,len(months_run)):

        if (ivar_run == 'U10M'): fmt = '.amu'
        if (ivar_run == 'V10M'): fmt = '.amv'
        if (ivar_run == 'MSL'): fmt = '.amp'
        if (ivar_run == 't2m'): fmt = '.amt'
        if (ivar_run == 'mcc'): fmt = '.amc'
        if (ivar_run == 'rh'): fmt == '.amr'

        completeFileID = ivar_run + 'completeFile' + fmt
        
        try:
            file_chk = open(completeFileID)
        except FileNotFoundError:
            sys.exit('\nERROR! input completeFile not found')

        with open(completeFileID, 'r') as f:
            file1 = f.read().split("\n")

        fileID = ivar_run + '_' + str(years_run[i]) + str(months_run[i]).zfill(2) + fmt

        try:
            file_chk = open(fileID)
        except FileNotFoundError:
            sys.exit('\nERROR! input file not found')

        with open(fileID, 'r') as f:
            file2 = f.read().split("\n")

        lines = file2[13:]
        vertically = "\n".join(file1 + lines)

        textJoin = open(completeFileID, 'w')
        textJoin.write(vertically)
        textJoin.close()


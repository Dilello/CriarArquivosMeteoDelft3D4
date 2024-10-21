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
# NETCDF4 WAS DOWNLOADED FROM ECMWF ERA REANALYS DATABASE
# http://apps.ecmwf.int/datasets/data/interim-full-daily/levtype=sfc/
# 

import sys
import numpy as np
import pandas as pd
from netCDF4 import Dataset

print('\nstart read .nc file\n')

year_start_model = int(input('Input year from Reference Date - Delft3D4 (YYYY): '))
year_start = int(input('Input year start run (YYYY): '))
year_end = int(input('Input year end run (YYYY): '))
month_start = int(input('Input month start run (number: 1, 2, ..., 11, 12): '))
month_end = int(input('Input month end run (number: 1, 2, ..., 11, 12): '))
day_end = int(input('Input day end run (number: 1, 2, ..., 30, 31): '))
years_run = np.arange(year_start, year_end+1, 1)
months_run = np.arange(month_start, month_end+1, 1)
var_run = []
# number of elements as input
n_elem = int(input("Enter number of variables (1, 2, 3, ...): "))
# iterating till the range
for i in range(0, n_elem):
    elem = str(input("Enter variables (MSL, U10M, V10M, ...): "))
    # adding the element
    var_run.append(elem) 
 
print(print(var_run))
timeH = pd.date_range(start = str(year_start_model)+'-1-1 00:00', end = str(year_end)+'-'+str(month_end)+'-'+str(day_end)+' 23:00', freq = "H")
countH = pd.DataFrame()
countH['timeH'] = timeH
listH = np.arange(0,len(countH),1)
countH['listH'] = listH
countH.index = timeH
countH1 = countH.asfreq('MS')
countH2 = countH1.loc[str(year_start)+'-'+str(month_start)+'-1':str(year_end)+'-'+str(month_end)+'-1']

for ivar_run in var_run:
    for iyear in years_run:
        for imonth in months_run:
            nc_fileID = ivar_run + '_Y' + str(iyear) + 'M' + str(imonth) + '.nc'
            try:
                file_chk = open(nc_fileID)
            except FileNotFoundError:
                sys.exit('\nERROR! file not found')

            # READ NETCDF FILE AND PRINT AVIABLE VARIABLES
            root = Dataset(nc_fileID)
            print(root)
            dims = root.dimensions
            ndims = len(dims)

            dic = {}
            dic2 = {}
            print('\navailable variables in selected .NC file:\n')
            vars = root.variables
            print(vars)
            nvars = len(vars)
            n = 0
            for var in vars:
                # sys.stdout.write('-'+var+' ')
                print('#',n,'   ',var, vars[var].shape)
                dic[str(var)] = n
                l = vars[var].shape
                dic2[str(var)] = len(l)
                n += 1
            print('\n')
            # INPUT VARIABLES THAT YOU WANT TO READ
            nc_data = []
            iter_var = []
            iter_var.append(ivar_run.split(' '))
            iter_var = iter_var[0]
            try:
                for v in iter_var:
                    dic[v]
            except KeyError:
                sys.exit('\nvariable name error\n')

            # WARNING!
            # MAX DIMENSIONS OF MASSIVE: 3

            var_inter_n = {}
            ni = 0
            for i in iter_var:
                if (dic2[i] == 1):
                    nc_data.append(np.array(root.variables[i][:], dtype=np.float32))
                if (dic2[i] == 2):
                    nc_data.append(np.array(root.variables[i][:,:], dtype=np.float32))
                if (dic2[i] == 3):
                    nc_data.append(np.array(root.variables[i][:,:,:], dtype=np.float32))
                var_inter_n[i] = ni
                ni += 1

            print('\nread complete\n')

            outfile2_name = 'uvsp_grd.dat'
            outfile2 = open(outfile2_name, 'w')
            for i in range((len(root.variables['lon']))):
                for j in range(len(root.variables['lat'])):
                    outfile2.write(str(root.variables['lon'][i])+'    '+str(root.variables['lat'][j])+'\n')
            print('wind grid write complete')
            # USING CONST LIST
            nodata_value = -999.000
            grid_unit = 'degree' #  m or degree
            longitude_name = 'lon'
            latitude_name = 'lat'
            time_name = 'time'
            n_quantity = 1
            fmt = '.dat'

            for i in iter_var:

                # LIST OF AVIABLE OUTPUT DATA FOR DELFT3D METEO INPUT FILES
                if (i == 'U10M'): fmt = '.amu'
                if (i == 'V10M'): fmt = '.amv'
                if (i == 'MSL'): fmt = '.amp'
                if (i == 't2m'): fmt = '.amt'
                if (i == 'mcc'): fmt = '.amc'
                if (i == 'rh'): fmt == '.amr'
                outfile_name = str(i)+'_'+str(iyear)+str(imonth).zfill(2)+fmt
                outfile = open(outfile_name, 'w')
                outfile.write('FileVersion = 1.03\n')
                outfile.write('filetype = meteo_on_equidistant_grid\n')
                outfile.write('NODATA_value = '+str(nodata_value)+'\n')
                n_cols = vars[i].shape[2]
                outfile.write('n_cols = '+str(n_cols)+'\n')
                n_rows = vars[i].shape[1]
                outfile.write('n_rows = '+str(n_rows)+'\n')
                outfile.write('grid_unit = '+str(grid_unit)+'\n')
                x_llcorner = root.variables[longitude_name][0]
                y_llcorner = root.variables[latitude_name][-1]
                outfile.write('x_llcorner = '+str(x_llcorner)+'\n')
                outfile.write('y_llcorner = '+str(y_llcorner)+'\n')
                dy = (root.variables[longitude_name][-1] - root.variables[longitude_name][0]) / (n_cols - 1) # REVISAR ISSO
                dx = (root.variables[latitude_name][0] - root.variables[latitude_name][-1]) / (n_rows - 1) # REVISAR ISSO
                outfile.write('dx = '+str(dx)+'\n')
                outfile.write('dy = '+str(dy)+'\n')
                outfile.write('n_quantity = '+str(n_quantity)+'\n')
                quantity1 = '???'
                unit1 = '???'
                if (i == 'U10M'):
                    quantity1 = 'x_wind'
                    unit1 = 'm s-1'
                elif (i == 'V10M'):
                    quantity1 = 'y_wind'
                    unit1 = 'm s-1'
                elif (i == 'MSL'):
                    quantity1 = 'air_pressure'
                    unit1 = 'Pa'
                if (i == 't2m'):
                    quantity1 = 'air_temperature'
                    unit1 = 'Celsius'
                if (i == 'mcc'):
                    quantity1 = 'cloudiness'
                    unit1 = '%'
                outfile.write('quantity1 = '+quantity1+'\n')
                outfile.write('unit1 = '+unit1+'\n')
                time1 = 0

                inicio0 = countH2.listH.loc[str(iyear)+'-'+str(imonth)+'-1']
                fim0 = countH.listH.loc[str(year_end)+'-'+str(month_end)+'-'+str(day_end)+' 23:00']

                newcount = np.arange(inicio0,fim0+1,1)
                # WRITE DATA IN FILE
                for t in range(len(countH.loc[str(iyear)+'-'+str(imonth)])):
                    # time1 = root.variables[time_name][t]
                    outfile.write('TIME = ' + str(newcount[t]) + ' hours since 2018-01-01 00:00:00 +00:00\n')
                    # FOR SINGLE MONTH WRITE USE THIS:
                    for n in range(int(vars[i].shape[1])):
                        for m in range(int(vars[i].shape[2])):
                            if i == 't2m':
                                outfile.write(str(nc_data[var_inter_n[i]][t, n, m] - 273.150)+' ')
                            else:
                                outfile.write(str(nc_data[var_inter_n[i]][t, n, m])+' ')
                        outfile.write('\n')
                    time1 += 6
                print('done')

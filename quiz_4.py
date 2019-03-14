# Uses Heath Nutrition and Population statistics,
# stored in the file HNP_Data.csv.gz,
# assumed to be located in the working directory.
# Prompts the user for an Indicator Name. If it exists and is associated with
# a numerical value for some countries or categories, for some the years 1960-2015,
# then finds out the maximum value, and outputs:
# - that value;
# - the years when that value was reached, from oldest to more recents years;
# - for each such year, the countries or categories for which that value was reached,
#   listed in lexicographic order.
# 
# Written by *** and Eric Martin for COMP9021


import sys
import os
import csv
import gzip


filename = 'HNP_Data.csv.gz'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

indicator_of_interest = input('Enter an Indicator Name: ')

first_year = 1960
number_of_years = 56
max_value = None
countries_for_max_value_per_year = {}

with gzip.open(filename) as csvfile:
    reader = csv.reader(line.decode('utf8').replace('\0', '') for line in csvfile)
    next(reader)
    linenum = 0
    for i in reader:
        if len(i) == 0:
            continue
        linenum += 1
        if i[2] != indicator_of_interest:
            continue
        for j in range(number_of_years):
            if i[j+4] is '':
                continue
            t_int = float(i[j+4])
            if max_value is None:
                max_value = t_int
            elif t_int < max_value:
                continue
            elif t_int > max_value:
                max_value = t_int
                countries_for_max_value_per_year.clear()
            countries_for_max_value_per_year.setdefault(j+first_year, list()).append(i[0])
    max_value = round(max_value) if round(max_value, 1) == round(max_value) else round(max_value, 1)

if max_value is None:
    print('Sorry, either the indicator of interest does not exist or it has no data.')
else:
    print('The maximum value is:', max_value)
    print('It was reached in these years, for these countries or categories:')
    print('\n'.join(f'    {year}: {countries_for_max_value_per_year[year]}'
                                  for year in sorted(countries_for_max_value_per_year)
                   )
         )

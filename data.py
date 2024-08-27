
'''
The Data Builder
by @jack-pittman
'''
# DESCRIPTION
# 
# This program takes a csv file and turns its contents into a nested list. 

import csv
from utilities import width_to_letter_coordinate, is_float, convert_stringified_numbers

# converts csv to nested list, then 'flips' rows and columns
def transpose_csv(file_path):
    transposed_data = []
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        data = [tuple(row) for row in reader]
        
        # Transpose the data
        transposed_data = list(zip(*data))
        
    return transposed_data

file_path = 'BUCKETS/USER - PROD./costs.csv'
# file_path = 'BUCKETS/USER - STAG. HERE/costs.csv'

# CALL FUNCTION AND POPULATE WRANGLED_DATA 
# –––––>> Also note that 'convert_stringified_numbers' is called, 
#         which converts all elements into floats that can be converted 
#         into floats. 

def get_data(file_path):
    wrangled_data = convert_stringified_numbers(transpose_csv(file_path))
    # print(wrangled_data)
    return wrangled_data
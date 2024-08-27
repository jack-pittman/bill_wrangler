'''
COGS Bill Wrangler
by @jack-pittman
'''
from data import get_data 
from utilities import width_to_letter_coordinate, letter_to_bucket, get_sheets, get_filepaths
from input_handler import get_user_input
from api_manager import workbook

# GET USER DATA 
selected_bucket = get_user_input()

# GET CORRECT WORKSHEET NAME FROM USER INPUT 
sheet = workbook.worksheet(letter_to_bucket(selected_bucket, get_sheets()))

# RETRIEVE DATA LOCALLY FROM CORRECT FOLDER
wrangled_data = get_data(letter_to_bucket(selected_bucket, get_filepaths()))

# BUILD NESTED ARRAY USING WRANGLED DATA
table_content = []

for i in range(len(wrangled_data)):
    table_content.append(sheet.row_values(i+1))

# GET LETTER COORDINATE VALUE FOR WIDTH (i.e. 3 –> C)
data_width_let = width_to_letter_coordinate(len(wrangled_data[0]))

# UPDATE SHEET 
sheet.update(f"A1:{data_width_let}{len(wrangled_data)}", wrangled_data)
print('\n\nSHEET UPDATED!')

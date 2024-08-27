# SHEETS API STUFF 
import gspread
from google.oauth2.service_account import Credentials

# define access
scopes = ["https://www.googleapis.com/auth/spreadsheets"]

# retreive necessary credentials from json file
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)

# authorize ourselves 
client = gspread.authorize(creds)

# set sheet ID (findable inside URL)
sheet_id = "1bO1-l0yFy8hjM17b41QQrQHuI0yNif_3MpfuFDagcW0"

# now that we have authorization and the sheet ID, we can open the sheet! Let's go!
# FUN FACT: you can also open by url, sheetname, etc. 
workbook = client.open_by_key(sheet_id)

sheets = map(lambda x: x.title, workbook.worksheets())
# print('\n\n', list(sheets))

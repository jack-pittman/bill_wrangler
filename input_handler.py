welcome = '''
WELCOME TO BILL WRANGLER

To get started, you need to download 4 .csv files from Amazon 
Cost Explorer. First, set the data range at 6 months (this 
will save you from scary spreadsheet errors). Next, apply the 
following filters, downloading a copy of the filtered data 
each time.

   1. Filter by user: Nish/Production ONLY
   2. Filter by user: Staging ONLY
   3. Filter by Region: US/East ONLY
   4. Filter by Region: US/West ONLY

Drag each .csv file into the appropriate BUCKET. Once you have
done this, you are ready to start! 

_________

Which sheet would you like to update? 

    a) Production
    b) Staging
    c) US/East
    d) US/West
'''

options = ['a','b','c','d']

def get_user_input():

    print(welcome)
    
    answer = ""

    while answer not in options:
        answer = input("Please enter a lowercase letter. ")

    print("Your answer was:", answer)

    return answer
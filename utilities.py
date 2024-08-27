def width_to_letter_coordinate(num):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    return alphabet[num-1]

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def convert_stringified_numbers(nested_list):
    converted_list = []
    for sublist in nested_list:
        converted_sublist = []
        for item in sublist:
            if isinstance(item, str) and is_float(item):
                converted_sublist.append(float(item))
            else:
                converted_sublist.append(item)
        converted_list.append(converted_sublist)
    return converted_list

def get_sheets():
    return ["Production", "Staging", "East", "West"]

def get_filepaths():
    return [
        "BUCKETS/USER - PROD./costs.csv", 
        "BUCKETS/USER - STAG./costs.csv",
        "BUCKETS/REGION - EAST/costs.csv",
        "BUCKETS/REGION - WEST/costs.csv"
    ]

def letter_to_bucket(letter, buckets):

    if letter == "a":
        return buckets[0]
    if letter == "b":
        return buckets[1]
    if letter == "c":
        return buckets[2]
    if letter == "d":
        return buckets[3]
    
    return "ERROR"
    
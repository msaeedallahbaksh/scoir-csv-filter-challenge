import os
import pandas as pd 


def filter_csv(file_name):
    # read csv file
    df = pd.read_csv(file_name, dtype=str)
    filter_type, filter_value = get_filter()

    # check if value is in the given columnexa
    if not filter_value in df[filter_type].unique():
        return f'There is no {filter_value} value for the given filter in the CSV file'

    # get all records containing value
    record = df.query("{0} == @filter_value".format(filter_type))
    return record 

# ask user for CSV file 
def get_file():
    while True:
        file = input("Please enter the name of the CSV file.\n")
        if os.path.exists(file):
            return file
        print("This CSV file does not exist.")

def get_filter():
    while True:
        prompt_filter_type = input("Would you like to filter by first name, last name, or birth year?\n")
        filter_type = prompt_filter_type.lower().strip()
        if filter_type == "first name":
            filter_type = "first_name"
            break
        elif filter_type == "last name":
            filter_type = "last_name"
            break
        elif filter_type == "birth year":
            filter_type = "dob"
            break       
    
    #handles any exception cases and reloops
        print("That is not a valid filter option.")

    filter_value = input(f'Please provide the {prompt_filter_type.lower().strip()}\n')
    return filter_type, filter_value


file_name = get_file()
print(filter_csv(file_name))

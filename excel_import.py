import pandas as pd
import os

# Define the directory where your Excel files are located
data_path = "/Users//niallwhelan/Projects/excelpro/excelpro/data"
analysis_path = "/Users//niallwhelan/Projects/excelpro/excelpro/analysis"


def check_data_path(data_path):
    if os.path.exists(os.path.join(data_path, 'example1_us.xlsx')):  # This exmaple file is too specific for a test, need to change.
        print('Excel files found...')
    else:
        print('no excel files found.. check the path')
        exit(1)


def load_excel_files(data_path):
    # Get a list of all the Excel files in the directory
    excel_files = [f for f in os.listdir(data_path) if f.endswith('.xlsx')]
    return excel_files


def check_analysis_path(analysis_path):
    # Check if the directory exists, and create it if it doesn't
    if not os.path.exists(analysis_path):
        os.makedirs(analysis_path)


def format_excel_data(excel_files):
    # Create an empty list to hold the data from each Excel file
    data_list = []

    # Loop through each Excel file, load the first sheet into a Pandas dataframe, and append it to the data_frames list
    for file in excel_files:
        file_path = os.path.join(data_path, file)
        excel_data = pd.read_excel(file_path, sheet_name=0, header=0)
        data_list.append(excel_data)
    return data_list

def merge_excel_data(data_row_list):
    # Concatenate all the list of data rows into a single dataframe
    df = pd.concat(data_row_list, axis=0)
    return df

def write_merged_data_to_csv(merged_data, output_path):
    # Write the merged data to a CSV file
    merged_data.to_csv(output_path, index=False)


check_data_path(data_path)
check_analysis_path(analysis_path)
 
# Define the output file name and path
output_file = "output.csv"
output_path = os.path.join(analysis_path, output_file)

excel_files = load_excel_files(data_path)

# Create an empty list to hold the data from each Excel file
data_row_list = format_excel_data(excel_files)

# Concatenate all the list of data rows into a single dataframe
merged_data = merge_excel_data(data_row_list)

# Write the merged data to a CSV file
write_merged_data_to_csv(merged_data, output_path)


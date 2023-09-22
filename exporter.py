"""
exporter.py

Contains relevent functions in exporting data.

:author: Jerry Chen
:email: jerryvc@uci.edu
"""

import csv
import json

def export_to_csv(json_data, filename='.\output\output.csv'):
    """
    Export the parsed data to a CSV file.

    :param json_data: JSON string containing a list of dictionaries with the parsed data.
    :type json_data: str
    :param filename: The name of the CSV file to which the data should be written.
    :type filename: str
    """
    data = json.loads(json_data)  # Load JSON string to Python list of dictionaries
    
    header = data[0].keys() if data else []
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        
        writer.writeheader()  # write the header to the CSV file
        writer.writerows(data)  # write the data rows to the CSV file


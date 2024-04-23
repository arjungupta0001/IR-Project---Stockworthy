import os
import pandas as pd

def process_value(value):
    # This is a placeholder function, you can replace it with your actual processing logic
    processed_value = value.upper()
    return processed_value

def process_csv_file(file_path):
    df = pd.read_csv(file_path)
    value = df.iloc[0]['C']  # Assuming 'C' is the column you want to extract from the first row
    processed_value = process_value(value)
    os.remove(file_path)  # Remove the CSV file after processing
    return processed_value

csv_dir = '/home/ankush-gupta/Downloads'
while True:
    csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]
    for csv_file in csv_files:
        file_path = os.path.join(csv_dir, csv_file)
        result = process_csv_file(file_path)
        print(f"Processed value: {result}")

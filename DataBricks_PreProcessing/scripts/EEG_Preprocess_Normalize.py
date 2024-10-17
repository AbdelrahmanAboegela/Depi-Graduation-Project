import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the Excel file
folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = folder_path + '/../raw_data/EEG (EO, AC1, AC2).xlsx'  # Replace with your actual file path

# Load the 'Non Normalize' sheet
df = pd.read_excel(file_path, sheet_name='Normalize')

print(df)

# Drop the first row that contains extra headers (electrode positions)
eeg_data = df.drop([0]).reset_index(drop=True)

# Extract the proper column names using the headers from the first row of the sheet
header_rows = pd.read_excel(file_path, sheet_name='Normalize').iloc[0, :]

# Define the correct frequency bands and electrodes for renaming
frequency_bands = ['Delta (1-4 Hz)', 'Theta (4-8 Hz)', 'Alpha (8-12 Hz)', 'Beta 1 (12-20 Hz)', 'Beta 2 (20-30 Hz)', 'Gamma (30-60 Hz)', 'Gamma 2 (60-100 Hz)']
electrodes = ['Fp1', 'Fp2', 'F3', 'F4', 'T3', 'T4', 'P3', 'P4']

# Create the final column names with the correct format
new_column_names = ['Segment', 'Subject NO.', 'Gender']

for band in frequency_bands:
    for electrode in electrodes:
        new_column_names.append(f'{electrode}_{band}')

# Apply the new column names
eeg_data.columns = new_column_names[:len(eeg_data.columns)]

# Correct the "Segment" column for 40 participants across three phases (EO, AC1, AC2)
num_subjects = 40
phases = ['EO', 'AC1', 'AC2']
segment_column = [phase for phase in phases for _ in range(num_subjects)]

# Assign the new 'Segment' column
eeg_data['Segment'] = segment_column[:len(eeg_data)]

# Final cleaned EEG data
eeg_data_cleaned = eeg_data

print(eeg_data_cleaned)

# Preprocessed and Normalized CSV file 
path = f'{folder_path}' 
eeg_data_cleaned.to_csv(path + '/../preprocessed_data/Preprocessed_EEG_Data_Normalized.csv', index=False) 

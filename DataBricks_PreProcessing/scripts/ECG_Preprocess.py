import os
import pandas as pd

# Load the Excel file
folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = folder_path + '/../raw_data/ECG (EO, AC1, AC2).xlsx'  # Replace with your actual file path

# Load the ECG data from the specified file with different sheets
ecg_eo = pd.read_excel(file_path, sheet_name='EO')
ecg_ac1 = pd.read_excel(file_path, sheet_name='AC1')
ecg_ac2 = pd.read_excel(file_path, sheet_name='AC2')

# Add prefixes to the column names to indicate the period
ecg_eo = ecg_eo.add_prefix('EO_')
ecg_ac1 = ecg_ac1.add_prefix('AC1_')
ecg_ac2 = ecg_ac2.add_prefix('AC2_')

# Rename the subject number and gender columns back to their original names for joining
ecg_eo = ecg_eo.rename(columns={'EO_Subject NO.': 'Subject NO.', 'EO_Gender': 'Gender'})
ecg_ac1 = ecg_ac1.rename(columns={'AC1_Subject NO.': 'Subject NO.', 'AC1_Gender': 'Gender'})
ecg_ac2 = ecg_ac2.rename(columns={'AC2_Subject NO.': 'Subject NO.', 'AC2_Gender': 'Gender'})

# Merge the data on the 'Subject NO.' and 'Gender' columns
ecg_merged = ecg_eo.merge(ecg_ac1.drop(columns=['Gender']), on='Subject NO.', how='outer') \
                    .merge(ecg_ac2.drop(columns=['Gender']), on='Subject NO.', how='outer')

# Columns without segment prefixes
columns_without_segment = ['Subject NO.', 'Gender']

# Define the order of the columns as per your provided format
final_column_order = ['Subject NO.', 'Gender', 'Mean HR (BPM)', 'AVNN (ms)', 'SDNN (ms)', 'NN50 (beats)', 
                      'pNN50 (%)', 'RMSSD (ms)', 'LF (ms2)', 'LF Norm (n.u.)', 'HF (ms2)', 
                      'HF Norm (n.u.)', 'LF/HF Ratio', 'Segment']

# Extract the columns for each segment (EO, AC1, AC2)
eo_columns = [col for col in ecg_merged.columns if 'EO_' in col]
ac1_columns = [col for col in ecg_merged.columns if 'AC1_' in col]
ac2_columns = [col for col in ecg_merged.columns if 'AC2_' in col]

# Remove the EO_, AC1_, and AC2_ prefixes from the columns for consistency
eo_data = ecg_merged[columns_without_segment + eo_columns].copy()
ac1_data = ecg_merged[columns_without_segment + ac1_columns].copy()
ac2_data = ecg_merged[columns_without_segment + ac2_columns].copy()

# Rename the columns to standardize "Mean HR (BPM)" for all segments
# Standardize 'Mean HR' column name and handle case insensitivity
eo_data.columns = columns_without_segment + [col.replace('EO_', '').replace('Mean HR (BPM)', 'Mean HR (BPM)').replace('Mean HR (bpm)', 'Mean HR (BPM)') for col in eo_columns]
ac1_data.columns = columns_without_segment + [col.replace('AC1_', '').replace('Mean HR (bpm)', 'Mean HR (BPM)') for col in ac1_columns]
ac2_data.columns = columns_without_segment + [col.replace('AC2_', '').replace('Mean HR (bpm)', 'Mean HR (BPM)') for col in ac2_columns]

# Add a Segment column to each dataset
eo_data['Segment'] = 'EO'
ac1_data['Segment'] = 'AC1'
ac2_data['Segment'] = 'AC2'

# Ensure that the final column order is consistent across all datasets
# Only keep the columns that are present in both the data and the final_column_order
eo_data = eo_data[[col for col in final_column_order if col in eo_data.columns]]
ac1_data = ac1_data[[col for col in final_column_order if col in ac1_data.columns]]
ac2_data = ac2_data[[col for col in final_column_order if col in ac2_data.columns]]

# Concatenate the data for all segments
final_preprocessed_ecg = pd.concat([eo_data, ac1_data, ac2_data], ignore_index=True)

print(final_preprocessed_ecg)

# Preprocessed and Normalized CSV file 
path = f'{folder_path}' 
final_preprocessed_ecg.to_csv(path + '/../preprocessed_data/Preprocessed_ECG_Data.csv', index=False)
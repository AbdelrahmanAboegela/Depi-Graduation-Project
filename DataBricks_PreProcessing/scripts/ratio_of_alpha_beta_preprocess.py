import os
import pandas as pd


# Get the directory of the current file
folder_path = os.path.dirname(os.path.abspath(__file__))

# Path to the normalized Ratio Alpha Beta data
ratio_of_alpha_beta_file_path = f'{folder_path}/../raw_data/Ratio of Alpha _ Beta Power.xlsx'

# Load the normalized data
ratio_alpha_data = pd.read_excel(ratio_of_alpha_beta_file_path, sheet_name = 'Alpha')
ratio_beta1_data = pd.read_excel(ratio_of_alpha_beta_file_path, sheet_name = 'Beta1')
ratio_beta2_data = pd.read_excel(ratio_of_alpha_beta_file_path, sheet_name = 'Beta2')

# Function to drop 12 columns (non-normalized data) after ['Subject (No.)', 'Gender']
def drop_columns(df):
    # Find index of 'Subject (No.)' and 'Gender'
    subject_col_idx = df.columns.get_loc('Subject (No.)')
    gender_col_idx = df.columns.get_loc('Gender')
    
    # Keep 'Subject (No.)', 'Gender' and remove the next 12 columns
    cols_to_keep = list(df.columns[:gender_col_idx + 1]) + list(df.columns[gender_col_idx + 13:])
    
    # Return dataframe with only the required columns
    return df[cols_to_keep]

# Function to preprocess and reshape each sheet for the required structure
def preprocess_and_reshape(df, sheet_name, block_size=40):
    """Preprocess and reshape data from one sheet."""
    
    # Drop the first two rows (metadata) and reset the index
    df = df.drop([0, 1]).reset_index(drop=True)
    
    # Drop the non-normalized columns
    df = drop_columns(df)

    # Ensure the columns are correctly named after the drop
    df.columns = ['Subject NO.', 'Gender', 'EO_Fp 1 - Fp 2', 'EO_F 3 - F 4', 'EO_T 3 - T 4', 'EO_P 3 - P 4',
                  'AC1_Fp 1 - Fp 2', 'AC1_F 3 - F 4', 'AC1_T 3 - T 4', 'AC1_P 3 - P 4',
                  'AC2_Fp 1 - Fp 2', 'AC2_F 3 - F 4', 'AC2_T 3 - T 4', 'AC2_P 3 - P 4']
    
    # Reshape data by periods (EO, AC1, AC2)
    reshaped_data = pd.DataFrame()
    periods = ['EO', 'AC1', 'AC2']
    for period in periods:
        block = df[['Subject NO.', 'Gender',
                    f'{period}_Fp 1 - Fp 2', f'{period}_F 3 - F 4', f'{period}_T 3 - T 4', f'{period}_P 3 - P 4']].copy()
        
        # Rename columns to match the period
        block.columns = ['Subject NO.', 'Gender', f'{sheet_name}_(Fp 1 - Fp 2)', f'{sheet_name}_(F 3 - F 4)',
                         f'{sheet_name}_(T 3 - T 4)', f'{sheet_name}_(P 3 - P 4)']
        
        # Add segment column
        block['Segment'] = period
        
        # Append reshaped period data
        reshaped_data = pd.concat([reshaped_data, block], ignore_index=True)
    
    return reshaped_data



# Preprocess and reshape each sheet
alpha_data = preprocess_and_reshape(ratio_alpha_data, 'Alpha')
beta1_data = preprocess_and_reshape(ratio_beta1_data, 'Beta1')
beta2_data = preprocess_and_reshape(ratio_beta2_data, 'Beta2')

# Merge the three datasets on 'Subject NO.', 'Gender', and 'Segment'
final_df = alpha_data.merge(beta1_data, on=['Subject NO.', 'Gender', 'Segment'])
final_df = final_df.merge(beta2_data, on=['Subject NO.', 'Gender', 'Segment'])

# Move the 'Segment' column to the 3rd position
cols = final_df.columns.tolist()
cols.insert(2, cols.pop(cols.index('Segment')))  # Move 'Segment' to the 3rd position
final_df = final_df[cols]

print(final_df)

# Preprocessed CSV file 
path = f'{folder_path}' 
final_df.to_csv(path + '/../preprocessed_data/Preprocessed_Alpha_Beta_Ratio_1.csv', index=False) 

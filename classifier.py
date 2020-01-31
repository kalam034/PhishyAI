import pandas as pd

import merge_dataframes

training_df = pd.read_csv("training_datasets/merged_dataframes.csv", header = 0)

bn_records = training_df.loc[training_df ['Label'] == 0]
ml_records = training_df.loc[training_df ['Label'] == 1]

print("Total number of records in training dataframe: " + str(training_df.shape[0]))
print("Total number of benign records in training dataframe: + " + str(bn_records.shape[0]))
print("Total number of malicious records in training dataframe: + " + str(ml_records.shape[0]))


    

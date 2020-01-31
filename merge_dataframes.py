import pandas as pd

open_phish_DF = pd.read_csv("training_datasets/open_phish.txt", names=["Url"])
open_phish_DF['Label'] = 0

phish_storm_DF = pd.read_csv("training_datasets/phish_storm.csv", skipinitialspace=True, encoding="ISO-8859-1", low_memory=False, usecols=["domain","label"])
phish_storm_DF.columns = ["Url", "Label"]
phish_storm_DF = phish_storm_DF.drop(phish_storm_DF[(phish_storm_DF.Label !="1.0") & (phish_storm_DF.Label != "0.0")].index)
phish_storm_DF.Label = phish_storm_DF.Label.astype(float)
  
    
unb_phish_DF = pd.read_csv("training_datasets/unb_phish.txt", names=["Url"])
unb_phish_DF["Label"] = 0
      
phish_tank_DF = pd.read_csv("training_datasets/phish_tank.csv", skipinitialspace=True, usecols=["phish_detail_url"])
phish_tank_DF.columns = ["Url"]
phish_tank_DF["Label"] = 0
        
unb_benign_DF = pd.read_csv("training_datasets/unb_benign.txt", names=["Url"])
unb_benign_DF["Label"] = 1

merged_df = pd.concat([open_phish_DF, unb_phish_DF, phish_storm_DF, phish_tank_DF, unb_benign_DF], sort = True, axis=0)

merged_df.to_csv("training_datasets/merged_dataframes.csv", encoding='utf-8', header=True, index=False)
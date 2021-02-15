import pandas as pd

print("=========Dataset loadting will be started!=========")
rv_dataset = pd.read_excel('../data/raw_data/rv_raw_dataset.xlsx')
prep_dataset = pd.read_excel('../data/raw_data/preprocessing.xlsx')
exclude_app_list = pd.read_excel('../data/raw_data/exclude_app_list.xlsx')
print("=========Dataset loadting is completed!=========")
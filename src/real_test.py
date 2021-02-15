import pandas as pd

rv_prep_dataset = pd.read_excel('../data/preprocessed_review/rv_prep_dataset_test.xlsx')

numOfMonth = 36
minNumToken = 3
maxNumToken = 15

print("before: ", len(rv_prep_dataset))

rv_sel_dataset = rv_prep_dataset.loc[rv_prep_dataset['numOfmonth']  <= numOfMonth]
rv_sel_dataset = rv_sel_dataset.loc[rv_sel_dataset['numOfToken'] >= minNumToken]
rv_sel_dataset = rv_sel_dataset.loc[rv_sel_dataset['numOfToken'] <= maxNumToken]

print("after: ", len(rv_sel_dataset))
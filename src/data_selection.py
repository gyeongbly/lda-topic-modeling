import pandas as pd
from data_processing import rv_prep_dataset

numOfMonth = 36
minNumToken = 3
maxNumToken = 15

# To convert types of some columns in the dataframe into integer
rv_prep_dataset['numOfmonth'] = rv_prep_dataset['numOfmonth'].astype('int')
rv_prep_dataset['numOfToken'] = rv_prep_dataset['numOfToken'].astype('int')
rv_prep_dataset['reviewRating'] = rv_prep_dataset['reviewRating'].astype('int')

print("\nThe only review dataset with between {} and {} tokens that were posted within last {} months were selected.\n".format(minNumToken, maxNumToken, numOfMonth))

# To select the dataset fitting several conditions
rv_sel_dataset = rv_prep_dataset.loc[rv_prep_dataset['numOfmonth'] <= numOfMonth]
rv_sel_dataset = rv_sel_dataset.loc[rv_sel_dataset['numOfToken'] >= minNumToken]
rv_sel_dataset = rv_sel_dataset.loc[rv_sel_dataset['numOfToken'] <= maxNumToken]
rv_sel_dataset.to_excel('../data/tokenized_review/rv_sel_dataset.xlsx')

# To seperate the dataset based on review ratings
rv_pos_dataset = rv_sel_dataset.loc[rv_sel_dataset['reviewRating'] >= 4]
rv_neg_dataset = rv_sel_dataset.loc[rv_sel_dataset['reviewRating'] <= 2]

# To save the dataframes
rv_pos_dataset.to_excel('../data/tokenized_review/rv_pos_dataset.xlsx')
print("The file name with positive reviews: rv_pos_dataset.xlsx")
rv_neg_dataset.to_excel('../data/tokenized_review/rv_neg_dataset.xlsx')
print("The file name with negative reviews: rv_neg_dataset.xlsx")
print("The dataset sepeartion based on review ratings is finished! Please check out the files.\n")
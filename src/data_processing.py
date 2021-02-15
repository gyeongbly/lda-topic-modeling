# To handle data with several rows and columns
import pandas as pd
# To support the regular expression
import re
# The Mecab for the morpheme analyzer
from konlpy.tag import Mecab
# To import dataset:
# 1) collected review dataset
# 2) dataset to refer to preprocess
# 3) app list to initially exclude
from data_preparation import rv_dataset, prep_dataset, exclude_app_list
# To ignore an error message 'SettingWithCopyWarning'
pd.options.mode.chained_assignment = None 

# To remove all of non-Korean
def text_cleaning(doc):
    doc = re.sub("[^가-힣 ]", "", doc)
    return doc

# In the first preprocessing step
# To replace a word to unify the specific word as the synonym
def text_replace_init(doc):
    for i in range(len(prep_dataset['before_replace'].dropna())):
        doc = re.sub(prep_dataset['before_replace'][i], prep_dataset['after_replace'][i], doc)
    return doc

# In the final preprocessing step (after the tokzenization)
# To replace a word to unify the specific word as the synonym
def text_replace_fin (doc):
    for i in range(len(prep_dataset['before_replace_fin'].dropna())):
        if (doc == prep_dataset['before_replace_fin'][i]):
            doc = prep_dataset['after_replace_fin'][i]
        else:
            pass
    return doc

# A class for the tokenization
class MyTokenizer:
    def __init__(self, tagger):
        self.tagger = tagger
    def __call__(self, sent):
        try:
            sent = text_cleaning(sent)
            sent = text_replace_init(sent)
            nouns = self.tagger.nouns(sent)
            valid_noun = []
            for noun in nouns:
                '''
                The only tokenized words fitting one of two conditions below will be appended 
                to a list to be utilized for the opinion mining.
                

                cond 1) if a length of tokenized word is one and the word belongs to the pre-defined list,
                the word will be replaced with the specific synonym and appended to be utilized for the opinion mining.
                '''
                if ( (len(noun) == 1) and (noun in list(prep_dataset['one_char'].dropna()))):
                    # To replace a word to unify the specific word as the synonym 
                    noun = text_replace_fin(noun)
                    valid_noun.append(noun)

                '''
                cond 2) if a length of tokenized word is more than one and the word not belongs to the list of stopwords,
                it will be appended to a list to be utilized for the opinion mining.
                '''
                
                if ((len(noun) > 1) and (noun not in list(prep_dataset['stopword'].dropna()))):
                    valid_noun.append(noun)

            return valid_noun
        except Exception as e:
            return e
            
# To define a tokenizer with the Mecab
my_tokenizer = MyTokenizer(Mecab())

# In the initial step to exclude some apps
rv_prep_dataset = rv_dataset
print("{} apps will be excluded!".format(len(exclude_app_list)))
for i in range(len(exclude_app_list)):
    rv_prep_dataset = rv_prep_dataset.loc[rv_prep_dataset['appName'] != exclude_app_list['appName'][i]]
# To store the dataset after some app exclusion
rv_prep_dataset.to_excel('../data/preprocessed_review/rv_excluded_dataset.xlsx')
# To add a column in the dataset to store tokenized nouns
rv_prep_dataset['reviewContentNouns'] = ''
# To count the number of token (nouns)
rv_prep_dataset['numOfToken'] = ''
print("The review dataset will be tokenized by the noun extracter of the Mecab")

# To tokenize preprocessed reviews
for i in range(len(rv_prep_dataset)):
    try:
        # To tokenize reviews
        tok_nouns_v = my_tokenizer(rv_prep_dataset['reviewContentRaw'][i])
        # To store the tokenized review
        rv_prep_dataset['reviewContentNouns'][i] = tok_nouns_v
        # To count the number of tokens
        rv_prep_dataset['numOfToken'][i] = len(tok_nouns_v)
    except Exception as e:
        print("Error occurred at the {} reveiew: {}".format(i, e))
rv_prep_dataset.to_excel('../data/preprocessed_review/rv_prep_dataset.xlsx')
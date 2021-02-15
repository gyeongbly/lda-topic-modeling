from data_selection import *
from topic_modeling import *

# To ignore error message 'DeprecationWarning'
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import imp

# To conduct LDA Topic Modeling based on sentiments of review dataset
for sentiment in ['pos', 'neg']:
    if (sentiment == 'pos'):
        # To convert string to list in positive review dataset
        doc_list = str_to_list(rv_pos_dataset)
    else:
        # To convert string to list in negative review dataset
        doc_list = str_to_list(rv_neg_dataset)
    # To set a file name for stroing result of visualized lda topic modeling
    fileName = 'lda_' + str(numOfMonth) + 'm' + '_' + str(minNumToken) + 'to' + str(maxNumToken) + '_' + sentiment + '.html'
    modeling(doc_list, fileName)
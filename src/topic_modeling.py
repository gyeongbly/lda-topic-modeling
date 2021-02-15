from gensim import corpora
from gensim import models
import pyLDAvis
import pyLDAvis.gensim
import re

# To activate pyLDAvis to excute on jupyter notebook
# pyLDAvis.enable_notebook()

# To declare the number of topic and keyword in the topics
num_topic = 10
num_keyword = 10

# To build a documnet-term matrix
def build_doc_term_mat(docs):    
    print("Building a document-term matrix will be started.")
    # To encapsulate the mapping between normalized words and their integer ids
    dictionary = corpora.Dictionary(docs)
    # To convert a collection of words to its bag-of-words
    corpus = [dictionary.doc2bow(doc) for doc in docs]
    return corpus, dictionary

# To print out the result of topic modeling
def print_topic_words(model):
    print("\nPrinting topic words.\n")
    for topic_id in range(model.num_topics):
        topic_word_probs = model.show_topic(topic_id, num_keyword)
        print("Topic ID: {}".format(topic_id))
        for topic_word, prob in topic_word_probs:
            print("\t{}\t{}".format(topic_word, prob))
        print("\n")

# To convert data with string type into list type
def str_to_list (docs):
    docs_list = []
    for i in range(len(docs)):
        print("docs: ", docs)
        doc = re.sub("[^가-힣,]", "", str(docs['reviewContentNouns'][docs.index[i]]))
        doc = doc.split(',')
        docs_list.append(doc)
    return docs_list

# To conduct LDA Topic Modeling
def modeling(docs_list, fileName):
    # To build a documnet-term matrix
    corpus, dictionary = build_doc_term_mat(docs_list)
    '''
        To build a LDA Topic Model
        1) Alpha 
            - To provide a value for the likelihood that an unseen review will fall into each topic.
            - The lower alpha value is, the closer new reviews fit to topics,
            instead of being a mix of several topics.
        2) Eta
            - To decide how many terms belong to a topic.
            - The lower Eta value is, the fewer topics have words.
    '''
    lda_model = models.ldamodel.LdaModel(corpus = corpus, num_topics=num_topic, id2word=dictionary, alpha="auto", eta="auto")
    lda_model.save('../data/model/lda_model')
    # To print out the results of topic modeling
    print_topic_words(lda_model)
    # To transform and prepare LDA model data for visualization
    data = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary)
    # To set up a location to store a result of LDA topic modeling
    filePath = '../data/result_lda/'
    pyLDAvis.display(data)
    # To save the visualized data to a standalone HTML file
    pyLDAvis.save_html(data, filePath+fileName)

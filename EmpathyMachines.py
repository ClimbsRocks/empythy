import csv
import os

from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

import utils

module_path = os.path.dirname(__file__)

class EmpathyMachines(object):

    def __init__(self):
        pass

    def train(self, corpus='Twitter', corpus_array=None):
        corpus_file_path = os.path.join(module_path, 'corpora', 'aggregatedCorpusCleaned.csv')
        if corpus == 'passed_in_argument':
            raw_data = corpus_array
        else:
            raw_data = utils.load_dataset(corpus_file_path)
        # print('raw_data[:10]')
        # print(raw_data[:10])

        corpus_strings, sentiments = utils.clean_initial_data(raw_data, confidence_threshold=0.5)

        print('len(corpus_strings)')
        print(len(corpus_strings))
        print(corpus_strings[:10])
        print('len(sentiments)')
        print(len(sentiments))
        print(sentiments[:10])

        tfidf = TfidfVectorizer(
            # if we fail to parse a given character, just ignore it
            decode_error='ignore',
            # strip accents from characters
            strip_accents='unicode',
            # break the string apart into words, not characters
            analyzer='word',
            # get words in groups that range in length from 1 - 4. So "I love DoorDash" turns into "I", "love", "I love", "I love DoorDash"...
            ngram_range=(1,4),
            # instead of using pre-defined stopwords, ignore all words that have an intra-document frequency > 0.7
            # (ignore all words/phrases that appear in more than 70% of our documents)
            max_df=0.7,
            # stop_words are commonly used words that don't likely differentiate a message ('of','me','a', etc.)
            stop_words='english',
            # convert all characters to lowercase
            lowercase=True,
            # keep only this many features (all features if None)
            max_features=3000,
            # smooth idf weights to prevent zero divisions
            smooth_idf=True
        )

        sparse_transformed_corpus = tfidf.fit_transform(corpus_strings)
        X_train, X_test, y_train, y_test = train_test_split(sparse_transformed_corpus, sentiments, test_size=0.2)

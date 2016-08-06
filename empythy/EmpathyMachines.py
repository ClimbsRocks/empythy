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


    def train(self, corpus='Twitter', corpus_array=None, print_analytics_results=False, verbose=False, file_name=None):

        if print_analytics_results:
            verbose = True

        if verbose:
            print('Loading the corpus')

        if corpus.lower() == 'custom':
            raw_data = corpus_array

        elif corpus.lower() == 'twitter':
            corpus_file_path = os.path.join(module_path, 'corpora', 'aggregatedCorpusCleanedAndFiltered.csv')
            raw_data = utils.load_dataset(corpus_file_path)

        elif corpus.lower() == 'moviereviews':
            raw_data = utils.load_movie_reviews()

        confidence_threshold = None
        if corpus.lower() == 'twitter':
            confidence_threshold = 0.3

        corpus_strings, sentiments = utils.clean_initial_data(raw_data, confidence_threshold=confidence_threshold)

        if verbose:
            print('Running TfidfVectorizer on the corpus')

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
            max_features=20000,
            # smooth idf weights to prevent zero divisions
            smooth_idf=True
        )

        sparse_transformed_corpus = tfidf.fit_transform(corpus_strings)

        self.tfidf_transformer = tfidf

        if print_analytics_results:
            X_train, X_test, y_train, y_test = train_test_split(sparse_transformed_corpus, sentiments, test_size=0.2)
        else:
            X_train = sparse_transformed_corpus
            y_train = sentiments

        model = LogisticRegression()

        if verbose:
            print('Training the model')

        model.fit(X_train, y_train)

        self.trained_model = model

        if print_analytics_results:
            print('Model\'s score on the training data:')
            print(self.trained_model.score(X_train, y_train))
            print('Model\'s score on the holdout data:')
            print(self.trained_model.score(X_test, y_test))

        if verbose:
            print('Finished training!')


    def predict(self, text):
        if isinstance(text, basestring):
            transformed_text = self.tfidf_transformer.transform([text])
        # check for all forms of "lists", but only after determining that this is not a string.
        # this will probably break in some edge cases, but should be fine for most standard user behavior
        elif hasattr(text, "__len__"):
            transformed_text = self.tfidf_transformer.transform(text)

        # TODO(PRESTON):
            # consider formatting the output based on the input type
            # so if we get passed in a string, just return a string
            # whereas if we get passed an array, return an array.

        return self.trained_model.predict(transformed_text)
